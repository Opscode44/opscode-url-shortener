from database import Database
import string
import random

class Shortener:
    def __init__(self):
        pass

    def shorten(self, url):
        db = Database()
        db.create_table()
        check = db.check_url(url, "SELECT ShortURL FROM urls WHERE LongURL = ?")
        if check is not None:
            print("I got here", check[0])
            return check[0]
        else:
            def insert():
                gen_url = self.generate_short_url()
                #check if generated short url exist in the Database
                short_url_check = db.check_url(gen_url, "SELECT count(*) FROM urls WHERE ShortURL = ?")
                if short_url_check[0] > 0:
                    insert()
                else:
                    db.insert(gen_url, url)
                return gen_url
            short_url = insert()
            return short_url

    def generate_short_url(self):
        num = string.digits
        alph_upp = string.ascii_uppercase
        alph_low = string.ascii_lowercase
        short_url = ''.join(random.choices(num + alph_low + alph_upp, k=7))
        return short_url

    def get_url(self, short_url):
        db = Database()
        url = db.get_url(short_url)
        return url
