#class=>blueprint ,object=>isntance in class
 class student:
        def __init__(self,name,mark):
            self.name=name
            self.mark=mark
        def get_grade(self):
            if self.mark>=90:
                return "A"
            elif self.mark>=75:
                return "B"
            else:
                return "C"
