from app.models import Comment, User
from app import db
def setUp(self):
        self.client = User(username = 'Belinda',password = '1234', email = 'user@gmail.com')
        