import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn


conn = get_db_connection()
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    method_of_payment TEXT NOT NULL,
    paid_to TEXT NOT NULL,
    description TEXT NOT NULL,
    amount REAL NOT NULL


);
''')
#
# cursor.execute('''
# INSERT INTO expenses (category, amount, date)
# VALUES('economy',2560,'2025-01-22');
# ''')

# cursor.execute('''
# DROP TABLE expense
# ''')

conn.commit()
conn.close()

print("The 'expenses' table is created")
