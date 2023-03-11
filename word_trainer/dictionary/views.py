from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *


class WordListView(ListView):
    model = Word
    template_name = 'dictionary/word_list_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WordListView, self).get_context_data(**kwargs)
        context['word_details'] = [i.word for i in WordDetail.objects.filter(profile=
                                   Profile.objects.get(django_user=self.request.user))]
        return context


class DictionaryListView(ListView):
    template_name = 'dictionary/dictionary_list_view.html'

    def get_queryset(self):
        return WordDetail.objects.filter(profile=Profile.objects.get(django_user=self.request.user))


class WordDetailView(DetailView):
    model = WordDetail
    template_name = 'dictionary/word_detail_view.html'
