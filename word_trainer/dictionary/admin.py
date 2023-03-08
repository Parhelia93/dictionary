from django.contrib import admin
from .models import Profile, Word, WordDetail, WordStage, WordStatistic

admin.site.register(Profile)
admin.site.register(Word)
admin.site.register(WordDetail)
admin.site.register(WordStage)
admin.site.register(WordStatistic)
