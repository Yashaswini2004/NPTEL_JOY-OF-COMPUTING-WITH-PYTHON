import random
account=0
for i in range(365):
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    #print("Bet:",bet)
    #print("Lucky draw:",lucky_draw)
    if bet==lucky_draw:
        account=account+900-100
    else:
        account=account-100
print("YOUR ACCOUNT BALANCE:",account)