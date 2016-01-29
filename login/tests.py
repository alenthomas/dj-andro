from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class LoginTest(TestCase):
    def test_reg_form(self):
        """
        Test for proper rendering of register form
        """
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
