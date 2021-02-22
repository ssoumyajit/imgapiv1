from django.db import models

from django.db import models
from django.conf import settings
from user.models import User
from django_countries.fields import CountryField
import time
import datetime
import uuid


class Sharing(models.Model):
    s_student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student")
    s_teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="teacher", null=True,
                                  blank=True)
    s_teacher_name = models.CharField(default="", max_length=255)
    s_teacher_country = CountryField()
    s_photo = models.ImageField(default="", upload_to="sharing/")
    s_appreciation = models.CharField(max_length=160, default="")  # 1 line = 8 words, 20 lines to cover up the image
    s_video_talk = models.FileField(default="", upload_to="talk/")
    s_video_dance = models.FileField(default="", upload_to="dance/")
    s_date = models.DateField(auto_now=True)  # keeping track of the user's posting time.
    s_location = models.CharField(max_length=30)

    # voters_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "votes")

    class Meta:
        ordering = ['s_date']


class LikesToSharing(models.Model):
    LOVE = 'LO'
    DOPE = 'DO'
    INSPIRING = 'IS'
    RESPECT = 'RS'
    CUTE = 'CT'
    INFORMATIVE = 'IF'
    EMOTIONAL = 'EM'

    HOW_YOU_LIKE_IT_CHOICES = [
        (LOVE, 'love'),
        (DOPE, 'dope'),
        (INSPIRING, 'inspiring'),
        (RESPECT, 'respect'),
        (CUTE, 'cute'),
        (INFORMATIVE, 'informative'),
        (EMOTIONAL, 'emotional'),
    ]

    l_shareid = models.ForeignKey('Sharing', on_delete=models.CASCADE, related_name="likes_sharing")
    l_liker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    l_type = models.CharField(
        max_length=2,
        choices=HOW_YOU_LIKE_IT_CHOICES,
        default=LOVE
    )


class Comments(models.Model):
    c_shareid = models.ForeignKey('Sharing', on_delete=models.CASCADE, related_name="comments_sharing")
    c_commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    c_comment = models.CharField(max_length=255)  # add a validation here.
    # may be here just a like option embedded directly, no types of like.