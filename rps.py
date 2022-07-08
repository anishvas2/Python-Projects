import random
comp_inputs=[1,2,3]
inputs={1:'rock', 2:'paper' , 3:'scissors'}
name=input("Enter your name: ")
choice='yes'
while choice.lower()=='yes':
    user_choice=(input("Enter rock paper or scissors: ")).lower()

    if user_choice not in ['rock','paper','scissors']:
        continue
    comp_ran=random.choice(comp_inputs)
    comp_choice=inputs.get(comp_ran)
    print("%s selected: "%name)
    if(user_choice== 'rock'):
        print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)

    elif(user_choice== 'paper'):
        print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)

    else:
        print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)
    print("Computer selected: ")
    if(comp_choice== 'rock'):
        print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)

    elif(comp_choice== 'paper'):
        print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)

    else:
        print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)

    if(user_choice == comp_choice):
        print("***Tie***")

    elif((user_choice == 'rock' and comp_choice == 'scissors') or (user_choice == 'paper' and comp_choice == 'rock')or(user_choice == 'scissors' and comp_choice == 'paper')):
        print("***%s is the winner***"%(name))

    else:
        print("***Computer Wins***")

    choice=input("\n\n\n Want to play again (Yes or No)? : ")

