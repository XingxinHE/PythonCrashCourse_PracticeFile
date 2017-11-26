class User():
    """This is a class for user."""
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print("\nThe follow is the information of this user: ")
        print("First Name: "+self.first_name)
        print("Last Name: "+self.last_name)
    
    def greet_user(self):
        print("Hello! "+self.first_name+" "+self.last_name+".")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

liliyun = User('Steven','LI')
liangyiming = User('Marcus','LIANG')
hexingxin = User('Morris','HE')

liliyun.describe_user()
liliyun.greet_user()

liangyiming.describe_user()
liangyiming.greet_user()

hexingxin.describe_user()
hexingxin.greet_user()
hexingxin.increment_login_attempts()
print(hexingxin.login_attempts)
hexingxin.increment_login_attempts()
hexingxin.increment_login_attempts()
hexingxin.increment_login_attempts()
hexingxin.increment_login_attempts()
hexingxin.increment_login_attempts()
print(hexingxin.login_attempts)
hexingxin.reset_login_attempts()
print(hexingxin.login_attempts)