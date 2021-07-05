from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from blogs.models import Blog


class WriterManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not name:
            raise ValueError("Users must provide a name.")
        if not email:
            raise ValueError("Users must provide an email id")
        user = self.model(
            name=name.capitalize(),
            email=self.normalize_email(email),
            username=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        print("User created successfully.")
        return user

    def create_superuser(self, name, email, password=None):
        user = self.create_user(name=name, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Writer(AbstractUser):
    name = models.CharField("Name", max_length=100)
    email = models.EmailField("Email", max_length=100, unique=True)
    username = models.CharField("Pen Name", max_length=100, unique=True)
    bio = models.TextField("Bio", blank=True)
    dp = models.ImageField(
        "Profile Picture", upload_to="app/", default="app/writer.png"
    )
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="Follower", blank=True, symmetrical=False
    )
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="Following",
        blank=True,
        symmetrical=False,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = WriterManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        verbose_name = "Writer"
        verbose_name_plural = "Writers"

    def __str__(self):
        return self.email

    def no_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        return 0

    def no_of_following(self):
        if self.following.count():
            return self.following.count()
        return 0

    def no_of_blogs(self):
        return self.blog_set.count()

    def pub_blogs(self):
        return self.blog_set.filter(is_published=True)

    def arch_blogs(self):
        return self.blog_set.filter(is_published=False)

    def saved_blogs(self):
        return Blog.objects.filter(saves__id=self.pk)
