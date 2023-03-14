from django import forms
from .models import WordDetail, WordStage, Word
from .services import get_user_groups


class CreateWordDetailForm(forms.ModelForm):
    word_text = forms.CharField(max_length=10)

    class Meta:
        model = WordDetail
        fields = ['word_text', 'translate', 'description', 'word_group']

    def __init__(self, *args, **kwargs):
        super(CreateWordDetailForm, self).__init__(*args, **kwargs)
        self.request = kwargs['initial']['request']
        self.fields['word_group'].queryset = get_user_groups(self.request)


class UpdateWordDetail(forms.ModelForm):
    class Meta:
        model = WordDetail
        fields = ['translate', 'description', 'word_group']

    def __init__(self, *args, **kwargs):
        super(UpdateWordDetail, self).__init__(*args, **kwargs)
        self.request = kwargs['initial']['request']
        self.fields['word_group'].queryset = get_user_groups(self.request)


class WordStageForm(forms.ModelForm):
    class Meta:
        model = WordStage
        fields = ['name']