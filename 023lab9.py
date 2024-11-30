import csv

class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Book(Document):
    def __init__(self, title, author, genre="", pages=0):
        super().__init__(title, author)
        self.genre = genre
        self.pages = pages

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")
        print(f"Pages: {self.pages}")

class Article(Document):
    def __init__(self, title, author, journal="", doi=""):
        super().__init__(title, author)
        self.journal = journal
        self.doi = doi

    def display_info(self):
        super().display_info()
        print(f"Journal: {self.journal}")
        print(f"DOI: {self.doi}")

def save_documents_to_csv(documents, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['type', 'title', 'author', 'genre', 'pages', 'journal', 'doi']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for document in documents:
            if isinstance(document, Book):
                writer.writerow({'type': 'Book', 'title': document.title, 'author': document.author, 'genre': document.genre, 'pages': document.pages, 'journal': '', 'doi': ''})
            elif isinstance(document, Article):
                writer.writerow({'type': 'Article', 'title': document.title, 'author': document.author, 'genre': '', 'pages': '', 'journal': document.journal, 'doi': document.doi})

def read_documents_from_csv(filename):
    documents = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['type'] == 'Book':
                document = Book(row['title'], row['author'], row['genre'], int(row['pages']))
            elif row['type'] == 'Article':
                document = Article(row['title'], row['author'], row['journal'], row['doi'])
            documents.append(document)
    return documents

if __name__ == "__main__":
    documents = read_documents_from_csv("documents.csv")

    # Add new documents
    book1 = Book("Bang e Dara", "Allama Iqbal", 1924)
    article1 = Article("A Study on Quantum Computing", "Alice Johnson", "Nature", "10.1038/s41586-023-06203-w")
    documents.extend([book1, article1])

    # Display document information
    for document in documents:
        document.display_info()
        print()

    # Save updated document information
    save_documents_to_csv(documents, "documents.csv")