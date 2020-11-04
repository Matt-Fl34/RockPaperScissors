import random
import time

incorrect_input_list = ["Please Press 'y' to start", "Come On. It isn't that hard. Just Press 'y' to start", "please Try again" , "Don't be a dummy. Press 'y', it's quite yummy!",
                        "Please Try again" , "Not funny" , "Come on. I want this to be over too, you know." ,]
list1 = ['rock','paper','scissors']

win_count1 = 0
win_count2 = 0



def get_choice():
    
    while True:
       
        print()
        print('* * * * * * * * * * * *')
        print("choose 'r' for rock")
        print("choose 'p' for paper")
        print("choose 's' for scissors")
        print('* * * * * * * * * * * *')
        print()
        time.sleep(3)
        print('Make Your Choice in...')
        print()
        time.sleep(2)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print()
        
        player_choice = input('>')
        print()
        comp_choice = random.choice(list1)
        
        if player_choice not in ['r', 'p', 's']:
            print('Wrong Choice!. Lets try that again...')
            time.sleep(2)
        
        elif player_choice == 'r':
            player_final_choice = 'rock'
            break
        
        elif player_choice == 'p':
            player_final_choice = 'paper'
            break
        
        elif player_choice == 's':
            player_final_choice = 'scissors'
            break
    
    return player_final_choice, comp_choice
    
def main():
    
    global result
    global win_count1
    global win_count2
        
    while win_count1 < 2 and win_count2 < 2:
            
        print('You Choose:', result[0])
        print('Opponent Chooses:', result[1])
        time.sleep(1)
        
        if result[0] == result[1]:
            print("It's a Draw!")
            time.sleep(2)
            print('Best out of 3!')
            time.sleep(2)
            result = get_choice()

        elif result[0] == 'rock':
            if result[1] == 'paper':
                print('You Lose.')
                time.sleep(2)
                win_count2 += 1
                
                if win_count1 < 2 and win_count2 < 2:
                    print('Best out of 3!')
                    time.sleep(2)
                    result = get_choice()
            else:
                print('You Win!!')
                time.sleep(2)
                win_count1 += 1
                
                if win_count1 < 2 and win_count2 < 2:
                    print('Best out of 3!')
                    time.sleep(2)
                    result = get_choice()
                    
        elif result[0] == 'paper':
            if result[1] == 'scissors':
                print('You Lose.')
                time.sleep(2)
                win_count2 += 1
               
                if win_count1 < 2 and win_count2 < 2:
                    print('Best out of 3!')
                    time.sleep(2)
                    result = get_choice()
            else:
                print('You Win!!')
                win_count1 += 1
                time.sleep(2)
                
                if win_count1 < 2 and win_count2 < 2:
                    print('Best out of 3!')
                    time.sleep(2)
                    result = get_choice()
                
        elif result[0] == 'scissors':
            if result[1] == 'rock':
                print('You Lose.')
                time.sleep(2)
                win_count2 += 1
                
                if win_count1 < 2 and win_count2 < 2:
                    print('Best out of 3!')
                    time.sleep(2)
                    result = get_choice()
            else:
                print('You Win!!')
                time.sleep(2)
                win_count1 += 1
                
                if win_count1 < 2 and win_count2 < 2:
                    print('Best out of 3!')
                    time.sleep(2)
                    result = get_choice()
            
                    
    print()
    print('Player Win Count:', win_count1)
    print('Opponent Win Count:', win_count2)
    print()
    
    if win_count1 > win_count2:
        time.sleep(3)
        print('You Win!!')
    else:
        time.sleep(3)
        print('You Lose')
        

print('*** Welcome To This, The Tenth Annual Universal Rock Paper Scissors Tournament!! ***')
time.sleep(3.7)
print("*** We Are All Set For the First Exciting Round to Commence!...                  ***")
time.sleep(3)
print()
print('Is The Player Ready?')
time.sleep(2)
print()
print("Enter 'y' to Start.")
print()
    
while True:
        
    start = input('>')
    if start == 'y':
        result = get_choice()
        break
    else:
        print(random.choice(incorrect_input_list))

while True:
    
    main()
    
    win_count1 = 0
    win_count2 = 0
    
    time.sleep(1)
    print()
    time.sleep(1)
    print("Press 'Enter' to Play Again. ('q' to quit) ")
    print()
    
    try_again = input('>')
    if try_again == 'q':
        break
    else:
        result = get_choice()
    