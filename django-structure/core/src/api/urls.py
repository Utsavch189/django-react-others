from django.urls import path,re_path
from src.api.controller.authorCotroller import AuthorControllerApi
from src.api.controller.bookController import BookControllerApi

AUTHOR_URL='^author(?:\?author-id=[a-zA-Z0-9_-]+(?:\?page=[a-zA-Z0-9_-]&page-size=[a-zA-Z0-9_-]))?' 
"""
Possibilites : 

author/
author?author-id=xEir2yi48MSFEgGRjhiGpT5-FdeBk8viFih_u/
author?author-id=b6fyJ6LRNdYBo7tQIEDEjlTGev6jkYDB7BesvRyKR-um8n7/
author/
author/
author/
author?author-id=ANbkhaHXVBzxLBXqH66teh3C0YLVPMnD4U6xyOl6C3C_jT2Bp9FyFa_VQDVdibB9zK66-qLstDxHbJfbVI4iS3GR1KYvmCc7/
author/
author?author-id=U/
author?author-id=x3vVjxw/

"""

AUTHOR_URL2='^author(?:\?author-id=[a-zA-Z0-9_-]+(?:&author-name=[a-zA-Z0-9_-]+)?)?\/$'
"""
Possibilites : 

author?author-id=8rpHhUaT9mLQGBxCu_T2wohwgI0vJfhsKgwAlCBkp6Etc/
author/
author?author-id=qmRtP7NQmUP6qvFGUB5R7uZ768lzC3iJAILg7AgHykIMVKFiz2OnWM0NyXhoIfnlOC7NcKi&author-name=kMERBnkXihYx2TeSVqvOHHSjHuaWKef9-HRyUlp8iXA5/
author/
author/
author?author-id=Bhz-O675gUVih56fjGJBtOjxQjXb7dmGjOuKuPSZ1PyUu4_1vxpJdvV9CR&author-name=btmy587WrVSDQf_PRhVKjcRixry/
author/
author?author-id=JIC-UxLV6sMyZdbGrUUB4SRLcasW3cw4RHqQVCkKx0WK77HtQp_-Q5T2NsVUhk8G-0CS9Is73LxHRP&author-name=FmQijWAgHrgjpVeys5JyBzjgIO65F348C4_r263UuM/
author/
author/
"""

BOOK_URL='^book(?:\?book-id=[a-zA-Z0-9_-]+(?:\?page=[a-zA-Z0-9_-]&page-size=[a-zA-Z0-9_-]))?'

urlpatterns = [
    re_path(rf'{AUTHOR_URL}',AuthorControllerApi.as_view()),
    re_path(rf'{BOOK_URL}',BookControllerApi.as_view())
]
