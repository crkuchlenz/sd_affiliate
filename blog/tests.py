from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="john_doe")
        post = Post.objects.create(
            title = "Blog Post Dynamic",
            content = "I created this in a test",
            author = user
        )

    def test_post_title(self):
        post = Post.objects.get(title = "Blog Post Dynamic")
        expected_str = "Blog Post Dynamic"
        self.assertEqual(str(post.title), expected_str)
    
    def test_post_content(self):
        post = Post.objects.get(title = "Blog Post Dynamic")
        expected_str = "I created this in a test"
        self.assertEqual(str(post.content), expected_str)
        
    def test_post_author_username(self):
        post = Post.objects.get(title = "Blog Post Dynamic")
        expected_str = "john_doe"
        self.assertEqual(str(post.author.username), expected_str)
        
    def test_post_str(self):
        post = Post.objects.get(title = "Blog Post Dynamic")
        expected_str = "Blog Post Dynamic"
        self.assertEqual(str(post), expected_str)
