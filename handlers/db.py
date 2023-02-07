import sqlite3

class Users:
    def __init__(self):
        self.conn = sqlite3.connect('DB/users.db', check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id INT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            bio TEXT NOT NULL,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL
        )""")
        self.conn.commit()


    def is_correct(self, login, password):
        self.cur.execute('SELECT * FROM users WHERE email = ? AND password = ?', (login, password))
        return self.cur.fetchone()

    def get(self, login):
        self.cur.execute('SELECT * FROM users WHERE email = ?', (login,))
        return self.cur.fetchone()

    def get_count(self):
        self.cur.execute('SELECT COUNT(id) FROM users')
        return int(self.cur.fetchone()[0])

    def register(self, login, password, firstname, lastname):
        self.cur.execute('INSERT INTO users VALUES(?, ?, ?, ?, ?, ?)', (self.get_count()+1, login, password, 'Share with world!', firstname, lastname))
        self.conn.commit()