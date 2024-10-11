class Item:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

class Book(Item):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def additional_info(self):
        print(f"Pages: {self.pages}")

class Magazine(Item):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def additional_info(self):
        print(f"Issue Number: {self.issue_number}")

if __name__ == "__main__":
    book1 = Book("Shikwa", "Allama Iqbal", 96)
    book2 = Book("Jawab-e-Shikwa", "Allama Iqbal", 120)
    magazine = Magazine("Hamara Sawaal", "Various Authors", 15)

    book1.display_info()
    book1.additional_info()

    book2.display_info()
    book2.additional_info()

    magazine.display_info()
    magazine.additional_info()
