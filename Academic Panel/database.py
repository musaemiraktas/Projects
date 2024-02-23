import psycopg2

def connect_to_database(username, password, host, port, database):
    return psycopg2.connect(
        dbname=database,
        user=username,
        password=password,
        host=host,
        port=port
    )

def query_database(conn, query, parameters=None):
    cur = conn.cursor()
    cur.execute(query, parameters)
    return cur.fetchall()

def add_database():
    pass

def get_user_credentials(conn, user_id): # daha iyisini yazdığım için gerek kalmadı
    query = "SELECT username, password FROM users WHERE id = %s"
    parameters = (user_id,)
    result = query_database(conn, query, parameters)
    if result:
        return result[0]  # İlk sıradaki (username, password) tuple'ı döndür
    else:
        return None  # Kullanıcı bulunamazsa None döndür

