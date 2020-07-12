


class Company:
	def __init__(self, emp):
		self.rate = 0.1
	def compute_hike(self,sal):
		self.salary = sal
		self.hiked_perc = self.rate*self.salary
		self.hiked_salary = self.salary + self.hiked_perc
	def employee_name(self,name):
		self.emp_name= name
	def employee_status(self):
		self.emp_status = 'Active'
	def employee_id(self,emplo_id):
		self.emp_id = emplo_id
	def change_status(self, c_state):
		if c_state == 'active':
			self.changed_state = 'terminated/suspended'
		else:
			self.changed_state = 'active'





emp1 = Company()
emp2 = Company()
emp3 = Company()


emp1.compute_hike(200)
emp1.change_status('terminated/suspended')
emp1.employee_status()
emp1.employee_id(1)


print(emp1.hiked_salary)
print(emp1.changed_state)
print(emp1.emp_status)
print(emp1.emp_id)

print("<<<<<<<<<<<<<<<<<og ans>>>>>>>>>>>>>>>>>>>>>>")







