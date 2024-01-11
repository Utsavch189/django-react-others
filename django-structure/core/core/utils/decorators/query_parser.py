import re
from django.http import HttpResponseNotFound
from rest_framework.response import Response
from datetime import datetime
from rest_framework import status

def query_parser(query_collections:list[list]=None,path=''):
    def inner(func):
        def wrapper(*args, **kwargs):
            try:
                query_string=args[1].META.get('QUERY_STRING')

                if args[1].META.get('PATH_INFO')!=path:
                    return HttpResponseNotFound("Not Found")

                elif query_string and query_collections:
                    res=re.split(r'[?&/]',query_string)
                    if res[len(res)-1]=='':
                        res.pop()
                    query_dict={key_value.split('=')[0]: key_value.split('=')[1].rstrip('/') for key_value in res}
                    if query_collections:
                        if [i.split('=')[0] for i in res] in query_collections:
                            return func(*args,query_dict)
                        return HttpResponseNotFound("Not Found")
                    return func(*args,query_dict)
                
                elif query_string and (not query_collections):
                    return HttpResponseNotFound("Not Found")

                else:
                    return func(*args,query_dict=None)
            except Exception as e:
                return Response({"message":"Internal Server Error","timestamp":datetime.timestamp(datetime.now())},status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        return wrapper
    return inner