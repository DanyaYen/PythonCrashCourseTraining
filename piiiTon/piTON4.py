class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nUser Profile for {self.first_name} {self.last_name}:")
        print(f"  Age: {self.age}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name}! Hope you're having a great day.")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts
    
class Admin(User):
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "can modify site settings"]

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


user1 = User("John", "Doe", 30, "john.doe@example.com", "New York")
user2 = User("Jane", "Smith", 25, "jane.smith@example.com", "Los Angeles")
user3 = User("Bob", "Johnson", 35, "bob.johnson@example.com", "Chicago")

for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()
    print(f"Login attempts: {user.increment_login_attempts()}")
    print(f"Login attempts: {user.increment_login_attempts()}")
    print(f"Reset login attempts: {user.reset_login_attempts()}")

admin = Admin("Alice", "Admin", 35, "alice.admin@example.com", "Admin Office")

admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()