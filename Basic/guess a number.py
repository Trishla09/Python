import random
num=random.randint(1,20)
guess=int(input("Can u guess the number which is less than 20:"))
while num!=guess:
      if num>guess:
        print("u r guess is low")
      else:
        print("u r guess is high ")
      guess=int(input("guess again :"))
print("u won")

          
