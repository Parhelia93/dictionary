from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *


class WordList(ListView):
    model = Word
    template_name = 'dictionary/word_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WordList, self).get_context_data(**kwargs)
        context['word_details'] = [i.word for i in WordDetail.objects.filter(profile=
                                   Profile.objects.get(django_user=self.request.user))]
        return context


class DictionaryList(ListView):
    template_name = 'dictionary/dictionary_list.html'

    def get_queryset(self):
        return WordDetail.objects.filter(profile=Profile.objects.get(django_user=self.request.user))
