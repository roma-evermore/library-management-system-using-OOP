class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.borrow = False
    def show_info(self):
        print(f"The title of the book is : {self.title}")
        print(f"The author of the book is : {self.author}")
        print(f"The year the book was created : {self.year}")
        print(f"Status: {'Borrowed' if self.borrow else 'Available'} ")
        print()

class library:
    def __init__(self):
        self.books = [
        Book("The Hobbit", "J.R.R. Tolkien", 1937),
        Book("1984", "George Orwell", 1949),
        Book("Dune", "Frank Herbert", 1965)
        ]
    def add_book(self):
        title = str(input("Enter the title of the book you want to add: "))
        author = str(input("Enter the author of the book: "))
        year = int(input("Enter the year of the book: "))

        new_book = Book(title, author, year)

        self.books.append(new_book)

        print("The book is added!")

    def borrow_book(self):
        wanted_book = input("Enter the title of the book: ")

        for current_book in self.books:
            if current_book.title == wanted_book:
               if current_book.borrow == False:
                       current_book.borrow = True
                       print("The book is borrowed")
               else:
                       print("The book is already borrowed.")

               return
            
        print("The book is absent from the library!")
      
    def return_book(self):
        book_to_return = str(input("Enter the title of the book you want to return: "))

        for current_book in self.books:

            if current_book.title == book_to_return:
                   if current_book.borrow == True:
                      current_book.borrow = False
                      print("The book returned!")
                   else:
                      print("There is no need to return such book")
                   return
        print("The book is absent from the library!")
        
           

my_library = library()

while True:
    print("=====Library Management System=====")
    print("1. Add book ")
    print("2. Show all books ")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")
 
    
    choice = int(input("Enter the choice you want:"))

    if choice == 1:
        my_library.add_book()

    elif choice == 2:
        for book in my_library.books:
            book.show_info()

    elif choice == 3:
        my_library.borrow_book()

    elif choice == 4:
        my_library.return_book()

    elif choice == 5:
        print("So sad you are leaving... Come again!!!")
        break

    else:
        print("Enter 1-5 option! ")




