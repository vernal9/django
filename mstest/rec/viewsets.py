from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import ServerValue
from .serializers import todobasicSerializer

class todobasicViewSet(viewsets.ModelViewSet):
    queryset = ServerValue.objects.all()
    serializer_class = todobasicSerializer
    permission_classes = (AllowAny,)