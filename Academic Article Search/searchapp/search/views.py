from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup
import re
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from searchapp.mongo_connection import collection
from django.http import FileResponse
from urllib.parse import unquote



# Create your views here.  37
def home(request):
    return render(request, "search/index.html")

def clean_title(title):
    cleaned_title = re.sub(r'\[PDF\]', '', title)
    cleaned_title = re.sub(r'\[KİTAP\]', '', cleaned_title)
    cleaned_title = re.sub(r'\[B\]', '', cleaned_title)
    cleaned_title = re.sub(r'\[HTML\]', '', cleaned_title)
    cleaned_title = re.sub(r'\[C\]', '', cleaned_title)
    cleaned_title = re.sub(r'\[ALINTI\]', '', cleaned_title)
    return cleaned_title

def extract_author(raw_author):
    try:
        return raw_author.split('-')[0].strip()
    except IndexError:
        return "bulunamadı"

def extract_publisher(raw_publisher):
    try:
        return raw_publisher.split('-')[1].split(',')[0].strip()
    except IndexError:
        return "bulunamadı"

def extract_pubdate(raw_date):
    try:
        return raw_date.split('-')[1].split(',')[1].strip()
    except IndexError:
        return "bulunamadı"
    
    
def isDergipark(link):
    control = link[:37]
    if control[:28] == "https://dergipark.org.tr/en/" or control[:28] == "https://dergipark.org.tr/tr/":
        if control[-10:] == "/download/":
            return "download_link"
        else:
            return link
    else:
        return False
    
