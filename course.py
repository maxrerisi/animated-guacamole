class Course:
    def __init__(self, courseName, teacherName, weight, gradingRubric):
        self.assignments = {a:{} for a in gradingRubric} 
        # keys are assignment types (assessment, homework etc)
        # each assignment type has some sort of setting "same weight", "point weight", or "participation" (which can be self set)
        courseID = get_course_id(courseName, teacherName)
        self.weight = weight
        self.courseName = courseName
        self.teacherName = teacherName
        self.gradingRubric = gradingRubric



def get_course_id(courseName, teacherName):
    # connect to database and get courseID
    pass
