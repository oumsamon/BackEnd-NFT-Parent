from rest_framework import generics
from .serializers import DiaperSerializers, DiaperCommentSerializers, BottleSerializers, BottleCommentSerializers, BottleNippleSerializers, BNCommentSerializers
from .models import Diaper, DiaperComment, Bottle, BottleComment, BNComment, BottleNipple

# Create your views here.

class DiaperList(generics.ListCreateAPIView):
    queryset = Diaper.objects.all()
    serializer_class = DiaperSerializers

class DiaperCommentList(generics.ListCreateAPIView):
    queryset = DiaperComment.objects.all()
    serializer_class = DiaperCommentSerializers

class DiaperCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiaperComment.objects.all()
    serializer_class = DiaperCommentSerializers

class BottleList(generics.ListCreateAPIView):
    queryset = Bottle.objects.all()
    serializer_class = BottleSerializers

class BottleCommentList(generics.ListCreateAPIView):
    queryset = BottleComment.objects.all()
    serializer_class = BottleCommentSerializers

class BottleCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BottleComment.objects.all()
    serializer_class = BottleCommentSerializers


class BNCommentList(generics.ListCreateAPIView):
    queryset = BNComment.objects.all()
    serializer_class = BNCommentSerializers

class BNCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BNComment.objects.all()
    serializer_class = BNCommentSerializers

class BNList(generics.ListCreateAPIView):
    queryset = BottleNipple.objects.all()
    serializer_class = BottleNippleSerializers

class BNListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BottleNipple.objects.all()
    serializer_class = BottleNippleSerializers