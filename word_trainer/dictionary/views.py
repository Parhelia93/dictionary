from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from .models import *
from .services import get_word_detail_list_by_user, get_list_user_words, get_user_profile, get_user_groups
from .forms import CreateWordDetailForm, UpdateWordDetail, WordStageForm


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


# class UpdateWordDetailView(UpdateView):
#     template_name = 'dictionary/update_word_detail_view.html'
#     model = WordDetail
#     fields = ['translate', 'description', 'word_group']


def create_word_detail(request):
    template_name = 'dictionary/create_word_detail_view.html'

    if request.method == 'GET':
        return render(request, template_name, context={'form': CreateWordDetailForm(initial={'request': request})})

    if request.method == 'POST':
        word_detail_form = CreateWordDetailForm(request.POST, initial={'request': request})
        if word_detail_form.is_valid():
            word_detail = word_detail_form.save(commit=False)
            user_word, created = Word.objects.get_or_create(word=word_detail_form.cleaned_data['word_text'],
                                                            user_flag=True)
            word_detail.word = user_word
            word_detail.profile = get_user_profile(request)
            result = word_detail_form.save()
            return redirect(result)
        else:
            return render(request, template_name, context={'form': CreateWordDetailForm(request.POST, initial={'request': request})})


def update_word_detail(request, pk):
    template_name = 'dictionary/update_word_detail_view.html'
    word_detail = WordDetail.objects.get(pk=pk)
    word_stage = WordStage.objects.get(word_stage=word_detail)

    if request.method == 'GET':
        return render(request, template_name, context={'word_detail_form': UpdateWordDetail(instance=word_detail, initial={'request': request}),
                                                       'word_stage_form': WordStageForm(instance=word_stage)})

    if request.method == 'POST':
        word_detail_instance = UpdateWordDetail(request.POST, instance=word_detail, initial={'request': request})
        word_stage_instance = WordStageForm(request.POST, instance=word_stage)
        if word_detail_instance.is_valid() and word_stage_instance.is_valid():
            word_detail_instance.save()
            word_stage_instance.save()
            return redirect(word_detail)
        else:
            return render(request, template_name, context={'word_detail_form': UpdateWordDetail(request.POST,
                                                                                                instance=word_detail, initial={'request': request}),
                                                           'word_stage_form': WordStageForm(request.POST,
                                                                                            instance=word_stage, initial={'request': request})})


class GroupList(ListView):
    model = WordGroup
    template_name = 'dictionary/group_list_view.html'

    def get_queryset(self):
        return get_user_groups(self.request)
