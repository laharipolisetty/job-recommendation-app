import sqlite3

def init_db():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_profiles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    skills TEXT,
                    experience TEXT,
                    matches TEXT,
                    gaps TEXT
                )''')
    conn.commit()
    conn.close()

def save_user_profile(name, skills, experience, matches, gaps):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO user_profiles (name, skills, experience, matches, gaps)
                 VALUES (?, ?, ?, ?, ?)''',
              (name, ', '.join(skills), experience, ', '.join(matches), ', '.join(gaps)))
    conn.commit()
    conn.close()

def fetch_profiles():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM user_profiles')
    rows = c.fetchall()
    conn.close()
    return rows
