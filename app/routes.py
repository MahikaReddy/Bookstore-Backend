# app/routes.py

from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token

from app import app, db
from app.models import Book

# Routes

# Add a new book
@app.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    data = request.get_json()

    # Validate input data
    if 'title' not in data or 'author' not in data or 'isbn' not in data or 'price' not in data or 'quantity' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    new_book = Book(
        title=data['title'],
        author=data['author'],
        isbn=data['isbn'],
        price=data['price'],
        quantity=data['quantity']
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify({'message': 'Book added successfully'}), 201

# Retrieve all books
@app.route('/books', methods=['GET'])
@jwt_required()
def get_all_books():
    books = Book.query.all()

    book_list = []
    for book in books:
        book_data = {
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'price': book.price,
            'quantity': book.quantity
        }
        book_list.append(book_data)

    return jsonify({'books': book_list})

# Retrieve a specific book by ISBN
@app.route('/books/<isbn>', methods=['GET'])
@jwt_required()
def get_book_by_isbn(isbn):
    book = Book.query.filter_by(isbn=isbn).first()

    if book:
        book_data = {
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'price': book.price,
            'quantity': book.quantity
        }
        return jsonify(book_data)
    else:
        return jsonify({'message': 'Book not found'}), 404

# Update book details
@app.route('/books/<isbn>', methods=['PUT'])
@jwt_required()
def update_book(isbn):
    book = Book.query.filter_by(isbn=isbn).first()

    if book:
        data = request.get_json()

        # Update book details
        book.title = data['title']
        book.author = data['author']
        book.price = data['price']
        book.quantity = data['quantity']

        db.session.commit()

        return jsonify({'message': 'Book updated successfully'})
    else:
        return jsonify({'message': 'Book not found'}), 404

# Delete a book
@app.route('/books/<isbn>', methods=['DELETE'])
@jwt_required()
def delete_book(isbn):
    book = Book.query.filter_by(isbn=isbn).first()

    if book:
        db.session.delete(book)
        db.session.commit()

        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'message': 'Book not found'}), 404
