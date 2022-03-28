#8.fibonacci nim
print("RULES : /n 1.the first player will enter number of coins he wants to remove \n "
      "2.the next move must be less than or equal the double of the previous one, till the gamed ends \n"
      "3.the player takes last coin wins! \n"
      "4.each game starts with a random number of coins  ")
import random
n_coins = random.randint(10,100) #giving a random number of coins, maximum 100 so that the game does not take long
coins = int(n_coins)
print("the number of coins is:",coins)
while (coins !=0):
    print("player1 turn")
    player1 = (input())
    while not player1.isdigit():
        print("please enter a number ")
        player1 = (input())
    first_move = int(player1) #assiging the move as an integer to be able to compare its value in the next while loop
    while (first_move == coins) or (first_move> coins) or (first_move <= 0):
        print("play again,enter a valid number ")
        first_move = int(input())

    while not player1.isdigit():
        print("please enter a number")
        first_move = int(player1)
    coins = coins - first_move
    while (coins != 0):
        print("the number of coins is:",coins)
        print("player2 turn, you can pick up to",(int(player1) *2))
        player2= (input())
        while not player2.isdigit():
            print("please enter a number")
            player2 = (input())
        second_move = int(player2)
        while (second_move > (int(player1)*2)) or (second_move <= 0) or (second_move > coins) :
            print("play again,enter a valid number ")
            second_move = int(input())
        player2 = second_move
        while (player2 == coins ):
            print("player2 won,CONGRATULATIONS!")
            exit()
        coins = coins - player2
        print("the number of coins is :",coins)
        print("player1 turn, you can pick up to ",((int(player2))*2))
        player1 = int(input())
        while (player1 > int(player2)*2) or (player1 <= 0) or (player1 > coins):
            print("play again,enter a valid number")
            player1 = int(input())
        if (player1 == coins):
            print("player1 won ,CONGRATULATIONS!")
            exit()
        coins = coins - player1