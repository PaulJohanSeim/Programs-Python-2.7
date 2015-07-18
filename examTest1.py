# Copyright Paul-Johan Seim

class courseInfo(object):

    def __init__(self, courseName):
        self.courseName = courseName
        self.psetsDone = []
        self.grade = "No Grade"
        
    def setPset(self, pset, score):
        self.psetsDone.append((pset, score))
        
    def getPset(self, pset):
        for (p, score) in self.psetsDone:
            print "fer"
            if p == pset:
                return score

    def setGrade(self, grade):
        if self.grade == "No Grade":
            self.grade = grade

    def getGrade(self):
        return self.grade



class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))

    def setGrade(self, grade, course="6.01x"):
        courseInfo(course).setGrade(grade)

    def getGrade(self, course="6.02x"):
        return courseInfo(course).getGrade()

    def setPset(self, pset, score, course="6.00x"):
        courseInfo(course).setPset(pset, score)

    def getPset(self, pset, course="6.00x"):
        return courseInfo(course).getPset(pset)

