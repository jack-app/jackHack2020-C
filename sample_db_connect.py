import psycopg2
from dotenv import load_dotenv

import os

# .env から読み込み
load_dotenv(verbose=True)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
dbname = os.environ.get("POSTGRES_DB")

# DBに接続
conn = psycopg2.connect(user=user, password=password, host="db_container", port="5432", database=dbname)

# excexute sql
cur = conn.cursor()
cur.execute('SELECT * FROM test;')
results = cur.fetchall()

#output result
print(results)

cur.close()
conn.close()
