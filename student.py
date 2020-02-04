from person import NSSPerson
class Student(NSSPerson):
    def __init__(self, firstName, lastName, slackHandle, cohort):
        super().__init__(firstName, lastName, slackHandle, cohort)
        self.exercises = list() 
    def __repr__(self):
        return f'{self.firstName} {self.lastName} is in cohort {self.cohort}'