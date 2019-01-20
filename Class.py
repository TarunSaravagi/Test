#Parent Class
class Student :
	' this is commented' 
	count =0
	
	def __init__ (self,name,roll):
		self.name= name
		self.roll= roll
		Student.count += 1
		
	def display (self):
		print ("This is the basic class program:" ,self.name, "  roll:" ,self.roll,
		 " \n also   " ,self.count)
	
#Child Class	
class Developer (Student) :
	count=10
	def __init__ (self,name,roll,pay):
		super().__init__(name,roll)
		self.pay= pay
		


class Manager (Student) :
	count=10
	def __init__ (self,name,roll,employess=None):
		super().__init__(name,roll)
		if employess ==None:
			self.employess =[]
		else:
			self.employess= employess
		
		
	def add_Emp (self,emp):
		if emp not in self.employess:
			self.employess.append(emp)
			
	def rem_Emp (self,emp):
		if emp in self.employess:
			self.employess.remove(emp)	
	
	def print_emp (self):
#		for i in self.employess:
		print ("The emloyee name" ,self.employess)
	
	

#print (help(Developer))
#print (help(Student))	

#s1= Student('Tarun',123)
#s2= Student('Tarun1',124)
#s3= Student('Tarun1',124)
#s4c= Student('Tarun1',124)

#s1.display()
#s2.display()

d1= Developer('Tarun2',1234,797)
d2= Developer('Tarun3',1245,8788)


m1= Manager('M1',222,d1)
m1.print_emp()
m1.display()

#m2= Manager('M2',33,'Golu2')
#
#
#m1.display()
#m2.display()

#d1.display()
#d2.display()






#############################################################

#s3 = getattr(s1, 'roll') 
#print (s3)
#
#setattr(s2, 'roll', 155)
#s4 = getattr(s2, 'roll') 
#print (s4)

#print ("Employee.__doc__:", Student.__doc__)
#print ("Employee.__name__:", Student.__name__)
#print ("Employee.__module__:", Student.__module__)
#print ("Employee.__bases__:", Student.__bases__)
#print ("Employee.__dict__:", Student.__dict__ )

#delattr(s1, 'roll')
#s3 = getattr(s1, 'roll') 
#print (s3)

#  Write a code for Class  Developer & Anchor using Inheritance
