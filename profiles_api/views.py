from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'User HTTP methods as function (get, post, put, delete)',
            'Hello world!',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})