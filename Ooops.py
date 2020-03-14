import sys
print(sys.version)
class University:
	univ_name = 'Mumbai University' #class attribute
	def __init__(self):
		print('an object is created!')
	def assign_id(self, student_id):
		self.id =  student_id   #assign student_id to self.id
	def assign_name(self, student_name):
		self.name = student_name
	def assign_branch(self, student_branch):
		self.branch = student_branch
	def assign_marks(self,student_marks):
		self.marks = student_marks

student_1 = University() #Object
student_2 = University()

student_1.assign_id(1) #passing id to def assign_id(self,student_id)
student_1.assign_name('Mayur')
student_1.assign_branch('IT')
student_1.assign_marks(60)
print(University.univ_name)
print(student_1.id)
print(student_1.name)
print(student_1.branch)
print(student_1.marks)