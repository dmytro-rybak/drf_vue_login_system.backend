import json
from rest_framework.response import Response
import requests
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.views import APIView


@authentication_classes([])
@permission_classes([])
class ActivateUser(APIView):
    def get(self, request, uid, token):
        payload = {'uid': uid, 'token': token}

        url = "http://localhost:8000/api/v1/users/activation/"
        response = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        return Response({}, response.status_code)
