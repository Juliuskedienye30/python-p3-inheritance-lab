#!/usr/bin/env python

from user import User  # Import the User class so we can inherit from it

class Student(User):
    """
    Student class that inherits from User.
    Represents a student who can learn and store knowledge.
    """

    def __init__(self, first_name, last_name):
        """
        Initialize the student with first and last name (from User)
        and an empty list to store knowledge.
        """
        # Call the __init__ method from the User class to set first & last name
        super().__init__(first_name, last_name)
        
        # List to store all topics or information the student learns
        self.knowledge = []  

    def learn(self, new_info):
        """
        Add a piece of information to the student's knowledge list.
        new_info: string or any data representing something the student learned
        """
        self.knowledge.append(new_info)  # Store the learned info in the list
