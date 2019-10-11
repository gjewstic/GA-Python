class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        print('instance created')

    def say_hello(self):
        print(f'Hello, my name is {self.name}, and I am {self.age} years old.')


# - classes allow us to create our own data types.  'self' has to be in the __init__() function/method
# p1 = Person('Greg', 44)
# p1.say_hello()
# print(type(p1))

# 3

# - Create a Rectangle class
# Write methods to calculate the perimeter and area for your rectangles

class Rectangle:
    def __init__(self, w, l):
        self.perimeter = 2 * (w + l)
        self.area = (w * l)

    def cal_rectangle(self):
        print(
            f'The perimeter of the rectangle is {self.perimeter} centimetres, and the area of the rectangle is {self.area} centimetres')


rect = Rectangle(10, 20)
# rect.cal_rectangle()

# - Homework: Build an instagram account class
# - Class should have username, email and a list of pictures and a list of followers (follower usernames and emails in the list)
# - An instagram account can follow another instagram account (method)

instagram_followers = [
    {'name': 'follower_1', 'email': 'follower_1@email.addr'},
    {'name': 'follower_2', 'email': 'follower_2@email.addr'},
    {'name': 'follower_3', 'email': 'follower_3@email.addr'}
]

users = []
pictures = []

for follower in instagram_followers:
    users.append(follower)
    # print(follower['name'])


class InstagramAccount:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.followers = []
        self.following = []
        self.pictures = []

    def add_photo(self, photo_url):
        self.pictures.append(photo_url)
    '''
    def follow(self, account):
        try:
            account.followers.append(self)
        except:
            print(f'{account} is not a valid Instagram account')
    '''

    def follow(self, account):
        # isinstance() function used to check if data type matches, else print error
        if isinstance(account, InstagramAccount):
            account.followers.append(self)
        else:
            print(f'{account} is not a valid Instagram Account')

    def get_followers(self):
        return self.followers
    #

    def __repr__(self):
        return f'\nusername: {self.username}\nemail: {self.email}\nfollowers: {self.followers}\n'


ac1 = InstagramAccount('@greg', 'greg@email.addr')
ac2 = InstagramAccount('@greg2', 'greg2@email.addr')

ac1.follow(ac2)
# ac2.follow(ac1)

# print(ac1)
print(ac2)
