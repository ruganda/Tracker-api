"""This module defines tests for the user class and its methods"""
import unittest
from app.models.user import User


class UserTests(unittest.TestCase):
    """Define and setup testing class"""

    def setUp(self):
        """ Set up user object before each test"""
        self.user = User("mubarak","ruganda","password",True)

    def test_isuccessful_registration(self):
        """Test is a user with correct credentials can register sucessfully"""
        res = self.user.register("Mubarak ruganda", "ruganda", "password",)
        self.assertEqual(res, "Registration successfull")

    def test_duplicate_user(self):
        """Test with an already existing user, try registering a user twice"""
        self.user.register("Mubarak ruganda", "ruganda", "password",)
        res = self.user.register("Mubarak ruganda", "ruganda", "password",)
        self.assertEqual(res, "Username already exists.")

    def test_user_login(self):
        """Test if a user with valid details can login"""
        self.user.register(" Mubarak ruganda", "ruganda", "password")
        res = self.user.login("ruganda", "password")
        self.assertEqual(res, "Login successful")

    def test_wrong_password(self):
        """Test for a login attempt with a wrong password"""
        self.user.register("Mubarak ruganda", "ruganda", "654123", )
        res = self.user.login("ruganda", "password")
        self.assertEqual(res, 'invalid username or password')

    def test_non_existing_user_login(self):
        """Test if a non-existing user can login"""
        res = self.user.login("Kapere", "654123")
        self.assertEqual(res, "user does not exist")
    
    def test_is_aplha(self):
        res = User.validate_input("   Ruganda   ")
        self.assertEqual(res,"Ruganda")

    def test_is_aplha_with_other_characters(self):
        res = User.validate_input("  *-238 Ruganda   ")
        self.assertEqual(res,"Your input contains invalid characters")
        