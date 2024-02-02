class library:
    def __init__(self,):
        self.nobooks=0
        self.books=[]

    def __add__(self, book):
        self.books.append(book)
        self.nobooks=len(self.books)

    def showinfo(self):
        print(f"No.of books are {self.nobooks} and they are {self.books}")

l=library()
l.__add__("Abra")
l.__add__("Ka")
l.__add__("Jabra")
l.showinfo()