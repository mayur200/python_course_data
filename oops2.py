class University:
	univ_name = 'Mumbai University' #class attribute
	def __init__(self, student_id, student_name, student_branch):
		self.id = student_id
		self.name = student_name
		self.branch = student_branch

student1 = University(2, 'Rakesh', 'Arts')
print(student1.id, student1.name, student1.branch)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

class Circle:
	def __init__(self,colo_r,radiu_s):
		self.color = colo_r
		self.radius = radiu_s

	def compute_area(self):
		self.area = 3.14*self.radius* self.radius

circle1 = Circle('red', 5)
circle2 = Circle('green', 10)

circle1.compute_area()
circle2.compute_area()


print("ans is", circle1.area, circle2.area)
