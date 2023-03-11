from django.urls import path
from .views import WordListView, DictionaryListView, WordDetailView


urlpatterns = [
    path('', WordListView.as_view()),
    path('my_list/', DictionaryListView.as_view(), name='my_list'),
    path('word_detail/<int:pk>/', WordDetailView.as_view(), name='word_detail')
]
