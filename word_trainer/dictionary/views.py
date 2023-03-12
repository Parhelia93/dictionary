from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import *
from .services import get_word_detail_list_by_user, get_list_user_words


class WordListView(ListView):
    model = Word
    template_name = 'dictionary/word_list_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WordListView, self).get_context_data(**kwargs)
        context['word_details'] = get_list_user_words(self.request)
        return context


class DictionaryListView(ListView):
    template_name = 'dictionary/dictionary_list_view.html'

    def get_queryset(self):
        return get_word_detail_list_by_user(self.request)


class WordDetailView(DetailView):
    model = WordDetail
    template_name = 'dictionary/word_detail_view.html'


class UpdateWordDetailView(UpdateView):
    template_name = 'dictionary/update_word_detail_view.html'
    model = WordDetail
    fields = ['translate', 'description', 'word_group']


