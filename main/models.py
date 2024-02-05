from django.db import models
from django.contrib.auth.models import User
from PIL import Image


from .exceptions import ProfileError

# Create your models here.
REACTION_CHOICES = (("like", "like"), ("dislike", "dislike"))


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_of_birth = models.DateField(null=True, blank=True)

    display_pic = models.ImageField(default="default.png", upload_to="images")
    background_pic = models.ImageField(upload_to="images", null=True, blank=True)

    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)

    bio = models.CharField(max_length=300, null=True, blank=True)

    # followers = models.ManyToManyField(
    #     "self", symmetrical=False, related_name="follower", blank=True
    # )

    # following = models.ManyToManyField(
    #     "self", symmetrical=False, related_name="follows", blank=True
    # )

    posts = models.ManyToManyField("Post", blank=True)

    @property
    def followers(self):
        return Follow.objects.filter(follow_user=self.user)

    @property
    def following(self):
        return Follow.objects.filter(user=self.user)

    @property
    def username(self):
        return self.user.username

    def __str__(self):
        return f"User('{self.username}')"

    # @property
    # def follow(self, profile_or_user):
    #     if isinstance(profile_or_user, Profile):
    #         profile = profile_or_user
    #     elif isinstance(profile_or_user, User):
    #         profile = Profile.objects.get(user=profile_or_user)
    #     else:
    #         raise ProfileError(
    #             "'Profile.follow': Expected instance of 'Profile' or 'User'"
    #             f" instead got '{type(profile_or_user)}'."
    #         )

    #     if not profile:
    #         raise ProfileError(
    #             "'Profile.follow': The specified profile or user does" " not exist."
    #         )

    #     if len(profile.followers.all().filter(user=self.user)) > 0:
    #         raise ProfileError("'Profile.follow': Already following user.")

    #     profile.followers.add(self)
    #     profile.save()

    #     return self

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        for image in [self.display_pic, self.background_pic]:
            if not image:
                continue

            img = Image.open(image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(image.path)

    @staticmethod
    def from_username(username):
        user = User.objects.get(username=username)
        if not user:
            raise ProfileError(f"No user wirh username '{username}'")
        return Profile.objects.get(user_id=user.id)

    def add_post(self, **kwargs):
        kwargs["user"] = self.user

        post = Post(**kwargs)
        post.save()

        self.posts.add(post)
        return self


class Reaction(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    # post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    reaction = models.CharField(max_length=10, choices=REACTION_CHOICES)

    def __str__(self):
        return f"Reaction('{self.reaction}', user='{self.user.username}')"


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    # post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    text = models.TextField(max_length=10000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    reactions = models.ManyToManyField(Reaction, blank=True)
    comments = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return f"Comment('{self.text}', user='{self.user.username}')"


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)

    title = models.CharField(max_length=500)
    body = models.TextField()

    viewers = models.ManyToManyField(Profile, related_name="view", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    reactions = models.ManyToManyField(Reaction, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return f"Post('{self.title}', author='{self.author.username}')"

    # @property
    # def reactions(self):
    #     return Reaction.objects.filter(post=self)

    # def react(self, user, reaction='like', unreact=True):
    #     instance = Reaction.objects.get(
    #         post=self, user=user
    #     )

    #     if instance:
    #         if unreact is True:
    #             instance.delete()
    #         elif instance.reaction != reaction:
    #             instance.reaction = reaction
    #             instance.save()
    #     else:
    #         instance = Reaction.objects.create(
    #             user=user, post=self,
    #             reaction=reaction
    #         )
    #         instance.save()


class Follow(models.Model):
    user = models.ForeignKey(
        Profile, related_name="profile",
        on_delete=models.DO_NOTHING
    )
    follow_user = models.ForeignKey(
        Profile, related_name="follow_profile",
        on_delete=models.DO_NOTHING
    )
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.user.pk == self.follow_user.pk:
            raise Exception("User can't follow them self")

        super().save(*args, **kwargs)
