from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_query_param = "sahifa"
    def get_paginated_response(self, data):
        return Response(data={
            "sahifalar":{
                "oldingi" : self.get_previous_link(),
                "Keyingi" : self.get_next_link()
            },
            "soni" : self.page.paginator.count,
            "natijalar" : data
        })
    