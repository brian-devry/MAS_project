import flaskblog.forms as form
import unittest
import unittest

import flaskblog.forms as form


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


 def test_login(self):
     tester = app.test_client(self)
     response = tester.get(
         '/login', content_type = 'html/text')
     self.assertEqual(response.status_code, 200)


     if __name__ == "__main__":
      unittest.main()
