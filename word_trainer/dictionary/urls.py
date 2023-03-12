from django.urls import path
from .views import WordListView, DictionaryListView, WordDetailView, UpdateWordDetailView


urlpatterns = [
    path('', WordListView.as_view()),
    path('my_list/', DictionaryListView.as_view(), name='my_list'),
    path('word_detail/<int:pk>/', WordDetailView.as_view(), name='word_detail'),
    path('update_word_detail/<int:pk>', UpdateWordDetailView.as_view(), name='update_word_detail')
]
