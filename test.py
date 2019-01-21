import psycopg2 as sql

connection = sql.connect(database='postgres', user='baris',
                         password='4865', host='localhost', port='5432')

cursor = connection.cursor()
cursor.execute("SELECT * FROM address")
records = cursor.fetchall()
print(records)
