

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return "Title: {0} \nAuthor :{1} \nPages: {2}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


print(Book("Crime and Punishment", "Fyodor Dostoevsky", 560))

