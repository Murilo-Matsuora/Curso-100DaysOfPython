class User:
    def __init__(self, user_id, username):
        # Initialize attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def print_stats(self):
        print(f"Stats of {self.username}:\n - Followers: {self.followers}\n - Following: {self.following}")


user_1 = User("001", "Murilo")
user_2 = User("002", "Murilo Júnior")

user_1.print_stats()
user_2.print_stats()
user_1.follow(user_2)
user_1.print_stats()
user_2.print_stats()
user_2.follow(user_1)
user_1.print_stats()
user_2.print_stats()

