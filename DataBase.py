import sqlite3  # import library for DB

conn = sqlite3.connect('mydatabase.db')  # make connect to DB

cursor = conn.cursor()  # make cursor for ask and get answer from DB

cursor.execute("""INSERT INTO albums
                  VALUES """)

#cursor.execute("""CREATE TABLE Albums
     #          (title text, artist text, release_date text, publisher text, media_type text)
           #    """)

#cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
#result = cursor.fetchall()
#result1 = cursor.fetchall()

#print(result)
#print(result1)

conn.close()