# Library Management System

class Library:

    def __init__(self):
        
        self.listBook = []
        

    def add(self , name):
        self.listBook.append(name)
        
    def listBooks(self):
        print(f"The Library has {len(self.listBook)} and they are : ")
        for book in self.listBook:
            print(book)

book1 = Library()
book1.add("Ikigai")
book1.add("Karnali Blues")
book1.add("Summer Love")
book1.add("The Psychology of Money")

book1.listBooks()


        



