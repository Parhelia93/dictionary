from django.http import HttpRequest
from .models import Profile, WordDetail, WordGroup


def get_user_profile(request):
    return Profile.objects.get(django_user=request.user)


def get_word_detail_list_by_user(request):
    profile = get_user_profile(request=request)
    return WordDetail.objects.filter(profile=profile)


def get_list_user_words(request):
    return [i.word for i in get_word_detail_list_by_user(request)]


def get_user_groups(request):
    profile = get_user_profile(request=request)
    return WordGroup.objects.filter(profile=profile)
