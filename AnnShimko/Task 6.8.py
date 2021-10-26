# Task 4.8

#Implement a Pagination class helpful to arrange text on pages and list content on given page.
#The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page
# (take spaces into account as well).
#You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that
# accepts the page number and return quantity of symbols on this page.
#If the provided number of the page is missing print the warning message "Invalid index. Page is missing".
# If you're familliar with using of Excpetions in Python display the error message in this way.
#Pages indexing starts with 0.

#Example:
#>>> pages = Pagination('Your beautiful text', 5)
#>>> pages.page_count
#4
#>>> pages.item_count
#19
#>>> pages.count_items_on_page(0)
#5
#>>> pages.count_items_on_page(3)
#4
#>>> pages.count_items_on_page(4)
#Exception: Invalid index. Page is missing.

class Pagination:
    def __init__(self, text, number):
        self.text = text
        self.number = number

    def pages_count(self):
        return -(-len(self.text)//self.number)

    def pages_book(self):
        book = {}
        for page in range(0, self.pages_count()):
            book[page] = self.text[self.number * (page): self.number * (page + 1)]
        return book

    def item_count(self, page_number):
        try:
            len(self.pages_book()[page_number])
            #0 >= page_number > self.pages_count()
        except KeyError:
            return f'"{page_number}" - Invalid index. Page is missing'
        return len(self.pages_book()[page_number])

    def search(self, element):
        page_list = []
        book = self.pages_book()
        for key, value in book.items():
            if element in value:
                page_list.append(key)
        return page_list


pages = Pagination('qwert qwert qeert qwert', 5)
print(pages.pages_count())
print(pages.pages_book())
print(pages.item_count(4))
print(pages.item_count(10))
print(pages.search('qw'))
