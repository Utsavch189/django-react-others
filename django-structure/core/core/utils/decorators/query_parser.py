from django.http import HttpResponseNotFound

def query_parser(query_collections:list[list]=None,path=''):
    def inner(func):
        def wrapper(*args, **kwargs):
            try:
                if args[1].META.get('PATH_INFO')!=path:
                    return HttpResponseNotFound("Not Found")

                elif args[1].query_params and query_collections:
                    query_params_list=[i for i in args[1].query_params]
                    funcs=lambda x : True if query_params_list==x else False
                    res=map(funcs,query_collections)

                    for i in res:
                        if i:
                            return func(*args, **kwargs)
                    return HttpResponseNotFound("Not Found")
                
                elif args[1].query_params and (not query_collections):
                    return HttpResponseNotFound("Not Found")

                else:
                    return func(*args, **kwargs)
            except Exception as e:
                return Exception("Internal Server Error!") 
        return wrapper
    return inner