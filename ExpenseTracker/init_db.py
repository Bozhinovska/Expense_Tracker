import sqlite3

def initialize_database():
    conn = sqlite3.connect('database.db')
    conn.close()

if __name__ == '__main__':
    initialize_database()
    print('Database initialized.')