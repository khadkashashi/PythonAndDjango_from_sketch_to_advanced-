import random
print(random.random())
random_num = random.randint(1,50)
print(random_num)







print("---------------welcome to guessing challenge")
random_num=random.randint(1,50)
print("random number is:", random_num)
count=0
#max_lim=5
while count<5:
    # print("Life left", max_limit-count)
    #user_num = int(input(f"life lefit {max_limit-count} Enter the number:  "))
    user_num =int(input("enter the number:"))
    count=count+1
   

    if user_num ==random_num:
        print(f"number guess successfully in {count} times")
        break
    else:
        if random_num<user_num:
            print("lower")
        else:
            print("higher")
        print("try again !")
        #message="choose a smaller number." if random_num<user_num else "chose a larger number"
        #if count>=max_lim:
        #print(f"limit reached, random number of{'random_num'}")


print("you used all attempts")








#refined onee 
int("--------------Welcome to the Number Guessing Game-----------------")

random_num = random.randint(1, 50)
print("Generated number is", random_num)

count = 0
max_limit = 5

while True:
    user_num = int(input(f"Attempts left {max_limit-count}: Enter your guess: "))
    count += 1

    if user_num == random_num:
        print(f"\nCongratulations! You guessed the number in {count} attempts.")
        break
    else:

        message = "Choose a smaller number."   if random_num < user_num else "Choose a larger number."
        print(f'\n{message} Please try again! ')
        if count >= max_limit:
            print(f"\nNo attempts remaining. The correct number was {random_num}.")
            break






# rock paper scissors
data=['r','p','s']
while True:
    computer=random.choice(data)# list bata 1 ota data linx
    user=input('enter a value r,p,s :').lower()
    if user not in data:
        print("Invalid input choose r, p ,s ")
        continue

    if computer == user:
        print("Tie")

    elif (user=='r'and computer=='s')or(user=='p'and computer=='r')or (user=='s'and computer=='p'):
        print('u win')
        
            
    else:
        print('u lost')
    user_input= input ('do u wnat to play again y/n').lower()
    if user_input=="n":
        break


