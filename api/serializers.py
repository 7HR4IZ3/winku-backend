from django.contrib.auth.models import User
from main.models import Post, Reaction, Profile, Follow, Comment
from rest_framework.serializers import HyperlinkedModelSerializer


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class ReactionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Reaction
        fields = "__all__"



class ProfileSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    # posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


class CommentSerializer(HyperlinkedModelSerializer):
    user = ProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(HyperlinkedModelSerializer):
    author = ProfileSerializer(read_only=True)
    # viewers = UserSerializer(many=True, read_only=True)
    reactions = ReactionSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class FollowSerializer(HyperlinkedModelSerializer):
    user = ProfileSerializer(read_only=True)
    follow_user = ProfileSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = "__all__"