def getDataFromDergiPark(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
    }
    response = requests.get(link, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find("div", class_="kt-content kt-grid__item kt-grid__item--fluid")
        if articles:
            return articles
        else:
            return None
    else:
        return None

def download_pdf(request, path_to_pdf, title):
    response = requests.get(path_to_pdf, stream=True)
    response.raise_for_status()  # Hata kontrolü
    filename = f"{path_to_pdf.split('/')[-1]}.pdf"

    response = FileResponse(response.raw, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response

def article_detail(request, title):
    title = unquote(title)  # URL'den gelen kodlanmış başlığı çözüyorum
    article = collection.find_one({'title': title})
    return render(request, 'search/article_detail.html', {'article': article})



    

def google_scholar_search(query):
    true_query = None
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
    }
    base_url = "https://scholar.google.com.tr/scholar"
    params = {"q": query}

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("div", class_="gs_r gs_or gs_scl")
        
        query_div = soup.find("div", class_="gs_r")
        if query_div:
            query_h2 = query_div.find("h2", class_="gs_rt")
            if query_h2:
                true_query = query_h2.get_text()


        results = []
        for i, article in enumerate(articles[:10]):
            title = article.find("h3", class_="gs_rt").get_text(strip=False)
            title = clean_title(title)
            authors = article.find("div", class_="gs_a").get_text(strip=True)
            raw_all = authors
            authors = extract_author(authors)
            publisher = extract_publisher(raw_all)
            pub_date = extract_pubdate(raw_all)
            section = ""
            abstract = ""
            keywords = ""
            citations = ""
            cit_num = ""
            doi_link = ""
            doi_num = ""

            titleLink1 = article.find("div", class_="gs_ri")
            title_Link = titleLink1.find("h3", class_="gs_rt")
            a_tag = title_Link.find("a") if title_Link else None  

            if a_tag and "href" in a_tag.attrs:
                titleLink2 = a_tag["href"]
                isDergipark_result = isDergipark(titleLink2)
            else:
                
                titleLink2 = None
                
            

            
            if isDergipark_result == "download_link" or isDergipark_result == titleLink2:
                if isDergipark_result == "download_link":
                    print(f"{i+1}. dergipark ama sadece makale indirme linki içeriyor")
                if isDergipark_result == titleLink2:
                    articles2 = getDataFromDergiPark(titleLink2)
                    if articles2:
                        publisher = articles2.find("h1", id="journal-title").text
                        tab_content = articles2.find("div", class_="tab-content")
                        tab_content = tab_content.find("div", id="article_tr")
                        title = tab_content.find("h3", class_="article-title").text.strip()
                        properties_table = articles2.find("table", class_="record_properties table")
                        doi_link = tab_content.find("a", class_="doi-link")
                        cit_num = tab_content.find("div", class_="mt-3")
                        
                    else:
                        print(f"Error fetching data from DergiPark for link: {titleLink2}")
                    
                    if properties_table:
                        rows = properties_table.find_all("tr")
                        authors_list = []
                        for row in rows:
                            th = row.find("th")
                            if th and "Publication Date" in th.text:
                                td = row.find("td")
                                if td:
                                    pub_date = td.text
                            if th and "Authors" in th.text:
                                author_ps = row.find_all("p", id = lambda x: x and x.startswith('author'))
                                for p in author_ps:
                                    author_info = p.find('span', style="font-weight: 600")
                                    if author_info:
                                        author_name_parts = author_info.get_text(strip=True).split("This is me")
                                        author_name = author_name_parts[0].strip() if author_name_parts else ''
                                        authors_list.append(author_name)
                                    else:
                                        author_info = p.find("a", style="font-weight: 600")
                                        if author_info:
                                            author_name_parts = author_info.get_text(strip=True).split("This is me")
                                            author_name = author_name_parts[0].strip() if author_name_parts else ''
                                            authors_list.append(author_name)
                                authors = ", ".join(authors_list)
                            if th and "Journal Section" in th.text:
                                td = row.find("td")
                                if td:
                                    section = td.text


                    if articles2:
                        general_body = articles2.find("div", class_="kt-portlet__body")
                        abstract1 = general_body.find("div", class_="article-abstract data-section")
                        abstract = abstract1.find("p").get_text()
                        
                        keywords1 = general_body.find("div", class_="article-keywords data-section")
                        if keywords1:
                            keywords2 = keywords1.find("p")
                            if keywords2:
                                a_tags = keywords2.find_all("a")
                                keywords3 = [a.text for a in a_tags]
                                keywords = ", ".join(keywords3)
                        
                        citations1 = general_body.find("div", class_="article-citations data-section")
                        if citations1:
                            citations2 = citations1.find("ul", class_="fa-ul")
                            if citations2:
                                citations3 = citations2.find_all("li")
                                citations4 = []
                                if citations3:
                                    for citation in citations3:
                                        cit_info = citation.text
                                        citations4.append(cit_info)
                                    citations = "\n".join(f"----{index + 1}. {item}" for index, item in enumerate(citations4))

                        if cit_num:
                            cit_num = cit_num.getText(strip=True)
                            cit_num = cit_num[10:]
                        else:
                            cit_num = "-"


                        if doi_link:
                            doi_link = doi_link.text
                            doi_num = doi_link[16:]
                        else:
                            doi_num = "-"
   
            else:
                print(f"{i+1}. dergipark değil")
            
            if article.find("div", class_="gs_ri") and article.find("div", class_="gs_ggs gs_fl"):
                link = article.find("a")["href"]
            else:
                link = None
            result = {
                        'title': title,
                        'authors': authors,
                        'section': section,
                        'publisher': publisher,
                        'pub_date': pub_date,
                        'keywords': keywords,
                        'abstract': abstract,
                        'citations': citations,
                        'cit_num': cit_num,
                        'doi_num': doi_num,
                        'link': link,
                    }
            results.append(result)
        
        query_corrected = query != true_query if true_query else False
        return results, true_query, query_corrected
    else:
        return [], None



def search(request):
    query = request.GET.get('aranan', '')
    #siralama = request.GET.get('siralama', 'en_yeni')
    query_true = None
    query_corrected = False
    results = []
    context = {'query': query, 'results': results, 'query_true': query_true}

    last_article = collection.find_one(sort=[("article_id", -1)])
    if last_article:
        article_id = last_article['article_id'] + 1
    else:
        article_id = 0

    if query:
        existing_queries = list(collection.find({"search_query": query}))

        if len(existing_queries) > 0:
            results.extend(existing_queries)
        else:
            new_results, query_true, query_corrected = google_scholar_search(query)
            for result in new_results:
                document = {
                    "article_id": article_id,
                    "search_query": query,
                    "title": result['title'],
                    "authors": result['authors'],
                    "section": result['section'],
                    "publisher": result['publisher'],
                    "pub_date": result['pub_date'],
                    "keywords": result['keywords'],
                    "abstract": result['abstract'],
                    "citations": result['citations'],
                    "cit_num": result['cit_num'],
                    "doi_num": result['doi_num'],
                    "link": result['link'],
                }
                collection.insert_one(document)
                results.append(document)
                article_id += 1


    
    context['results'] = results
    context['query_true'] = query_true
    context['query_corrected'] = query_corrected
    return render(request, 'search/search_results.html', context)