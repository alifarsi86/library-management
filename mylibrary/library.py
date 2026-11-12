class library():
    def __init__(self):
        self.books=[]

    def add_book(self,title,author):
        book={
            "title":title,
            "author":author
        }
        self.books.append(book)

    def remove_book(self,title):
        found=False
        for book in self.books:
            if book["title"]==title:
                self.books.remove(book)
                found=True
                break
        if not found:
            print('book not found')

    def search_book (self,title):
        found=False
        for book in self.books:
            if book["title"]==title:
                print('title:',book["title"])
                print('author:',book["author"])
                found=True
                break
        if not found:
            print('book not found')
    def show_book(self):
            if self.books==[]:
                print('no available book')
            else:
                for book in self.books:
                    print(book["title"],' - ', book["author"])

