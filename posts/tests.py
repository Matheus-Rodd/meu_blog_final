from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is a test post content.')

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')