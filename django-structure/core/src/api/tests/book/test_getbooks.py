from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status


"""
RUN Test : py .\manage.py test  src.api.tests.book.test_getbooks

# pip install coverage

Run Coverage : coverage run --source='src.api' manage.py test src.api.tests.book.test_getbooks --> will generate .coverage file
Coverage Report : coverage report --> show report
Coverage html : coverage html --> show report in html

** .coveragerc file decides which file or folders should not be considered during tests
"""



ACCESS_TOKEN="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDU1MDM2NjUuNjMxNDA3LCJleHAiOjE3MDU1MDQyNjUuNjMxNDA3LCJ1c2VyIjoidXRzMTIzIn0.zCxyu5b37n_b8MmFMsPwtPoCknbyDuNnfrx5HOsy5b-XIF0hrn6f-YnqTc3Yi7FicShdNTgGUIocWbrGwTGhXQ"

class TestGetAllBooks(APITestCase):
    
    endpoint="/api/v1/book"

    def test_getBooks_withoutToken(self):
        resp=self.client.get(self.endpoint)
        self.assertEqual(resp.status_code,status.HTTP_401_UNAUTHORIZED)
    
    def test_getBooks_withToken(self):
        headers={
            "Authorization":f'Bearer {ACCESS_TOKEN}'
        }
        resp=self.client.get(self.endpoint,headers=headers)
        data=resp.json()
        data.pop('timestamp')
        expected_data={
            "books":[]
        }

        self.assertDictEqual(d1=data,d2=expected_data)
        self.assertEqual(resp.status_code,status.HTTP_200_OK)

class TestPaginatedBooks:
    pass

class TestGetBookById:
    pass