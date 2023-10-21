import random
bet=int(input("Your bet between 1 to 10"))
lucky_draw=random.randint(1,10)
print(lucky_draw)
account=0
if bet==lucky_draw:
    account=account+900-100
else:
    account=account-100
print(account)