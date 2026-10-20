class LibraryBook: # class define 
    libraryname= "Global Digital Library" # class attribute

    def __init__(self,title,author,ln): # Constructor & Instance Attributes
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.libraryname=ln 

    def borrow_book(self): # Instance method
        self.is_borrowed = True
        self.libraryname
        print(f"The {self.libraryname} \n book {self.title} by {self.author} has been borrowed.")

    @staticmethod # static method
    def operating_hours():  # decorator to create a method called operating_hours()
        print("Library is open daily from 9 AM to 5 PM.")

lb1 = LibraryBook("Python", "Guido van Rossum")
lb2 = LibraryBook("Java", "Joshua Bloch")

print(lb1.title)
lb1.borrow_book()
lb1.operating_hours()