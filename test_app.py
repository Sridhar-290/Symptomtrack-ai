import unittest
from app import app, hash_pw
import hashlib

class MedivisionTestCase(unittest.TestCase):
    
    def setUp(self):
        """
        Set up the Flask test client before each test runs.
        """
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_hash_pw(self):
        """
        Test the password hashing utility function.
        It should accurately match standard SHA-256 output.
        """
        password = "mysecretpassword123"
        expected_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        result = hash_pw(password)
        
        self.assertEqual(result, expected_hash, "Password hashing function failed to match SHA-256.")

    def test_index_route_loads(self):
        """
        Test that the home page (index) loads properly (Status Code 200).
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_route_loads(self):
        """
        Test that the login page loads correctly.
        """
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        # Ensure password field exists somewhere in the rendered HTML
        self.assertIn(b'password', response.data.lower()) 

    def test_signup_route_loads(self):
        """
        Test that the signup page loads correctly.
        """
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)

    def test_protected_user_routes(self):
        """
        Test that unauthorized users trying to access protected user 
        dashboards are forcibly redirected to login (Status Code 302).
        """
        response = self.client.get('/user/dashboard', follow_redirects=False)
        # 302 means Temporary Redirect (Flask redirects them to login)
        self.assertEqual(response.status_code, 302)

    def test_protected_admin_routes(self):
        """
        Test that unauthorized users trying to access protected admin 
        dashboards are forcibly redirected to login (Status Code 302).
        """
        response = self.client.get('/admin/dashboard', follow_redirects=False)
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
