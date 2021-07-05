from django.test import TestCase
from blogs.models import Blog


class BlogTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(
            title="Test Blog 1", content="Content of Test Blog 1", is_published=True
        )
        Blog.objects.create(
            title="Test Blog 2", content="Content of Test Blog 2", is_published=False
        )
