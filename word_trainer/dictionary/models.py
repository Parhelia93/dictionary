from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    telegram_id = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(blank=True)
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    repeat_timeout = models.IntegerField(default=30)

    def __str__(self):
        return str(self.django_user)


class Word(models.Model):
    word = models.CharField(max_length=25, unique=True, primary_key=True)
    audio_ref = models.CharField(max_length=25, blank=True)
    user_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.word


class WordGroup(models.Model):
    name = models.CharField(max_length=25)
    add_date = models.DateTimeField(auto_now_add=True)
    enable_training = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class WordDetail(models.Model):
    translate = models.CharField(max_length=25)
    description = models.TextField(max_length=50, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    word_group = models.ManyToManyField(WordGroup)

    def __str__(self):
        return f'{self.translate} - {self.profile}'


class WordStage(models.Model):
    STAGE_NEW = 'New'
    STAGE_KNOW = 'Know'
    STAGE_REPEAT = 'Repeat'
    STAGE_NAMES = [
        (STAGE_NEW, 'New'),
        (STAGE_KNOW, 'Know'),
        (STAGE_REPEAT, 'Repeat')
    ]

    name = models.CharField(max_length=10, choices=STAGE_NAMES, default=STAGE_NEW)
    changed_date = models.DateTimeField(auto_now=True)
    word_stage = models.OneToOneField(WordDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WordStatistic(models.Model):
    answer = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    word_detail = models.ForeignKey(WordDetail, on_delete=models.CASCADE)
