from django.db import models
from django.conf import settings


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=False, null=False)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="likes", blank=True, symmetrical=False
    )
    saves = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="saves", blank=True, symmetrical=False
    )

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title + " ({})".format(self.author.username)

    def author_pname(self):
        return self.author.username

    def no_of_likes(self):
        if self.likes.count():
            if self.likes.count() == 1:
                return self.likes.count()
            return self.likes.count()
        return 0
