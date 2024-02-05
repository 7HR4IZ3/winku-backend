from rest_framework import viewsets
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import IsAuthenticated

from rest_framework.serializers import ValidationError
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, permission_classes

from main.models import Profile, Post, Follow, Comment, Reaction
from .serializers import (
    PostSerializer,
    ProfileSerializer,
    UserSerializer,
    FollowSerializer,
    ReactionSerializer,
    CommentSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profile to be viewed or edited.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]


class FollowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profile to be viewed or edited.
    """

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ReactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profile to be viewed or edited.
    """

    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profile to be viewed or edited.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CustomAuthToken(ObtainAuthToken):
    # authentication_classes = (BasicAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "profile": ProfileSerializer(
                    Profile.objects.get_or_create(user=user)[0],
                    context={"request": request},
                ).data,
            }
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_profile(request, username=None, format=None):
    if username:
        user = User.objects.get(username=username)
    elif request.user:
        user = request.user
    else:
        user = None

    if user:
        return Response(
            {
                "profile": ProfileSerializer(
                    Profile.objects.get_or_create(user=user)[0],
                    context={"request": request},
                ).data
            }
        )

    return Response({"detail": "Unauthorized access denied."}, 401)
