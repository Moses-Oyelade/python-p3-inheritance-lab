#!/usr/bin/env python

from user import User

import random




class Teacher(User):
   
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
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
        index_last = len(self.knowledge) -1
        return self.knowledge[random.randint(0, index_last)]
    
    
    
    
teacher1 = Teacher("John", "Bull")
# print(teacher1.__dict__)
print(teacher1.teach())
