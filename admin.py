from user import User
class Privileges():
	def __init__(self):
		self.privileges = ['add post','delete post','ban user']

	def show_privileges(self):
		print("privileges:")
		print(self.privileges)

class Admin(User):
	def __init__(self, first, last):
		super().__init__(first,last)
		self.privileges = Privileges()

# a = Admin('heidi','keller')
# a.privileges.show_privileges()