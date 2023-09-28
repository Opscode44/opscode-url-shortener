import sqlite3

class Database:
    def __init__(self):
        self.connect = sqlite3.connect('b797079d')
        
    def create_table(self):
        self.connect.execute ('''CREATE TABLE IF NOT EXISTS urls 
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            ShortURL TEXT NOT NULL,
                            LongURL TEXT NOT NULL);''')
    
    def check_url(self, url, query):
        check = self.connect.execute(query,(url,)).fetchone()
        return check

    def insert(self, short_url, url):
        self.connect.execute("INSERT INTO urls (ShortURL, LongURL) VALUES (?,?)",(short_url,url))
        self.connect.commit()
        all_data = self.connect.execute("SELECT * FROM urls")
        for row in all_data:
           print(row)
        pass

    def get_url(self,short_url):
        url = self.connect.execute("SELECT LongURL FROM urls WHERE ShortURL = ?",(short_url,)).fetchone()
        return url