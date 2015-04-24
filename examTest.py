class courseInfo(object):
    def __init__(self, courseName, grade):
        self.courseName = courseName
        self.psetsDone = []
        self.grade = grade
        
    def setPset(self, pset, score):
        self.psetsDone.append((pset, score))
        
    def getPset(self, pset):
        for (p, score) in self.psetsDone:
            if p == pset:
                return score

    def setGrade(self, grade):
        self.grade = grade
        print "hei"
        print "grade = " +str(self.grade)

    def getGrade(self):
        print self.grade
        print "deg"
        
        return self.grade


class edx(object):
    def __init__(self, courses, grades):
        self.courses = courses
        self.grades = grades
        self.myCourses = []
        self.myGrades = []
        for course in courses:
            for grade in grades:
                self.myCourses.append(courseInfo(course, grade))
            
    def setGrade(self, grade, course):
        hu = courseInfo(course, grade)
        hu.setGrade(grade)

    def getGrade(self, grade, course):
        hu = courseInfo(course, grade)
        return hu.getGrade()

    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        courseInfo(course).setPset(pset, score)
        
        pass

    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string        

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        return courseInfo(course).getPset(pset)



#edX = edx( ["6.00x","6.01x","6.02x"] )


#me = edX.setGrade(90, "6.01x")


#se = edX.getGrade()


#edX.setPset(1,100)
#print her
#edX.setPset(2,100,"6.00x")
#edX.setPset(2,90,"6.00x")

#edX.setGrade(100)

#for c in ["6.00x","6.01x","6.02x"]:
    #edX.setGrade(90,c)