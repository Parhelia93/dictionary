from django import forms
from .models import WordDetail, WordStage, Word


class CreateWordDetailForm(forms.ModelForm):
    word_text = forms.CharField(max_length=10)

    class Meta:
        model = WordDetail
        fields = ['word_text', 'translate', 'description', 'word_group']


class UpdateWordDetail(forms.ModelForm):
    class Meta:
        model = WordDetail
        fields = ['translate', 'description', 'word_group']


class WordStageForm(forms.ModelForm):
    class Meta:
        model = WordStage
        fields = ['name']