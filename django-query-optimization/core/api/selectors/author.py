from api.models import Author
from api.serializers.author import AuthorSerializer

"""
prefetch_related:

prefetch_related is used to optimize queries when dealing with many-to-many and reverse ForeignKey/OneToOneField relationships.
It performs a separate lookup for each relationship, retrieves the related objects, and does the "joining" in Python.
This can be more efficient than select_related in scenarios where a large number of related objects need to be fetched, as it avoids the issues of Cartesian products that might occur with multiple joins.
"""

class AuthorSelector:
    
    @staticmethod
    def normal_getall_author():
        """
        For each author, it triggers an additional query to fetch their books. 
        As a result, if you have N authors, you end up making N+1 queries 
        (1 query to fetch authors and N queries to fetch books for each author), 
        which can lead to performance issues, especially with a large number of authors.

        So 1 extra query for get all author [SELECT "api_author"."author_id",
                                                        "api_author"."name"
                                            FROM "api_author"]

        Then n queries to fetch all of author's corresponding books.[
                                                                        SELECT "api_book"."book_id",
                                                                            "api_book"."title",
                                                                            "api_book"."author_id",
                                                                            "api_book"."publication_date"
                                                                        FROM "api_book"
                                                                        WHERE "api_book"."author_id" = '''a'''

         
                                                                        SELECT "api_book"."book_id",
                                                                               "api_book"."title",
                                                                               "api_book"."author_id",
                                                                               "api_book"."publication_date"
                                                                          FROM "api_book"
                                                                         WHERE "api_book"."author_id" = '''b'''

                                                                         
                                                                        SELECT "api_book"."book_id",
                                                                               "api_book"."title",
                                                                               "api_book"."author_id",
                                                                               "api_book"."publication_date"
                                                                          FROM "api_book"
                                                                         WHERE "api_book"."author_id" = '''c'''

                                                                    ]
        (n+1) problem...
        """
        authors=Author.objects.all()
        return AuthorSerializer(instance=authors,many=True).data
    
    @staticmethod
    def optimized_getall_author():
        """
            Executed SQL:
            
            1.  SELECT "api_author"."author_id",
                "api_author"."name"
                FROM "api_author"

            2.  SELECT "api_book"."book_id",
                "api_book"."title",
                "api_book"."author_id",
                "api_book"."publication_date"
                FROM "api_book"
                WHERE "api_book"."author_id" IN ('''a''', '''b''', '''c''')

            By using prefetch_related('book_set'), we fetch all authors and their associated books in a single query.
        
        """
        authors=Author.objects.prefetch_related('book_set').all()
        return AuthorSerializer(instance=authors,many=True).data
    
    @staticmethod
    def normal_geta_author(author_id:str):

        """
            Executed SQL:

            1.  SELECT '1' AS "a"
                FROM "api_author"
                WHERE "api_author"."author_id" = '''a'''
                LIMIT 1
            
            2.  SELECT "api_author"."author_id",
                "api_author"."name"
                FROM "api_author"
                WHERE "api_author"."author_id" = '''a'''
                LIMIT 21

            3.  SELECT "api_book"."book_id",
                "api_book"."title",
                "api_book"."author_id",
                "api_book"."publication_date"
                FROM "api_book"
                WHERE "api_book"."author_id" = '''a'''
        """

        if not Author.objects.filter(author_id=author_id).exists():
            raise Exception("author doesn't exists!")
        
        author=Author.objects.get(author_id=author_id)
        return AuthorSerializer(instance=author).data
    
    @staticmethod
    def optimized_geta_author(author_id:str):
        """
            Executed SQL:
            
            1.  SELECT "api_author"."author_id",
                "api_author"."name"
                FROM "api_author"
                WHERE "api_author"."author_id" = '''a'''
                LIMIT 21

            2.  SELECT "api_book"."book_id",
                "api_book"."title",
                "api_book"."author_id",
                "api_book"."publication_date"
                FROM "api_book"
                WHERE "api_book"."author_id" = '''a'''
        """
        if not Author.objects.filter(author_id=author_id).exists():
            raise Exception("author doesn't exists!")

        author=Author.objects.prefetch_related('book_set').get(author_id=author_id) # book_set here is related_name on Book model
        return AuthorSerializer(instance=author).data
    