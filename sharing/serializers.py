from rest_framework import serializers
from sharing.models import Sharing, Comments, LikesToSharing
# from user.serializers import UserSerializer
from user.models import User


class LikesToSharingSerializers(serializers.ModelSerializer):
    l_liker = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = LikesToSharing
        fields = ['id', 'l_shareid', 'l_liker', 'l_type']


class CommentSerializers(serializers.ModelSerializer):
    c_commenter = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Comments
        fields = ['id', 'c_shareid', 'c_commenter', 'c_comment']


class SharingSerializers(serializers.ModelSerializer):
    s_student = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    s_teacher = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    # likes_count = serializers.SerializerMethodField()
    likes_sharing = LikesToSharingSerializers(many=True, read_only=True)
    comments_sharing = CommentSerializers(many=True, read_only=True)

    class Meta:
        model = Sharing
        fields = ['id', 's_student', 's_teacher', 's_teacher_name', 's_photo', 's_appreciation', 's_video_talk',
                  's_video_dance', 's_date', 's_location', 'likes_sharing', 'comments_sharing']
