from rest_framework import generics
from .serializers import DiaperSerializers, DiaperCommentSerializers
from .models import Diaper, DiaperComment

# Create your views here.

class DiaperList(generics.ListCreateAPIView):
    queryset = Diaper.objects.all()
    serializer_class = DiaperSerializers

class DiaperCommentList(generics.ListCreateAPIView):
    queryset = DiaperComment.objects.all()
    serializer_class = DiaperCommentSerializers