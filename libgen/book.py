import json


class Book:

    def __init__(self, title, author, year, language, imageurl, bookurl):
        self.title = title
        self.author = author
        self.year = year
        self.language = language
        self.imageurl = imageurl
        self.bookurl = bookurl

    def toJSON(self):
        json_object = {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'language': self.language,
            'imageurl': self.imageurl,
            'bookurl': self.bookurl
        }
        return json_object
