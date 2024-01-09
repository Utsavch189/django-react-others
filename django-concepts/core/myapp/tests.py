from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

class BookSaveTest(APITestCase):

    def test_booksave(self):
        _data={
            "book_name":"XYZ",
            "price":"550"
        }
        _response=self.client.post('/api/v1/myapp/savebook',data=_data,format='json')
        print(_response.status_code)
        _data=_response.json()
        print(_data)
        self.assertEqual(_response.status_code,status.HTTP_201_CREATED)
