import sqlite3

connection = sqlite3.connect('database.db') 
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clients (''id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'name TEXT,'
               'weight REAL'
               ')')

# cursor.execute('INSERT INTO clients (name, weight) VALUES ("Rayana Neves", 62.0)')
# connection.commit()

# Avoiding SQLInfection:
# cursor.execute('INSERT INTO clients (name, weight) VALUES (?, ?)',
#   ('Jhonnatan Panoch', 75.0))
# connection.commit()

# name = 'Jurema'
# weight = 80.0
# cursor.execute('INSERT INTO clients (name, weight) VALUES (?, ?)',
#   (name, weight))
# connection.commit()

# update
# cursor.execute('UPDATE clients SET name=? WHERE id=:id', ('Maria', 3))
# connection.commit()

# delete
# cursor.execute('DELETE FROM clients WHERE id=:id', {'id': 3})
# connection.commit()

# select
# cursor.execute('SELECT name, weight FROM clients WHERE weight>:weight', {'weight': 65.0})
# for line in cursor.fetchall():
#   print(line)
# connection.commit()

# cursor.execute('SELECT * FROM clients')
# for line in cursor.fetchall():
#   print(line)

# another way to do:
for lin in cursor.fetchall():
  index, name, weight = lin
  print(index, name, weight)
  # print(f'Index: {index}')
  # print(f'Name: {name}')
  # print(f'Weight: {weight}')

cursor.close()
connection.close()