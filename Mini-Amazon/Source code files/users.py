from storage import load_data, save_data

USERS_FILE = "data/users.json"

class UserManager:
    def __init__(self):
        self.users = load_data(USERS_FILE, [])

        if not isinstance(self.users, list):
            self.users = []

        clean_users = []
        for u in self.users:
            if isinstance(u, dict) and "username" in u and "password" in u:
                clean_users.append(u)

        self.users = clean_users            

    def save(self):
        save_data(USERS_FILE, self.users)

    def register(self):
        username = input("Enter username: ").strip()

        if any (u.get("username") == username for u in self.users):
            print("Username already exists!")
            return
        
        password = input("Enter password (>= 6 characters): ").strip()

        if len(password) < 6:
            print("Password is too short!")
            return
        
        new_user = {
            "username": username,
            "password": password
        }
        
        self.users.append(new_user)
        self.save()

        print("Registration successful!")
    
    def login(self):
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        for user in self.users:
            if isinstance(user, dict):
                if user.get("username") == username and user.get("password") == password:
                    print("Login successful!")
                    return username
            
        print("Invalid credentials.")
        return None