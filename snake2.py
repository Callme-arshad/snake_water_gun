'''
1 for snake 
2 for water 
3 for gun
'''
import random
computer= random.choice([1,2,3])
youDict = {"snake":1,"water":2,"gun":3}
reverseDict = {1:"snake",2:"water",3:"gun"}
first_Choice = input("Enter your choice :-")
first_Choice=youDict[first_Choice]
print("Computer choose",reverseDict[computer])
# pattern notice first_choice-Computer .... 
if((first_Choice-computer)==1 or (first_Choice-computer)==-2):
        print("you loose! computer win ")
elif((first_Choice-computer)==-1 or (first_Choice-computer)==2):
        print("Congrats you win")
elif(first_Choice==computer):
        print("Match draw")
else:
        print("Error ........")


