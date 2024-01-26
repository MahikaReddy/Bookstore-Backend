import unittest
from flask import json
from flask_testing import TestCase
from app import app, db

class TestBookstoreAPI(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['JWT_SECRET_KEY'] = 'your_test_secret_key'
        return app

    def setUp(self):
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def get_auth_token(self):
        # Implement your authentication token retrieval logic here
        # For example, you might have a test user in your database
        test_user = {'username': 'test_user', 'password': 'test_password'}
        response = self.client.post('/login', json=test_user)
        return response.get_json().get('access_token')

    def test_add_book(self):
        headers = {'Authorization': 'Bearer ' + self.get_auth_token(), 'Content-Type': 'application/json'}
        book_data = {'title': 'Test Book', 'author': 'Test Author', 'isbn': '1234567890123', 'price': 19.99, 'quantity': 10}
        response = self.client.post('/books', json=book_data, headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_get_all_books(self):
        headers = {'Authorization': 'Bearer ' + self.get_auth_token(), 'Content-Type': 'application/json'}
        response = self.client.get('/books', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_book_by_isbn(self):
        headers = {'Authorization': 'Bearer ' + self.get_auth_token(), 'Content-Type': 'application/json'}
        response = self.client.get('/books/1234567890123', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_update_book(self):
        headers = {'Authorization': 'Bearer ' + self.get_auth_token(), 'Content-Type': 'application/json'}
        updated_book_data = {'title': 'Updated Book', 'author': 'Updated Author', 'price': 24.99, 'quantity': 8}
        response = self.client.put('/books/1234567890123', json=updated_book_data, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        headers = {'Authorization': 'Bearer ' + self.get_auth_token(), 'Content-Type': 'application/json'}
        response = self.client.delete('/books/1234567890123', headers=headers)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
