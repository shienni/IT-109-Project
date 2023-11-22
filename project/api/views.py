from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required, permission_required
from .serializers import UserSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@login_required(login_url="/login")
@permission_required("__all__", login_url="/login", raise_exception=True)
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)