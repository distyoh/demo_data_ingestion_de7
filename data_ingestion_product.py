import psycopg2
import os

#connection
SQL_USER = os.environ.get('OLTP_USERNAME')
SQL_PASS = os.environ.get('OLTP_PASSWORD')
SQL_HOST = os.environ.get('OLTP_HOST')
SQL_PORT = os.environ.get('OLTP_PORT')
SQL_DB   = os.environ.get('OLTP_DATABASE')

conn = psycopg2.connect(host=SQL_HOST, dbname=SQL_DB, user=SQL_USER, password=SQL_PASS, port=SQL_PORT)
cur = conn.cursor() #perintah untuk membuka dan menutup koneksi dengan bantuan cursor untuk meenjalankan query

#export to csv
csv_file = open('yudistia_products.csv','w')
sql = 'COPY (SELECT * FROM PRODUCTS) TO STDOUT WITH CSV HEADER'

cur.copy_expert(sql,csv_file)
csv_file.close()
cur.close
conn.close