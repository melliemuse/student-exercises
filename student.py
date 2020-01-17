class Student:
    def __init__(self, firstName, lastName, slackHandle, cohortId):
        self.firstName = firstName
        self.lastName = lastName
        self.slackHandle = slackHandle
        self.cohortId = cohortId
        self.exercises = list() 
    