

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)  

# Expected output: "Nineteen Eighty-Four by George Orwell (1949)"
