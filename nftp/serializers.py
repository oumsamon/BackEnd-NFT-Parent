from rest_framework import serializers
from .models import Diaper, DiaperComment, Bottle, BottleComment, BNComment, BottleNipple

class DiaperCommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = DiaperComment
        fields = ('id', 'diapername', 'newparent', 'review')

class DiaperSerializers(serializers.ModelSerializer):
    DiaperComments = DiaperCommentSerializers
    
    class Meta:
        model = Diaper
        fields = ('id', 'name', 'type', 'photo_url', 'DiaperComments')

class BottleCommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = BottleComment
        fields = ('id', 'bottlename', 'newparent', 'review')

class BottleSerializers(serializers.ModelSerializer):
    BottleComments = BottleCommentSerializers
    
    class Meta:
        model = Bottle
        fields = ('id', 'name', 'type', 'photo_url', 'BottleComments')

class BNCommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = BNComment
        fields = ('id', 'bnipplename', 'newparent', 'review')

class BottleNippleSerializers(serializers.ModelSerializer):
    BNComments = BNCommentSerializers
    
    class Meta:
        model = BottleNipple
        fields = ('id', 'name', 'flow', 'photo_url', 'BNComments')