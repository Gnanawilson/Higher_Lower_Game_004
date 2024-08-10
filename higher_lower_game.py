import random
import higher_lower_logo 
import higher_lower_data
import os


print(higher_lower_logo.logo)
score=0
def display(account):
    name=account["name"]
    descryption=account["descryption"]
    country=account["Country"]
    return f"{name}, a {descryption},from {country}"

def check_answer(guess,follower_count_1,follower_count_2):
    if follower_count_1<follower_count_2:
        if guess==1:
            return False
        else:   
            return True
    else:    
        if guess==1:
            return True
        else:
            return False

account_2=random.choice(higher_lower_data.data)
continue_flag=True        
while continue_flag:     
  account_1=account_2
  account_2=random.choice(higher_lower_data.data)
  while account_1==account_2:
      account_2=random.choice(higher_lower_data.data)
  print(f"compare 1: {display(account_1)}")
  print(higher_lower_logo.vs)
  print(f"compare 2: {display(account_2)}")
  guess=int(input("Who has more followers? type 1 or 2: "))
  follower_count_1=account_1["follower_count"]
  follower_count_2=account_2["follower_count"]
  print(follower_count_1)
  print(follower_count_2)
  is_correct=check_answer(guess,follower_count_1,follower_count_2)
  os.system('cls')
  print(higher_lower_logo.logo)
  if is_correct==True:
    score+=1
    print(f"You are right.Your score is:{score}")
  else:
    print(f"You are wrong..Your final score is:{score}")
    continue_flag=False