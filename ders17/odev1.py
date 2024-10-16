class Library:
    def __init__(self, name):
        self.__name = name
        self.__books = {}

    def add_book(self, title, copies):
        self.__books[title] = copies

    def __display_books(self):
        for title, copies in self.__books.items():
            print(f"{title}: {copies} copies are available")

    def borrow_book(self, title):
        if title in self.__books and self.__books[title] > 0:
            print(f"Borrowed '{title}'. Enjoy reading!")
            self.__books[title] -= 1
        else:
            print(f"Sorry, '{title}' is not available")

    def get_library_name(self):
        return self.__name

    def display_books(self):
        self.__display_books()


class DigitalLibrary(Library):  # Inheritance
    def __init__(self, name, physical_library):
        super().__init__(name)
        self.__ebooks = {}  # Private dictionary to store e-books and availability
        self.physical_library = physical_library  # Reference to the physical library

    def add_ebook(self, title, copies):
        self.__ebooks[title] = copies

    def borrow_book(self, title):  # Polymorphism (method overriding)
        if title in self.__ebooks and self.__ebooks[title] > 0:
            self.__ebooks[title] -= 1
            print(f"Borrowed e-book '{title}'. Enjoy reading digitally!")
        elif title in self.physical_library._Library__books and self.physical_library._Library__books[title] > 0:
            print(f"No digital version available, but '{title}' is available physically.")
        else:
            super().borrow_book(title)  # Call the parent class method if not found in e-books

    def display_all_books(self):
        print(f"\nBooks in the '{self.get_library_name()}' Library:")
        self.display_books()  # Access the public method to display physical books
        print("\nE-books:")
        for title, copies in self.__ebooks.items():
            print(f"{title}: {copies} copies available")


# Example usage
library_phisical = Library("Merkez Kütüphanesi")
library_phisical.add_book("Clean Code1", 10)

library = DigitalLibrary("City Library", library_phisical)
library.add_book("1984", 3)
library.add_book("To Kill a Mockingbird", 2)
library.add_ebook("The Art of Computer Programming", 1)
library.add_ebook("Clean Code", 5)

# Test borrowing
library.borrow_book("Clean Code1")  # Output will indicate physical availability
