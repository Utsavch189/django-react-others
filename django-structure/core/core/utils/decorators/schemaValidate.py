from rest_framework.response import Response
from datetime import datetime
from rest_framework import status
from utils.schema_validation.validation import SchemaValidate

def schema_validate(schema_name:str):
    def inner(func):
        def wrapper(*args, **kwargs):
            try:
                validation=SchemaValidate(request_data=args[1].data,json_file=schema_name)
                is_valid=validation.validate()    
                if is_valid:    
                    return func(*args, **kwargs)
                else:
                    return Response({"message":"requested schema is not correct","timestamp":datetime.timestamp(datetime.now())},status=status.HTTP_422_UNPROCESSABLE_ENTITY) 
            except Exception as e:
                return Response({"message":"Internal Server Error","timestamp":datetime.timestamp(datetime.now())},status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        return wrapper
    return inner