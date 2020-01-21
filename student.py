from person import NSSPerson
class Student(NSSPerson):
    def __init__(self, firstName, lastName, slackHandle):
        super().__init__(firstName, lastName, slackHandle)
        self.exercises = list() 
    