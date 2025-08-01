import datetime
from post_req import requires_registration

# --- Classes ---

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"{self.author} ({self.timestamp.strftime('%Y-%m-%d %H:%M')}): {self.content}"

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.posts = []

    def share_post(self, content):
        post = Post(self.username, content)
        self.posts.append(post)
        return post

# --- Global State ---

users = {}
all_posts = []
current_user = [None]  # list to allow mutation inside decorators

# --- Core Functions ---

def register():
    username = input("New username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("New password: ")
    users[username] = User(username, password)
    print("User registered.")

# @requires_registration(users)
def login():
    username = input("Username: ")
    password = input("Password: ")
    user = users.get(username)
    if user and user.password == password:
        print(f"Welcome, {username}!")
        user_session(user)  # ✅ pass the user directly
    else:
        print("Invalid credentials.")

def user_session(user):  # ✅ now takes the user as a parameter
    while True:
        print("\n1. Share post\n2. View posts\n3. Logout")
        choice = input("> ")
        if choice == "1":
            content = input("Enter your post: ")
            post = user.share_post(content)
            all_posts.append(post)
            print("Post shared.")
        elif choice == "2":
            print("\n--- Feed ---")
            for post in all_posts:
                print(post)
        elif choice == "3":
            print("Logged out.")
            break
        else:
            print("Invalid option.")
# --- Main Menu ---

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        option = input("> ")
        if option == "1":
            register()
        elif option == "2":
            login()
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
