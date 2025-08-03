import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        dbname="finalexamdb",
        user="user",
        password="pass",
        host="db",
        cursor_factory=RealDictCursor
    )

def get_all_references():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM references ORDER BY id")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def add_reference(title, pdf_url):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO references (title, pdf_url) VALUES (%s, %s)",
        (title, pdf_url)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_reference(ref_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM references WHERE id = %s", (ref_id,))
    conn.commit()
    cur.close()
    conn.close()