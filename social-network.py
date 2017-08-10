networkUsers = []

class User:

    def __init__(self, name):
        self.username = name
        self.password = ""
        self.connections = []
        self.number_friends = 0
        networkUsers.append(name)

    def set_password(self, password):
        self.password = password

    def add_connections(self, friend):
        self.connections.append(friend)
        self.number_friends += 1

    def get_user_info(self):
        print("Username: " + self.username)
        print("Password: " + self.password)
        print("Friends: " + str(self.connections))


class Network:
    def __init__(self):
        self.users = networkUsers



################################################################################


annie = User("annie")
annie.set_password("banana")

allie = User("allie")
allie.set_password("allie")

annie.add_connections(allie.username)


network1 = Network()

print(str(network1.users))

annie.get_user_info()


################################################################################

create_username = input("Username?")
create_password = input("Password?")

new_user = User(create_username)
new_user.set_password(create_password)

print("Congratulations! You created a new account!")

new_friend = input("Who would you like to be friends with?")
new_user.add_connections(new_friend)
new_user.get_user_info()
