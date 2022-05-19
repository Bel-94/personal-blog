from app.models import Blog, User, Comment
from app import db
def setUp(self):
        self.client = User(username = 'John Doe',password = 'codes', email = 'user@gmail.com')
        self.new_blog = Blog(id=1, title='Lets Talk Luxury Lifestyle', post='If you want Luxuries, come to Dubai' )
        self.new_comment = Comment(comment = "Awesome", post_id = self.new_blog.id, user_id = self.client.id)

def test_instance(self):
        self.assertTrue(isinstance(self.user_Moh, User))
        self.assertTrue(isinstance(self.new_blog, Blog))
        self.assertTrue(isinstance(self.new_comment, Comment))