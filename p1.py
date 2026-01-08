class Login:
    def __init__(self):
        self.users = {"admin": "1234"}

    def authenticate(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Login Successful")
        else:
            print("Invalid Credentials")


login = Login()
login.authenticate("admin", "1234")
