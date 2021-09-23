from django.contrib import admin
from .models import Diaper, Bottle, BottleNipple, DiaperComment, BottleComment, BNComment

# Register your models here.
admin.site.register(Diaper)
admin.site.register(Bottle)
admin.site.register(BottleNipple)
admin.site.register(DiaperComment)
admin.site.register(BottleComment)
admin.site.register(BNComment)