from django.db import models
from django.contrib.auth.models import User

class Writer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=7, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    dp = models.ImageField(blank=True)

TAGS = [
    ('politics', '#Politics'),
    ('feelings', '#Feelings'),
]

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    content = models.TextField()
    tag = models.CharField(choices=TAGS, max_length=20, default='none')
    likes = models.PositiveIntegerField(default=0)
    pub_date = models.DateField()
    mod_date = models.DateField()

    def __str__(self):
        return self.title
