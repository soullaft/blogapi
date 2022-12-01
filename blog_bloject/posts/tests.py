from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        testUser1 = User.objects.create_user(username='testuser1', password='abc123')
        testUser1.save()

        testPost = Post.objects.create(author=testUser1, title='Blog title', body='Blog body')
        testPost.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEquals(author, 'testuser1')
        self.assertEquals(title, 'Blog title')
        self.assertEquals(body, 'Blog body')
        