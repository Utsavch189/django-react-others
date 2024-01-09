from django.db import models
from dataclasses import dataclass,field

@dataclass
class Data:
    author_name:str=field(default_factory=str)
    email:str=field(default_factory=str)
    book_name:str=field(default_factory=str)
    book_price:int=field(default_factory=int)

class AuthorRepo(models.Manager):

    def __init__(self) -> None:
        from django.db import connection
        self.conn=connection

    # Author.repo_objects().get_author_withBooks('utsavchatterjee71@gmail.com')
    def get_author_withBooks(self,author_id):
        try:
            res:list[Data]=[]
            with self.conn.cursor() as c:
                c.execute("""select a.name,a.email,b.name,b.price from django_modelManager_app_author as a Join django_modelManager_app_book as b on b.author_id=a.email where a.email=%s""",(author_id,)) # parameterized query
                for row in c.fetchall():
                    # res.append(row) or,
                    data=Data(author_name=row[0],email=row[1],book_name=row[2],book_price=row[3])
                    res.append(data)
            return res
        except Exception as e:
            raise Exception(str(e))
    
    """
    or we can override predefined methods like,

    def all(self):
        return self.filter(email='utsavchatterjee71@gmail.com')
    
    note: Here self is instance of Author Object.

    this orm should be run by Author.repo_objects().all()
    """