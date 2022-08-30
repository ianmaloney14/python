class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0


    def display_info(self):
        print(" Name:", self.first_name + self.last_name,"Email:", self.email,"Age:", self.age)

    def enroll(self, is_rewards_member):
        if is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = self.gold_card_points + 200
            print("Welcome "  + self.first_name)
            print("You got " + str(self.gold_card_points) + " gold card points for enrolling!")
        else:
            print("You are already a member!")
            print("You have " + str(self.gold_card_points) + " gold card points!")

    def spend_points(self, amount):
        self.amount = amount
        if self.amount >= self.gold_card_points:
            print("You don't have enough points.")
        else:
            total = self.gold_card_points - amount
            print("You spent " + str(amount) + " gold card points.")
            print("You have " + str(total) + " gold card points left.")

user_1 = User("John ", "Doe\n", "johndoe123@gmail.com\n", 24)

user_1.display_info()
user_1.enroll(False)
user_1.spend_points(150)



# # Assignment: User
# # For this assignment you will create the user class and add a couple methods!

# ####### Note: NOT ALL CODE FROM THE VIDEO IS PROVIDED #######

# class User:

#     def __init__(self, first_name, last_name, email, age):

#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.age = age
#         self.is_rewards_member = False
#         self.gold_card_points = 0

#     # Methods:
#     # display_info(self) - Have this method print all 
#     # of the users' details on separate lines.

#     def display_info(self):
#         print("==========================")
#         print(f"First name: {self.first_name}")
#         print(f"Last name: {self.last_name}")
#         print(f"Email: {self.email}")
#         print(f"Age: {self.age}")
#         print(f"Member: {self.is_rewards_member}")
#         print(f"Current Points: {self.gold_card_points}")
#         print("==========================")

#     def enroll(self):

#         # NINJA BONUS
#         # Add logic in the enroll method to check if 
#         # they are a member already, and if they are, 
#         # print "User already a member." and return False, otherwise return True.

#         # REGULAR STUFF

#         # Have this method change the user's member
#         # status to True and 
#         self.is_rewards_member = True

#         # set their gold card points to 200.
#         #######   You can do it!


    
    
#     def spend_points(self, amount):

#         # Add logic in the spend points method
#         # to be sure they have enough points to 
#         # spend that amount and handle appropriately.
        
#         # PSEUDO CODE FOR NINJA BONUS
#         # if they don't have enough points:
#             # print to the console -- "You don't have enough points."
#             # then return # exit function!

#         # decrease the user's points by the amount specified.
#         self.gold_card_points
#         # .... this line is incomplete .. how do set this to a new value?

    

#     # Ninja Bonuses:



# my_user = User("Sadie", "Flick", "sflick@codingdojo.com", 99)
# my_user.display_info()
# my_user.enroll()
# my_user.display_info()
# my_user.spend_points(100)
# my_user.display_info()