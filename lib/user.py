#!/usr/bin/env python

class User:
    """
    A generic user with a first name and last name.
    This is the base class for Student and Teacher.
    """

    def __init__(self, first_name, last_name):
        """
        Initialize a User with a first name and last name.
        """
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        """
        Return the full name of the user.
        """
        return f"{self.first_name} {self.last_name}"
