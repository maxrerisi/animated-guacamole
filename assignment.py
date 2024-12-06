class Assignment:
    def __init__(self, name, due_date, courseID, type):
        self.name = name
        self.due_date = due_date
        self.courseID = courseID
        self.type = type
        self.out_of = None
        self.assignmentID = get_assignment_id(name, type, courseID)


def get_assignment_id(name, type, courseID):
    # should say something like courseID#typeID#assignmentID
    pass