# # def addition():
# # #     a = int(input("First Number "))
# # #     b = int(input("Second Number "))
# # #     print(a + b)

# # # addition()

# # ##########################################################

# # # # def user_info(fname,lname,*args,**kwargs):
# # # #     ''' This Function prints out the data provided to the function
# # # #         by the arguament '''
# # # #     print("{} {} gets {} USD per month as a {}.".format(fname,lname,*args,**kwargs))

# # # # user_info("Joe","Kh")
# # # ##########################################################

# # # # print (1==1)

# # # # name=input("What's your name ? ")
# # # # if name== "joe":
# # # # #     print("Nice to see you {} " .format(name))
# # # # # elif name== "maria":
# # # # #     print("Nice name {} ".format(name))
# # # # # elif name== "mom":
# # # # #     print("You are the best {} ".format(name))
# # # # # else:
# # # # #     print ("Have a Great Day ! ")


# # # # def add():
# # # #     a= float(input("First number "))
# # # #     b= float(input("Number to add "))
# # # #     print (a+b)

# # # # def sub():
# # # #     a= float(input("First number "))
# # # #     b= float(input("Number to subtract "))
# # # #     print(a-b)

# # # # def mul():
# # # #     a= float(input("First number "))
# # # #     b= float(input("Number to multiply "))
# # # #     print(a*b)

# # # # def div():
# # # #     a= float(input("First number "))
# # # #     b= float(input("Number to divide "))
# # # #     print(a/b)

# # # # operation= input("Please choose + , - , * or / ")

# # # # if operation== "+":
# # # #     add()

# # # # elif operation== "-":
# # # #     sub()

# # # # elif operation== '*':
# # # #     mul()

# # # # elif operation== '/':
# # # #     div() 

# # # # else:
# # # #     print ("This Operation is invalid")


# # # ##########################################################

# # # # fruits= ["apple", "orange", "apricot", "pear", "watermelon"]

# # # # for fruit in fruits:
# # # #     print("Would you like a {} ?".format(fruit))


# # # # for number in range(1,11):
# # # #     print("Number {}".format(number))


# # # # temp_f= 40
# # # # while temp_f> 32:
# # # #     print("The temperature is {} degrees".format(temp_f))
# # # #     temp_f -=1
# # # #     if temp_f== 33:
# # # #         break


# # # # for number in range(1,11):
# # # #     if number== 7:
# # # #         pass
# # # #     else:
# # # #         print("Number {}".format(number))

# # # # on=True

# # # # def add():
# # # #     a= float(input("First number "))
# # # #     b= float(input("Number to add "))
# # # #     print (a+b)

# # # # def sub():
# # # #     a= float(input("First number "))
# # # #     b= float(input("Number to subtract "))
# # # #     print(a-b)

# # # # def mul():
# # # #     a= float(input("First number "))
# # # #     b= float(input("Number to multiply "))
# # # #     print(a*b)

# # # # def div():
# # # #     a= float(input("First number "))
# # # #     b= float(input("Number to divide "))
# # # #     print(a/b)


# # # # while on:
# # # #     operation= input("Please choose + , - , * , / or q to exit ")

# # # #     if operation== "+":
# # # #         add()

# # # #     elif operation== "-":
# # # #         sub()

# # # #     elif operation== '*':
# # # #         mul()

# # # #     elif operation== '/':
# # # #         div() 
    
# # # #     elif operation== 'q':
# # # #         on= False

# # # #     else:
# # # #         print ("This Operation is invalid")

# # # #############################################

# # # fruits= ["peaches", "apples", "bananas"]
# # # years= [3, 1988, 2, 987, 2000]

# # # print("apples" in fruits)
# # # print(fruits.index("apples"))



# # # # fruits.append("oranges")
# # # # fruits.extend(years)
# # # # print(fruits)

# # # # # fruits.remove("oranges")
# # # # # print(fruits)

# # # # # fruits.pop(-1)
# # # # # print(fruits)

# # # # print(years)
# # # # years.sort()
# # # # print(years)



# # #######################################################

# # # house= {"area": 60, "floor": 18, "street": 180 }

# # # print(house.items())

# # # print(house.keys())
# # # print(house.pop("street"))
# # # print(house.setdefault("zipcode", 4040))

# # # print(house)
# # # car= {"engine":1500, "seats":5, "area": 57}

# # # house.update(car)
# # # print(house)
# # # house.update(area= 61)
# # # print(house)


# # # print(house.get("area"))
# # ####################################################



# # from random import random


# # class Person:
# #     def __init__(self, firstname, lastname, health, status):
# #         self.firstname= firstname
# #         self.lastname= lastname
# #         self.health= health
# #         self.status= status

# #     def introduce(self):
# #         print("My Full name is {} {} ".format(self.firstname,self.lastname))

# #     def emote(self):
# #         emotion= random.randrange(1,3)
# #         if emotion == 1:
# #             print("{} {} is Happy today. ".format(self.firstname,self.lastname))
# #         elif emotion == 2:
# #             print("{} {} is Sad today. ".format(self.firstname,self.lastname))

# #     def status_change(self):
# #         if self.health == 100:
# #             print("{} is healthy. ".format(self.firstname))
# #         elif self.health >= 75:
# #             print("{} is feeling a little tired today. ".format(self.firstname))
# #         elif self.health >=50:
# #             print("{} needs to go to the doctor ASAP. ".format(self.firstname))
# #         else:
# #             print("{} is dead") 

# # M = Person("Maria", "Kh", 75, "True")
# # F = Person("Fadi", "Me", 100, "False")
# # Mo = Person("Ra", "Ya", 100, "True")




# # class Enemy(Person):
# #     def __init__(self, weapon, firstname, lastname, health, status):
# #         super().__init__(firstname, lastname, status, health) 
# #         self.weapon= weapon

# #     def hurt(self, other):
# #         if self.weapon== 'rock':
# #             other.health -=10
# #         elif self.weapon== 'stick':
# #             other.health -=5
# #         print("{} 's health is now {}".format(other.firstname,other.health))
    

# #     def insult(self, other):
# #         if other.health<= 80:
# #             print("You are Weak {} :D :D " .format(self.firstname))


# # D= Enemy('stick', 'Devil', 'Creature', 100, 'False')

# # D.hurt(F)

# ###########################################

# # Parent Class 1

# class Item():
#     def __init__(self, sku):
#         self.sku= sku

#     def show_sku(self):
#         print("Hi")

    
# #Parent Class 2

# class Garment():
#     def __init__(self, section, type):
#         self.section= section
#         self.type= type

#     def show_garment(self):
#         print("The Garment is in section {},{} ".format(self.section,self.type))


# #Child Class 

# class Shirts(Item, Garment):
#     def __init__(self, sku, section, type, name, color):
#         self.name=name
#         self.color=color
#         Item.__init__(self, sku)
#         Garment.__init__(self,section, type)

#     def show_shirt(self):
#         print("{} {} is on SALE".format(self.name,self.color))

# Blouse= Shirts("0001", "S5", "Top", "Formal Blouse", "White")

# Blouse.show_sku()
# Blouse.show_garment()
# Blouse.show_shirt()


