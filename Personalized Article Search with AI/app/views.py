import json
import os
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from pymongo import MongoClient
from django.contrib import messages
import numpy as np
import fasttext
import spacy
from transformers import AutoModel, AutoTokenizer

model = fasttext.load_model('C:\VSCode_Projects\yazlab3_3\cc.en.300.bin')
nlp = spacy.load('en_core_web_sm')


tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
scibert_model = AutoModel.from_pretrained('allenai/scibert_scivocab_uncased')

def get_mongo_collection():
    client = MongoClient('mongodb+srv://aktasmusaemir:denemesifre@emiraktas.jikcnjp.mongodb.net/')
    db = client['yazlab3']
    return db['users']

# login fonksiyonu
def login(request):
    print("Login method called with method:", request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("Attempting to log in with username:", username)
        collection = get_mongo_collection()
        user = collection.find_one({'username': username, 'password': password})
        if user:
            print("Login successful for:", username)
            return redirect('/home/?username=' + username)
        else:
            print("Login failed for username:", username)
            return HttpResponse('Invalid login')
    return render(request, "app/login.html")


def register(request):
    print("register")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        birth_place = request.POST.get('birth_place')
        gender = request.POST.get('gender')
        interests = request.POST.get('interests')

        collection = get_mongo_collection()

        if collection.find_one({'username': username}):
            messages.error(request, 'Bu kullanıcı adı zaten kullanılıyor.')
            return render(request, 'app/register.html')

        interests = request.POST.get('interests').split(',')  # Virgülle ayrılmış ilgi alanlarını liste yapar
        user_data = {
            "username": username,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date,
            "birth_place": birth_place,
            "gender": gender,
            "interests": interests,  # Liste olarak kaydet
            "fasttext_tp": 0,
            "fasttext_fp": 0,
            "scibert_tp": 0,
            "scibert_fp": 0,
        }
        
        collection.insert_one(user_data)
        return redirect('login')
    else:
        return render(request, 'app/register.html')

def search_for_articles(query, directory, username):
    print("search_for_articles")
    try:
        query_lemmas = lemmatize_text(query)
        articles = {}
        fasttext_results = {}
        scibert_results = {}
        
        client = MongoClient('mongodb+srv://aktasmusaemir:denemesifre@emiraktas.jikcnjp.mongodb.net/')
        db = client['yazlab3']
        fasttext_collection = db['article_vectors']
        scibert_collection = db['scibert_article_vectors']
        users_collection = db['users']

        user = users_collection.find_one({'username': username})
        if not user:
            print("User not found.")
            return {}

        fasttext_user_vector = get_user_vector(user['interests'])
        scibert_user_vector = get_user_vector_scibert(user['interests'])

        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
                    title_start = content.find('--T') + 3
                    title_end = content.find('--A', title_start)
                    title = content[title_start:title_end].strip()
                    title_lemmas = lemmatize_text(title)

                    if query_lemmas & title_lemmas:
                        fasttext_article = fasttext_collection.find_one({'filename': filename.replace('.txt', '')})
                        scibert_article = scibert_collection.find_one({'filename': filename.replace('.txt', '')})
                        
                        if fasttext_article and scibert_article:
                            fasttext_vector = np.array(fasttext_article['vector'])
                            scibert_vector = np.array(scibert_article['vector'])

                            fasttext_score = cosine_similarity(fasttext_user_vector, fasttext_vector)
                            scibert_score = cosine_similarity(scibert_user_vector, scibert_vector)

                            fasttext_results[filename] = {
                                'filename': filename.replace('.txt', ''),
                                'title': title,
                                'similarity_score': fasttext_score,
                                'username': username,
                            }
                            scibert_results[filename] = {
                                'filename': filename.replace('.txt', ''),
                                'title': title,
                                'similarity_score': scibert_score,
                                'username': username,
                            }

        # En yüksek benzerlik puanına sahip ilk 5 makaleyi her model için seç
        top_fasttext_articles = sorted(fasttext_results.items(), key=lambda x: x[1]['similarity_score'], reverse=True)[:5]
        top_scibert_articles = sorted(scibert_results.items(), key=lambda x: x[1]['similarity_score'], reverse=True)[:5]

        return {
            'fasttext_articles': {filename: details for filename, details in top_fasttext_articles},
            'scibert_articles': {filename: details for filename, details in top_scibert_articles}
        }

    except Exception as e:
        print(f"Error in search_for_articles: {str(e)}")

    return {'fasttext_articles': {}, 'scibert_articles': {}}



def home(request):
    username = request.GET.get('username')
    if username:
        collection = get_mongo_collection()
        user = collection.find_one({'username': username})
        if user:
            interests = user.get('interests')
            fasttext_user_vector = get_user_vector(interests)
            scibert_user_vector = get_user_vector_scibert(interests)
            
            fasttext_articles = get_recommended_articles(fasttext_user_vector, 'fasttext')
            scibert_articles = get_recommended_articles(scibert_user_vector, 'scibert')

            fasttext_tp = user.get('fasttext_tp', 0)
            fasttext_fp = user.get('fasttext_fp', 0)
            scibert_tp = user.get('scibert_tp', 0)
            scibert_fp = user.get('scibert_fp', 0)

            fasttext_precision = calculate_precision(fasttext_tp, fasttext_fp)
            scibert_precision = calculate_precision(scibert_tp, scibert_fp)

            return render(request, 'app/home.html', {
                'username': username,
                'fasttext_articles': fasttext_articles,
                'scibert_articles': scibert_articles,
                'fasttext_precision': fasttext_precision,
                'scibert_precision': scibert_precision,
            })
        else:
            return HttpResponse('Kullanıcı bulunamadı.', status=404)
    else:
        return redirect('login')

    
def get_recommended_articles(user_vector, model_type):
    client = MongoClient('mongodb+srv://aktasmusaemir:denemesifre@emiraktas.jikcnjp.mongodb.net/')
    db = client['yazlab3']
    
    if model_type == 'fasttext':
        collection = db['article_vectors']
    elif model_type == 'scibert':
        collection = db['scibert_article_vectors']
    else:
        return []

    articles = list(collection.find({}))
    article_similarities = []

    for article in articles:
        article_vector = np.array(article['vector'])
        similarity = cosine_similarity(user_vector, article_vector)
        title = get_article_title(article['filename'])
        article_similarities.append((article['filename'], title, similarity))
    
    # En yüksek benzerlik skoruna sahip ilk 5 makaleyi seç
    top_articles = sorted(article_similarities, key=lambda x: x[2], reverse=True)[:5]
    
    return [{'filename': a[0], 'title': a[1], 'similarity_score': a[2]} for a in top_articles]

def get_article_title(filename):
    txt_directory = 'C:/VSCode_Projects/yazlab3_3/Krapivin2009/Krapivin2009/docsutf8'
    txt_path = os.path.join(txt_directory, filename + '.txt')

    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            content = file.read()
            title_start = content.find('--T') + 3
            title_end = content.find('--A', title_start)
            title = content[title_start:title_end].strip()
            return title
    except FileNotFoundError:
        return 'No Title'



def search_articles(request):
    print("search_articles")
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        username = request.POST.get('username')

        if not username:
            return HttpResponse('Kullanıcı adı eksik.', status=400)

        directory = r'C:\VSCode_Projects\yazlab3_3\Krapivin2009\Krapivin2009\docsutf8'

        collection = get_mongo_collection()
        user = collection.find_one({'username': username})

        if user:
            update_user_interests(collection, username, search_query)
        else:
            return HttpResponse('Kullanıcı bulunamadı.', status=404)

        results = search_for_articles(search_query, directory, username)
        fasttext_articles = results.get('fasttext_articles', {})
        scibert_articles = results.get('scibert_articles', {})

        # Precision değerlerini hesapla
        fasttext_tp = user.get('fasttext_tp', 0)
        fasttext_fp = user.get('fasttext_fp', 0)
        scibert_tp = user.get('scibert_tp', 0)
        scibert_fp = user.get('scibert_fp', 0)

        fasttext_precision = calculate_precision(fasttext_tp, fasttext_fp)
        scibert_precision = calculate_precision(scibert_tp, scibert_fp)

        # Makale sonuçlarına model bilgisini ekleyelim
        for article in fasttext_articles.values():
            article['model'] = 'fasttext'
        for article in scibert_articles.values():
            article['model'] = 'scibert'

        return render(request, 'app/search_results.html', {
            'fasttext_articles': fasttext_articles,
            'scibert_articles': scibert_articles,
            'fasttext_precision': fasttext_precision,
            'scibert_precision': scibert_precision,
            'username': username 
        })
    else:
        return render(request, 'app/home.html')


    
def cosine_similarity(vec1, vec2):
    print("cosine_similarity")
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0
    similarity = dot_product / (norm_vec1 * norm_vec2)
    return similarity 


def view_article(request, filename):
    print("view_article")
    print(filename)
    txt_directory = 'C:/VSCode_Projects/yazlab3_3/Krapivin2009/Krapivin2009/docsutf8'
    key_directory = 'C:/VSCode_Projects/yazlab3_3/Krapivin2009/Krapivin2009/keys'
    txt_path = os.path.join(txt_directory, filename + '.txt')
    key_path = os.path.join(key_directory, filename + '.key')

    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            content = file.read()
            title_start = content.find('--T') + 3
            title_end = content.find('--A', title_start)
            summary_start = content.find('--A') + 3
            summary_end = content.find('--B', summary_start)

            title = content[title_start:title_end].strip()
            summary = content[summary_start:summary_end].strip()

        with open(key_path, 'r', encoding='utf-8') as file:
            keywords = file.read().strip().split('\n')

        return render(request, 'app/view_article.html', {
            'title': title,
            'summary': summary,
            'keywords': keywords
        })

    except FileNotFoundError:
        return HttpResponse('Dosya bulunamadı', status=404)
    



def create_vectors(summaries, model):
    print("create_vectors")
    return {filename: model.get_sentence_vector(summary) for filename, summary in summaries.items()}

def update_user_interests(collection, username, new_interest):
    print("update_user_interests")
    user = collection.find_one({'username': username})
    if user:
        current_interests = user.get('interests', [])
        
        # Eğer current_interests bir string ise, bir liste olarak değiştirin
        if isinstance(current_interests, str):
            current_interests = [current_interests]  # Mevcut ilgi alanını liste yap
        
        if new_interest not in current_interests:
            current_interests.append(new_interest)
            collection.update_one({'username': username}, {'$set': {'interests': current_interests}})
    else:
        raise Exception('Kullanıcı bulunamadı.')
    
def lemmatize_text(text):
    #
    doc = nlp(text.lower())
    return {token.lemma_ for token in doc}

def read_key_file(txt_filename):
    print("read_key_file")
    base_path = 'C:/VSCode_Projects/yazlab3_3/Krapivin2009/Krapivin2009/keys'
    key_filename = os.path.basename(txt_filename).replace('.txt', '.key')
    key_path = os.path.join(base_path, key_filename)
    try:
        with open(key_path, 'r', encoding='utf-8') as file:
            keywords = file.read().strip().split('\n')
        return keywords
    except FileNotFoundError:
        return []
    
def get_user_vector(interests):
    print("get_user_vector")
    """ Kullanıcının ilgi alanlarından vektör oluşturur. """
    vectors = [model.get_sentence_vector(interest) for interest in interests]
    user_vector = np.mean(vectors, axis=0)
    #print("user vector:", user_vector)
    return user_vector

def get_user_vector_scibert(interests):
    print("get_user_vector_scibert")
    """ Kullanıcının ilgi alanlarından SciBERT ile vektör oluşturur. """
    vectors = []
    for interest in interests:
        inputs = tokenizer(interest, return_tensors="pt", padding=True, truncation=True)
        outputs = scibert_model(**inputs)
        # Çıktıların ortalamasını alıyoruz.
        vector = outputs.last_hidden_state.mean(dim=1).detach().numpy()
        vectors.append(vector[0])  # Batch boyutunu kaldır
    user_vector = np.mean(vectors, axis=0)
    return user_vector


def add_interests(username, new_interests):
    """Kullanıcının ilgi alanları listesine yeni kelimeler ekler."""
    client = MongoClient('mongodb+srv://aktasmusaemir:denemesifre@emiraktas.jikcnjp.mongodb.net/')
    db = client['yazlab3']
    users_collection = db['users']
    user = users_collection.find_one({'username': username})
    if user:
        current_interests = user.get('interests', [])
        updated_interests = list(set(current_interests + new_interests))  # Yeni ilgi alanlarını ekleyin
        users_collection.update_one({'username': username}, {'$set': {'interests': updated_interests}})


@csrf_exempt
def add_keywords_to_interests(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        filename = data.get('filename')
        model = data.get('model')
        print("username:", username)
        print("filename:", filename)
        print("model:", model)

        key_directory = 'C:/VSCode_Projects/yazlab3_3/Krapivin2009/Krapivin2009/keys'
        key_path = os.path.join(key_directory, filename + '.key')

        try:
            with open(key_path, 'r', encoding='utf-8') as file:
                keywords = file.read().strip().split('\n')

            client = MongoClient('mongodb+srv://aktasmusaemir:denemesifre@emiraktas.jikcnjp.mongodb.net/')
            db = client['yazlab3']

            # MongoDB koleksiyonunu al ve ilgi alanlarını güncelle
            users_collection = db['users']
            user = users_collection.find_one({'username': username})

            if user:
                current_interests = user.get('interests', [])
                updated_interests = list(set(current_interests + keywords))
                users_collection.update_one({'username': username}, {'$set': {'interests': updated_interests}})

                # TP değerini güncelle
                if model == 'fasttext':
                    users_collection.update_one({'username': username}, {'$inc': {'fasttext_tp': 1}})
                elif model == 'scibert':
                    users_collection.update_one({'username': username}, {'$inc': {'scibert_tp': 1}})

                return JsonResponse({'status': 'success', 'message': 'Interests updated successfully.'}, status=204)
            else:
                return JsonResponse({'status': 'error', 'message': 'User not found.'})

        except FileNotFoundError:
            return JsonResponse({'status': 'error', 'message': 'Keywords file not found.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@csrf_exempt
def eject_keywords_to_interests(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        filename = data.get('filename')
        model = data.get('model')
        print("username:", username)
        print("filename:", filename)
        print("model:", model)

        key_directory = 'C:/VSCode_Projects/yazlab3_3/Krapivin2009/Krapivin2009/keys'
        key_path = os.path.join(key_directory, filename + '.key')

        try:
            with open(key_path, 'r', encoding='utf-8') as file:
                keywords = file.read().strip().split('\n')

            client = MongoClient('mongodb+srv://aktasmusaemir:denemesifre@emiraktas.jikcnjp.mongodb.net/')
            db = client['yazlab3']

            # MongoDB koleksiyonunu al ve ilgi alanlarını güncelle
            users_collection = db['users']
            user = users_collection.find_one({'username': username})

            if user:
                current_interests = set(user.get('interests', []))
                keywords_set = set(keywords)
                updated_interests = list(current_interests - keywords_set)
                users_collection.update_one({'username': username}, {'$set': {'interests': updated_interests}})

                # FP değerini güncelle
                if model == 'fasttext':
                    users_collection.update_one({'username': username}, {'$inc': {'fasttext_fp': 1}})
                elif model == 'scibert':
                    users_collection.update_one({'username': username}, {'$inc': {'scibert_fp': 1}})

                return JsonResponse({'status': 'success', 'message': 'Interests successfully removed.'}, status=204)
            else:
                return JsonResponse({'status': 'error', 'message': 'User not found.'})

        except FileNotFoundError:
            return JsonResponse({'status': 'error', 'message': 'Keywords file not found.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

    
def calculate_precision(tp, fp):
    if tp + fp == 0:
        return 0
    return tp / (tp + fp)

@csrf_exempt
def user_profile(request):
    client = MongoClient('mongodb+srv://aktasmusaemir:denemesifre@emiraktas.jikcnjp.mongodb.net/')
    db = client['yazlab3']
    users_collection = db['users']

    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            return HttpResponse('Username is missing', status=400)

        user = users_collection.find_one({'username': username})
        if user:
            first_name = request.POST.get('first_name', user.get('first_name', ''))
            last_name = request.POST.get('last_name', user.get('last_name', ''))
            birth_date = request.POST.get('birth_date', user.get('birth_date', ''))
            birth_place = request.POST.get('birth_place', user.get('birth_place', ''))
            gender = request.POST.get('gender', user.get('gender', ''))
            interests = request.POST.get('interests', ','.join(user.get('interests', ''))).split(',')

            users_collection.update_one(
                {'username': username},
                {'$set': {
                    'first_name': first_name,
                    'last_name': last_name,
                    'birth_date': birth_date,
                    'birth_place': birth_place,
                    'gender': gender,
                    'interests': interests
                }}
            )

            # Şifre değişikliği
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_new_password = request.POST.get('confirm_new_password')

            if current_password and new_password and confirm_new_password:
                if user['password'] == current_password:
                    if new_password == confirm_new_password:
                        users_collection.update_one(
                            {'username': username},
                            {'$set': {'password': new_password}}
                        )
                    else:
                        messages.error(request, "New passwords do not match.")
                else:
                    messages.error(request, "Current password is incorrect.")
        
        return redirect('/profile/?username=' + username)

    else:
        username = request.GET.get('username')
        if not username:
            return HttpResponse('Username is missing', status=400)

        user = users_collection.find_one({'username': username})
        if user:
            user_data = {
                'username': user['username'],
                'first_name': user['first_name'],
                'last_name': user['last_name'],
                'birth_date': user['birth_date'],
                'birth_place': user['birth_place'],
                'gender': user['gender'],
                'interests': ','.join(user['interests']),
            }
            return render(request, 'app/user_profile.html', {'user': user_data})
        else:
            return HttpResponse('User not found', status=404)





