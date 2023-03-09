from django.urls import path
from .views import WordList, DictionaryList


urlpatterns = [
    path('', WordList.as_view()),
    path('my_list/', DictionaryList.as_view(), name='my_list')
]
