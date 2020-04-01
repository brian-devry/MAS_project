from flaskblog import db


class MyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db'"
    TESTING = True

    def create_app(self):

        # pass in test configuration
        return create_app(self)

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()