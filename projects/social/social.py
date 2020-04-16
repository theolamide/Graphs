import random

from util import Queue


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        print(self.name)


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # Use add_user num-users times

        # Create friendships
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")

        # New friendships method
        # Randomly genreate friendships keeping new and rejecting duplicates till we get tot the number of friendships we need (num_user * avg friendships //2)

        # Keep track of good friendships and collisions
        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1

        print(f"Total collisons: {collisions}")

        # # generate all friendships
        # possible_friendships = []

        # # Avoid dupes by making sure first number is smaller than a secodn
        # for user_id in self.users:
        #     for friend_id in range(user_id+1, self.last_id+1):
        #         possible_friendships.append((user_id, friend_id))
        # # Shuffle all possible friendships
        # random.shuffle(possible_friendships)
        # # Create for first X pairs
        # for i in range(num_users*avg_friendships//2):
        #     friendship = possible_friendships[i]
        #     self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # !!!! IMPLEMENT ME

        # Keyword decode
        # Shortest tells us breadth first
        # extended network tells us traversal, connected component

        # Planning
        # how to build the graph? DOne in the graph class
        # Start at given user Id, do a bft, and returna path to each friend
        # Create queue

        qq = Queue()
        # Enqueue path
        qq.enqueue([user_id])
        # Create visited
        visited = {}  # Note that this is a dictionary, not a set

        # populate visited
        # While queue not empty
        while qq.size() > 0:
            # dequeue forst path
            path = qq.dequeue()
            vertex = path[-1]
            # IF not visited
            if vertex not in visited:
                # Do the thing
                # Add to visited
                visited[vertex] = path
                # For each neighbor
                for neighbor in self.friendships[vertex]:
                    # Copy path and enqueue
                    new_path = path.copy()
                    new_path.append(neighbor)
                    qq.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    # print("friendships")
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # print("connections")
    # print(connections)

    # total_social_paths = 0
    # for user_id in connections:
    #     total_social_paths += len(connections[user_id])

    # print(f"Avg length of social path: {total_social_paths/len(connections)}"
