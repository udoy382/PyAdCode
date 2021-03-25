class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" * " + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe it with in 30 days!")
            self.books.remove(bookName)
        else:
            print("Sorry! This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returing this book! Hope you enjoyed reding it. Have a great day ahead!")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow!")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__ == '__main__':
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()

    while(True):
        welcomeMsg = '''
        ***Welcome to Central Library***
        __Plese chose an option__
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.returnBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Centra library! have a great day ahed")
            exit()
        else:
            print("Invalid Choice!")