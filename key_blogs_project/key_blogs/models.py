from django.db import models
from django.contrib.auth.models import User

class Writer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=7, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    dp = models.ImageField(blank=True, upload_to='key_blogs/dp/', default='key_blogs/dp/writer.png')

TAGS = [
    ('travel', '#travel'),
    ('health', '#health'),
    ('elearning', '#e-learning'),
    ('tech', '#technology'),
    ('gaming', '#gaming'),
    ('parenting', '#parenting'),
    ('food', '#food'),
    ('criticism', '#criticism')
]

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    content = models.TextField()
    tag = models.CharField(choices=TAGS, max_length=20, default='none')
    pub_date = models.DateField()
    mod_date = models.DateField()

    def __str__(self):
        return self.title

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    ofblog = models.ForeignKey(Blog, on_delete=models.CASCADE)
