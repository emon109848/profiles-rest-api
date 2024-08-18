from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""
    def get(self, request, formate=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'emon',
            'hridoy',
            'nihon'
            ]
        
        return Response({'message':'api message', 'an_apiview': an_apiview})