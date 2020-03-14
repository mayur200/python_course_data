class Company:
	hike_ratio = 0.1
	active_count = 0

	def __init__(self, emp_id, emp_name, emp_salary, emp_position):
		self.id = emp_id
		self.name = emp_name
		self.emp_salary = emp_salary
		self.emp_position = emp_position
		self.status = 'Active'
		Company.active_count +=1

	def compute_hike(self):
		return self.emp_salary*Company.hike_ratio

	def change_status(self, new_status):
		if self.status in ['Suspended', 'Terminated'] and new_status == 'Active':
			Company.active_count +=1
		elif  self.status == 'Active' and new_status in ['Suspended','Terminated']:
			Company.active_count -=1

		self.status = new_status

emp1 = Company(1, 'ABC', 100000, 'Manager')
emp2 = Company(2, 'XYZ', 200000, 'IT')
print(emp1.name)
print(emp1.compute_hike())
print(emp1.change_status('Suspended'))
print(emp1.status)
print(emp2.status)
print(emp1.change_status('Suspended'))

print(Company.active_count)

