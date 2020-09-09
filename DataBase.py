import sqlite3  # import library for DB

conn = sqlite3.connect('mydatabase.db')  # make connect to DB

cursor = conn.cursor()  # make cursor for ask and get answer from DB

# cursor.execute("""CREATE TABLE Albums
#          (title text, artist text, release_date text, publisher text, media_type text)
#    """)
# conn.commit()

cursor.execute("SELECT artist text FROM Albums LIMIT 5")
result = cursor.fetchall()
result1 = cursor.fetchall()

print(result)
print(result1)

# cursor.execute("""INSERT INTO albums
#                   VALUES ('Master Of Puppets', 'Metallica', '12.08.1984',
#                   'Electric Records', 'Flac')"""
#                )

albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)

conn.commit()

conn.close()
