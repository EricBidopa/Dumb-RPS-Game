import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper and 's' for scissors\n" )
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return "it's a tie"
    # r > s, s>p and p >r
    if isWin(user, computer):
        return "You won!"
    return "You Lost!"
    
def isWin(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    

print(play())
