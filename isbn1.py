import requests

def get_book_info_by_isbn(isbn):
    base_url = "https://openlibrary.org/api/books"
    params = {"bibkeys": f"ISBN:{isbn}", "format": "json", "jscmd": "data"}

    response = requests.get(base_url, params=params)
    data = response.json()

    # Проверяем, есть ли информация по данному ISBN
    if f"ISBN:{isbn}" in data:
        return data[f"ISBN:{isbn}"]
    else:
        return None

# Пример использования
isbn_to_search = "9780306406157"
book_info = get_book_info_by_isbn(isbn_to_search)

if book_info:
    print(f"Информация о книге с ISBN {isbn_to_search}:\n")
    print(f"Название: {book_info.get('title', 'Н/Д')}")
    
    # Изменения здесь: проверяем, есть ли информация об авторах
    authors = ', '.join(author.get('name', 'Н/Д') for author in book_info.get('authors', []))
    print(f"Автор(ы): {authors}")
    
    print(f"Издательство: {book_info.get('publishers', ['Н/Д'])[0]}")
    print(f"Год публикации: {book_info.get('publish_date', 'Н/Д')}")
else:
    print(f"Информация о книге с ISBN {isbn_to_search} не найдена.")
