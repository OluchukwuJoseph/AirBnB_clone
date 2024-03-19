#!/usr/bin/python3
'''This module tests for the user class'''

from models.user import User
import unittest


class TestUser(unittest.TestCase):
    '''TestUser tests the attributes
    of the user class'''

    def setUp(self):
        '''this setup method initializes
        a User instance to each test case'''
        self.instance = User()

    def test_email(self):
        '''test_email tests the email of the user'''
        self.assertEqual(type(self.instance.email), str)
        self.assertEqual(self.instance.email, '')

    def test_password(self):
        '''test_password tests the password of the user'''
        self.assertIsInstance(self.instance.password, str)
        self.assertEqual(self.instance.password, '')

    def test_first_name(self):
        '''test_first_name tests the first name of the user'''
        self.assertIsInstance(self.instance.first_name, str)
        self.assertEqual(self.instance.first_name, '')

    def test_last_name(self):
        '''test_last_name tests the last_name of the user'''
        self.assertIsInstance(self.instance.last_name, str)
        self.assertEqual(self.instance.last_name, '')
