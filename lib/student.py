#!/usr/bin/env python

from user import User


class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
        self.topic_string = ""
    
    def learn(self, study_topics):
        self.knowledge.append(study_topics)
        if len(self.knowledge) == 1:
            self.topic_string = self.knowledge[0]
        elif len(self.knowledge) == 2:
            self.topic_string =  " and ".join(self.knowledge)
        else:
            self.topic_string = ", ".join(self.knowledge[:-1]) + ", and " + self.knowledge[-1]
    

student1 = Student("Elisha", "Kibet")
student1.learn("Intro to OOP")
student1.learn("Intro to Databases")
print(f"I'm {student1.first_name} {student1.last_name} and currently learning {student1.topic_string}")
