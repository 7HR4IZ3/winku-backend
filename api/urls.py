from django.urls import include, path
from django.views import static
from django.conf import settings
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r"profile", views.ProfileViewSet)
router.register(r"posts", views.PostViewSet)
router.register(r"users", views.UserViewSet)
router.register(r"follow", views.FollowViewSet)
router.register(r"reaction", views.ReactionViewSet)
router.register(r"comments", views.CommentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/user_profile", views.get_profile),
    path("api/user_profile/<username>", views.get_profile),
    path("api/", include(router.urls)),
    path("auth/api-token", views.CustomAuthToken.as_view()),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("media/<path:path>", static.serve, {"document_root": "media"}),
]
