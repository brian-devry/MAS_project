from flaskblog import app
import flaskblog.forms as form
import flaskblog.models as model
import flaskblog.routes as route
import unittest

class FlaskBlogTests(unittest.TestCase):
 #test if registeration form works correctly 
 def test_register(self):
     tester = app.test_client(self)
     response = tester.post(
         '/register',
         data=dict(form.RegistrationForm()),
         follow_redirects=True
     )
     self.assertIn(b'Your account has been created, you can now log in.',response.data)

if __name__ == "__main__":
      unittest.main()