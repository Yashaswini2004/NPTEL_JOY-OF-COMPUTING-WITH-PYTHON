def rock_paper(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3234
    p2=int(num2[bit2])%3
    if player_1[p1] == player_2[p2]:
        print("Its a draw")
    elif player_1[p1]=="rock" and player_2[p2]=="scissor":
        print("player 1 win..!")
    elif player_1[p1]=="rock" and player_2[p2]=="paper":
        print("player 2 win..!")
    elif player_1[p1]=="paper" and player_2[p2]=="scissor":
        print("player 2 win..!")
    elif player_1[p1]=="scissor" and player_2[p2]=="rock":
        print("player 2 wins...!")
    elif player_1[p1]=="paper" and player_2[p2]=="rock":
        print("player 1 wins...!")
    elif player_1[p1]=="scissor" and player_2[p2]=="paper":
        print("player 1 wins...!")        
player_1={0:"rock",1:"paper",2:"scissor"}
player_2={0:"paper",1:"rock",2:"scissor"}
while True:
    num1=input("Player1 enter your input:")
    num2=input("Player2 enter your input:")
    bit1=int(input("player1 enter secret bit position"))
    bit2=int(input("player2 enter secret bit position"))
    rock_paper(num1,num2,bit1,bit2)
    ch=input("Do you want to continue?y/n")
    if ch=='n':
        break