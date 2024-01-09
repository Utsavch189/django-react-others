from rest_framework.response import Response
from datetime import datetime

class Response(Response):

    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type=None):
        data={**data,"timestamp":datetime.timestamp(datetime.now())}
        super().__init__(data, status, template_name, headers, exception, content_type)