from api.models import Book
from api.serializers.book import BookSerializer

"""
select_related is used for ForeignKey and OneToOneField relationships to fetch related objects in a single query.
It performs a SQL JOIN to include the fields of the related object in the SELECT statement, reducing the number of queries made to the database.
"""

class BookSelector:
    
    @staticmethod
    def normal_a_book_with_its_author(book_id:str):
        """
        Executed SQL :
    
        1.  SELECT '1' AS "a"
            FROM "api_book"
            WHERE "api_book"."book_id" = '''xyz'''
            LIMIT 1

        2.  SELECT "api_book"."book_id",
                "api_book"."title",
                "api_book"."author_id",
                "api_book"."publication_date"
            FROM "api_book"
            WHERE "api_book"."book_id" = '''xyz'''
            LIMIT 21  

        3.  SELECT "api_author"."author_id",
                "api_author"."name"
            FROM "api_author"
            WHERE "api_author"."author_id" = '''c'''
            LIMIT 21  
        """

        if not Book.objects.filter(book_id=book_id).exists():
            raise Exception("book doesn't exists")
        
        book=Book.objects.get(book_id=book_id)
        book_data=BookSerializer(instance=book).data
        author=book.author
        author_data={
            "author_id":author.author_id,
            "name":author.name
        }

        return {"book":book_data,"author":author_data}
    
    @staticmethod
    def optimized_a_book_with_its_author(book_id:str):

        """
        Executed SQL :
    
        1.  SELECT '1' AS "a"
            FROM "api_book"
            WHERE "api_book"."book_id" = '''xyz'''
            LIMIT 1
        
        2.  SELECT "api_book"."book_id",
                "api_book"."title",
                "api_book"."author_id",
                "api_book"."publication_date",
                "api_author"."author_id",
                "api_author"."name"
            FROM "api_book"
            INNER JOIN "api_author"
            ON ("api_book"."author_id" = "api_author"."author_id")
            WHERE "api_book"."book_id" = '''xyz'''
            LIMIT 21
        """

        if not Book.objects.filter(book_id=book_id).exists():
            raise Exception("book doesn't exists")
        
        book=Book.objects.select_related('author').get(book_id=book_id) # here author is field name in book model
        book_data=BookSerializer(instance=book).data
        author=book.author
        author_data={
            "author_id":author.author_id,
            "name":author.name
        }

        return {"book":book_data,"author":author_data}