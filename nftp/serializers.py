from rest_framework import serializers
from .models import Diaper, DiaperComment

class DiaperCommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = DiaperComment
        fields = ('id', 'diapername', 'newparent', 'review')

class DiaperSerializers(serializers.ModelSerializer):
    DiaperComments = DiaperCommentSerializers
    
    class Meta:
        model = Diaper
        fields = ('id', 'name', 'photo_url', 'DiaperComments')
