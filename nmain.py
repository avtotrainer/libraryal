from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', genre='{self.genre}')>"

# Создаем движок для базы данных (в данном случае SQLite)
engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)

# Создаем сессию для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Операции CRUD (Create, Read, Update, Delete) через ORM

def add_book(title, author, genre):
    book = Book(title=title, author=author, genre=genre)
    session.add(book)
    session.commit()

def remove_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()

def search_books(title=None, author=None, genre=None):
    query = session.query(Book)
    if title:
        query = query.filter_by(title=title)
    if author:
        query = query.filter_by(author=author)
    if genre:
        query = query.filter_by(genre=genre)

    return query.all()

# Пример использования функций
add_book('The Catcher in the Rye', 'J.D. Salinger', 'Fiction')
add_book('To Kill a Mockingbird', 'Harper Lee', 'Classics')

# Используйте repr() для представления результатов запроса
result = search_books(author='J.D. Salinger')
print(result)

session.close()