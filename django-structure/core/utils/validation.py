import json,jsonschema
from django.conf import settings

class SchemaValidate:

    def __init__(self,request_data:dict,json_file:str) -> None:
        self.request_data=request_data
        self.json_file=json_file
    
    def __get_schema(self):
        try:
            with open(f'{settings.BASE_DIR}/utils/schemas/{self.json_file}', 'r') as file:
                schema = json.load(file)
            return schema
        except Exception as e:
            raise Exception(str(e))
    
    def validate(self)->bool:
        try:
            execute_api_schema = self.__get_schema()
            try:
                jsonschema.validate(instance=self.request_data, schema=execute_api_schema)
            except jsonschema.exceptions.ValidationError as err:
                return False
            except Exception as e:
                return False
    
            return True
        except Exception as e:
            raise Exception(str(e))