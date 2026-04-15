from dataclasses import dataclass,field
@dataclass
class Student:
    name:str
    student_id:str
    assignments_done:int=0
    scores:list[int]=field(default_factory=list)
    def submit(self, score: int):
        self.assignments_done+=1
        self.scores.append(score)
    def avg_score(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores)/len(self.scores)
       
@dataclass
class Course:
    course_name:str
    professor:str
    capacity:int
    students:list[Student]=field(default_factory=list)
    enrolled:int=field(init=False)
    def __post_init__(self):
        self.update_enrolled()
    def update_enrolled(self):
        self.enrolled = len(self.students)
    def enroll(self, student: Student) -> bool:
        if self.enrolled<self.capacity:
            self.students.append(student)
            self.update_enrolled()
            return True
        return False 
    def top_student(self) -> str:
        if not self.students:
           return "No data"
        best_students = {}
        for student in self.students:
            best_students[student.name] = student.avg_score()
        best_students = list(best_students.items())
        best_students.sort(key= lambda t: t[1], reverse=True)  
        return best_students[0][0]
    
    def course_stats(self) -> str:
        lines = []
        lines.append(f"{self.course_name} ({self.professor}):\n")
        for student in self.students:
            lines.append(f"  {student.name} - {student.assignments_done} assignments, avg  {student.avg_score():.1f} pts\n")
        lines.append(f"Enrolled: {self.enrolled}/{(len(self.students))}\n")
        joined_l = " ".join(lines)
        return joined_l


s1 = Student("Liam", "S101")
s2 = Student("Nora", "S102")
s3 = Student("Omar", "S103")

s1.submit(72)
s1.submit(88)
s1.submit(91)
s2.submit(95)
s2.submit(89)
s3.submit(60)

c = Course("Data Structures", "Prof. Kim", 3)
print(c.enroll(s1))
print(c.enroll(s2))
print(c.enroll(s3))
print(c.enroll(Student("Priya", "S104")))
print(c.enrolled)
print(c.top_student())
print(c.course_stats())


            





