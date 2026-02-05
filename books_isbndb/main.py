import requests as req
import json
 
h = {'Authorization': '66925_973fa38047a6bab401a7ee6c083ac6ad'}
resp = req.get("https://api2.isbndb.com/subject/Baby", headers=h)

if resp.status_code == 200:
  data = resp.json()
  #if data doesnt exist pass an empty list
  books_data = data.get("books", []);

  filter_books = []
  for book in books_data:
      filter_books.append({
          "title": book.get("title"),
          "image": book.get("image"),
          "authors": book.get("authors")
      })
  #Save it in JSON create a JSON or overwrite it 
  with open("books_children.json", "w", encoding="utf-8") as f:
      #to convert an object in Python to JSON, indecent=4 is for a nice view of JSON noy only line
      json.dump(filter_books, f, ensure_ascii=False, indent=4)
  #without filter
  with open("books_no_filter.json", "w", encoding="utf-8") as f:
      #to convert an object in Python to JSON, indecent=4 is for a nice view of JSON noy only line
      json.dump(books_data, f, ensure_ascii=False, indent=4)
  print("JSON created and saved.")
  print("Books: ", len(books_data))

else:
    print("Error:", resp.status_code, resp.text)