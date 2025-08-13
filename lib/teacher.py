#!/usr/bin/env python

# Import the User base class
from user import User

# Import Python's random module to help select random knowledge
import random

class Teacher(User):
    """
    Teacher class that inherits from User and can 'teach'
    by returning a random piece of predefined knowledge.
    """

    def __init__(self, first_name, last_name):
        """
        Initialize a Teacher object with:
        - first_name and last_name (inherited from User)
        - a predefined list of knowledge strings
        """

        # Call the __init__ method of the parent (User) class
        # This ensures that first_name and last_name are set
        # without having to rewrite the same code here.
        super().__init__(first_name, last_name)

        # Store a list of knowledge topics the teacher can teach
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        """
        Select and return a random piece of knowledge
        from the teacher's knowledge list.
        """

        # Get a random index between 0 and the last index of the list
        random_index = random.randint(0, len(self.knowledge) - 1)

        # Return the knowledge at that random position
        return self.knowledge[random_index]
