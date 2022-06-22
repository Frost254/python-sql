import psycopg2

connection = psycopg2.connect('dbname=HP')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Table2')
\
cursor.execute('''
               CREATE TABLE table2 (
                   id INTEGER PRIMARY KEY,
                   completed BOOLEAN NOT NULL DEFAULT False
               );
               ''')

cursor.execute('INSERT INTO table2(id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2(id, completed) VALUES (%(id)s, %(completed)s);'
Data = {
    'id': 2,
    'completed': True
}

cursor.execute(SQL, Data)

cursor.execute('INSERT INTO table2(id, completed) VALUES (%s, %s);', (3, False))

cursor.execute('SELECT * from table2;')

result = cursor.fetchmany(2)

print('fetchmany',result)

result2 = cursor.fetchone()

print('fetchone',result2)

connection.commit()

connection.close()
cursor.close()


