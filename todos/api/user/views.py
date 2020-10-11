
from rest_framework import viewsets
from .serializers import TestSerializer
from .models import Test
# Create your views here.

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all().order_by('full_name')
    serializer_class = TestSerializer