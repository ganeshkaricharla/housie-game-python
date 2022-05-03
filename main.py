import generateTicket
import gameNum
n=int(input('Enter number of Players'))
playerList = []
for i in range(n):
    print("Enter Player {} name :".format(i+1))
    playerList.append(input())

for i in range(n):
    print("ticket  Generated for {} :".format(playerList[i]))
    generateTicket.gene()

gameNum.pickNum()


