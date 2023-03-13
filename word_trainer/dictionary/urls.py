from django.urls import path
from .views import WordListView, DictionaryListView, WordDetailView, create_word_detail, update_word_detail


urlpatterns = [
    path('', WordListView.as_view()),
    path('my_list/', DictionaryListView.as_view(), name='my_list'),
    path('word_detail/<int:pk>/', WordDetailView.as_view(), name='word_detail'),
    path('update_word_detail/<int:pk>', update_word_detail, name='update_word_detail'),
    path('create_word_detail/', create_word_detail, name='create_word_detail')
]
