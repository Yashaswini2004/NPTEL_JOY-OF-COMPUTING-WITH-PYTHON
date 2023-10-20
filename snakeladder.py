from PIL import Image
import random
end=100
def show_board():
    image=Image.open(r'C:\NPTEL_PYTHON\board.jpg')
    image.show()
def check_ladder(points):
    if points==3:
        print('Ladder')
        return 20
    elif points==6:
        print('Ladder')
        return 14
    elif points==11:
        print('Ladder')
        return 28
    elif points==15:
        print('Ladder')
        return 34
    elif points==17:
        print('Ladder')
        return 74
    elif points==22:
        print('Ladder')
        return 37
    elif points==49:
        print('Ladder')
        return 67
    elif points==57:
        print('Ladder')
        return 76
    elif points==61:
        print('Ladder')
        return 78
    elif points==73:
        print('Ladder')
        return 86
    elif points==81:
        print('Ladder')
        return 98
    elif points==88:
        print('Ladder')
        return 91
    else:
        return points
def check_snake(points):
    if points==18:
        print("snake")
        return 1
    elif points==8:
        print("snake")
        return 4
    elif points==39:
        print("snake")
        return 5
    elif points==51:
        print("snake")
        return 6
    elif points==26:
        print("snake")
        return 10
    elif points==59:
        print("snake")
        return 17
    elif points==64:
        print("snake")
        return 36
    elif points==69:
        print("snake")
        return 33
    elif points==73:
        print("snake")
        return 1
    elif points==83:
        print("snake")
        return 19
    elif points==92:
        print("snake")
        return 51
    elif points==95:
        print("snake")
        return 24
    elif points==98:
        print("snake")
        return 28
    else:
        return points
def reached_end(points):
    if points==end:
        return True
    else:
        return False    
def play():
    p1_name=input("Player1 please enter your name:")
    p2_name=input("Player2 please enter your name:")
    pp1=0
    pp2=0
    turn=0
    while(1):
        if turn%2==0:
            print(p1_name,'This is your turn')
            c=input("Enter 1 continue and 0 to quick")
            if c==0:
                print(p1_name, 'scored:' ,pp1)
                print(p2_name, 'scored:' ,pp2)
                print("Quitting game,thanks for playing!!!")
                break
            dice=random.randint(1,6)
            print('dice showed', dice)
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if pp1>end:
                pp1=end
            print(p1_name,'Your score is:',pp1)
            if reached_end(pp1):
                print(p1_name, 'won')
                break
        else:
            print(p2_name,'This is your turn')
            c=input("Enter 1 continue and 0 to quick")
            if c==0:
                print(p1_name, 'scored:' ,pp1)
                print(p2_name, 'scored:' ,pp2)
                print("Quitting game,thanks for playing!!!")
                break
            dice=random.randint(1,6)
            print('dice showed', dice)
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if pp2>end:
                pp2=end
            print(p2_name,'Your score is:',pp2)
            if reached_end(pp2):
                print(p2_name, 'won')
                break
        turn=turn+1
show_board()
play()