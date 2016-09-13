from random import randint
from random import random
from time import sleep
print ""
print "Welcome to roulette!"
#numbersdic = {1 : "red", 2 : "black"} probs won't even need
number_dic = {0 : "green", 1 : "red", 2 : "black", 3 : "red", 4 : "black", 5 : "red", 6 : "black", 7 : "red", 8 : "black", 9 : "red", 10 : "black", 11 : "black", 12 : "red", 13 : "black", 14 : "red", 15 : "black", 16 : "red", 17 : "black", 18 : "red", 19 : "red", 20 : "black", 21 : "red", 22 : "black", 23 : "red", 24 : "black", 25 : "red", 26 : "black", 27 : "red", 28 : "black", 29 : "black", 30 : "red", 31 : "black", 32 : "red", 33 : "black", 34 : "red", 35 : "black", 36 : "red"}
def get_user_spot():
    user_continue = True
    user_bank = 100
    while user_continue == True:
        print ""
        if user_bank == 0:
            sleep(1)
            print "Sorry! You've gone bankrupt! Your balance is now at $0. Thanks for the money though..."
            sleep(2)
            print "quitting"
            sleep(.5)
            user_continue = False #making sure user has more than $0
        else:
            user_spot = raw_input("Where would you like to place your chips. You may choose one spot on the roulette board. Type 'n' if you want to bet on a specific number, 'odd' or 'even' if you want to bet on all odd numbers or even numbers, 'red' or 'black' if you want to bet on all red numbers or black numbers, '12' if wou want to bet on the first, second, or third third of the board, or type 'leave' to leave the table:  ")
            print ""
            print "Your selection is " + user_spot
            if user_spot == "leave":
                print ""
                print "Summary:"
                sleep(.5)
                print "Good job. You have ended with $" + str(user_bank) + " in your bank. Net profit = $" + str(user_bank - 100) + ". Thanks for playing..."
                sleep(3)
                print ""
                print "quitting..."
                user_continue = False #checking if user wants to leave
            else:
                confirm  = raw_input("Is that ok? (y/n):  ")
                if confirm != "y":
                    continue #confirming user wants to bet on "user_spot"
                else:
                    print ""
                    print "Your current balance is $" + str(user_bank)
                    user_bet = raw_input("How much would you like to bet?: $")
                    user_bet = int(user_bet)
                    if user_bet > user_bank or user_bet <= 0: #makeing sure bet does not exceed bank and is over 0
                        print "You cannot bet $" + str(user_bet) + "."
                        #user_continue = False
                        continue
                    else:
                        print ""
                        print "Are you sure you would like to bet $" + str(user_bet)
                        bet_confirm = raw_input("Confirm (y/n):  ")
                        if bet_confirm != "y":
                            continue #making sure that user is ok with betting $x
                        else: #under this "else" is all the betting math
                            rand_roll_number = randint(0,36)
                            rand_roll_color = number_dic[rand_roll_number]
                            if user_spot == "n":
                                user_number = int(raw_input("Pick any number 0-36: "))
                                if user_number in range(0, 36):
                                    user_odds = 36
                                    print "Your odds are 1 in 36"
                                    sleep(.2)
                                    print "Spinning..."
                                    sleep(.2)
                                    print "Three..."
                                    sleep(1)
                                    print "Two..."
                                    sleep(1)
                                    print "One..."
                                    sleep(1)
                                    print ""
                                    print "---> " + str(rand_roll_number) + " " + rand_roll_color + " <---"
                                    print ""
                                    if user_number == rand_roll_number:
                                        user_bank += user_bet * (user_odds - 1)
                                        print "YOU WON!!!"
                                        sleep(.5)
                                        print "$" + str(user_bet * (user_odds - 1)) + " has been added to your bank!"
                                        print "New bank sum: $" + str(user_bank)
                                    else:
                                        user_bank = user_bank - user_bet
                                        print "You lost."
                                        sleep(.5)
                                        print "$" + str(user_bet) + " has been taken from your bank."
                                        print "New bank sum: $" + str(user_bank)
                                        continue
                            elif user_spot == "12":
                                print ""
                                user_third = raw_input("What third of the board would you like to bet on? ('1st'/'2nd'/'3rd'):  ")
                                print user_third
                                if user_third == "1st" or user_third == "2nd" or user_third == "3rd":
                                    if rand_roll_number in range(1, 12):
                                        computer_third = "1st"
                                        user_odds = 3
                                        print "Your odds are 1 in 3"
                                        sleep(.2)
                                        print "Spinning..."
                                        sleep(.2)
                                        print "Three..."
                                        sleep(1)
                                        print "Two..."
                                        sleep(1)
                                        print "One..."
                                        sleep(1)
                                        print ""
                                        print "---> " + str(rand_roll_number) + " " + rand_roll_color + " <---"
                                        print ""
                                        if user_third == computer_third:
                                            user_bank += user_bet * (user_odds - 1)
                                            print "YOU WON!!!"
                                            sleep(.5)
                                            print "$" + str(user_bet * (user_odds - 1)) + " has been added to your bank!"
                                            print "New bank sum: $" + str(user_bank)
                                        else:
                                            user_bank -= user_bet
                                            print "You lost."
                                            sleep(.5)
                                            print "$" + str(user_bet) + " has been taken from your bank."
                                            print "New bank sum: $" + str(user_bank)
                                    elif rand_roll_number in range(13, 24):
                                        computer_third = "2nd"
                                        user_odds = 3
                                        print "Your odds are 1 in 3"
                                        sleep(.2)
                                        print "Spinning..."
                                        sleep(.2)
                                        print "Three..."
                                        sleep(1)
                                        print "Two..."
                                        sleep(1)
                                        print "One..."
                                        sleep(1)
                                        print ""
                                        print "---> " + str(rand_roll_number) + " " + rand_roll_color + " <---"
                                        print ""
                                        if user_third == computer_third:
                                            user_bank += user_bet * (user_odds - 1)
                                            print "YOU WON!!!"
                                            sleep(.5)
                                            print "$" + str(user_bet * (user_odds - 1)) + " has been added to your bank!"
                                            print "New bank sum: $" + str(user_bank)
                                        else:
                                            user_bank -= user_bet
                                            print "You lost."
                                            sleep(.5)
                                            print "$" + str(user_bet) + " has been taken from your bank."
                                            print "New bank sum: $" + str(user_bank)
                                    elif rand_roll_number in range(25, 36):
                                        computer_third = "3rd"
                                        user_odds = 3
                                        print "Your odds are 1 in 3"
                                        sleep(.2)
                                        print "Spinning..."
                                        sleep(.2)
                                        print "Three..."
                                        sleep(1)
                                        print "Two..."
                                        sleep(1)
                                        print "One..."
                                        sleep(1)
                                        print ""
                                        print "---> " + str(rand_roll_number) + " " + rand_roll_color + " <---"
                                        print ""
                                        if user_third == computer_third:
                                            user_bank += user_bet * (user_odds - 1)
                                            print "YOU WON!!!"
                                            sleep(.5)
                                            print "$" + str(user_bet * (user_odds - 1)) + " has been added to your bank!"
                                            print "New bank sum: $" + str(user_bank)
                                        else:
                                            user_bank -= user_bet
                                            print "You lost."
                                            sleep(.5)
                                            print "$" + str(user_bet) + " has been taken from your bank."
                                            print "New bank sum: $" + str(user_bank)
                                    else:
                                        print "Your odds are 1 in 3"
                                        sleep(.2)
                                        print "Spinning..."
                                        sleep(.2)
                                        print "Three..."
                                        sleep(1)
                                        print "Two..."
                                        sleep(1)
                                        print "One..."
                                        sleep(1)
                                        print ""
                                        print "---> " + "0" + " " + "green" + " <---"
                                        print ""
                                        if user_third == computer_third:
                                            user_bank += user_bet * (user_odds - 1)
                                            print "YOU WON!!!"
                                            sleep(.5)
                                            print "$" + str(user_bet * (user_odds - 1)) + " has been added to your bank!"
                                            print "New bank sum: $" + str(user_bank)
                                        else:
                                            user_bank -= user_bet
                                            print "You lost."
                                            sleep(.5)
                                            print "$" + str(user_bet) + " has been taken from your bank."
                                            print "New bank sum: $" + str(user_bank)
                                else:
                                    continue
                            elif user_spot == "odd" or user_spot == "even":
                                user_odds = 2
                                print "Your odds are 1 in 2"
                                sleep(.2)
                                print "Spinning..."
                                sleep(.2)
                                print "Three..."
                                sleep(1)
                                print "Two..."
                                sleep(1)
                                print "One..."
                                sleep(1)
                                print ""
                                print "---> " + str(rand_roll_number) + " " + rand_roll_color + " <---"
                                print ""
                                if user_spot == "even" and (rand_roll_number % 2) == 0:
                                    user_bank += user_bet * (user_odds - 1)
                                    print "YOU WON!!!"
                                    sleep(.5)
                                    print "$" + str(user_bet * (user_odds - 1)) + " has been added to your bank!"
                                    print "New bank sum: $" + str(user_bank)
                                elif user_spot == "odd" and (rand_roll_number % 2) != 0:
                                    user_bank += user_bet * (user_odds - 1)
                                    print "YOU WON!!!"
                                    sleep(.5)
                                    print "$" + str(user_bet * (user_odds - 1)) + " has been added to your bank!"
                                    print "New bank sum: $" + str(user_bank)
                                else:
                                    user_bank -= user_bet
                                    print "You lost."
                                    sleep(.5)
                                    print "$" + str(user_bet) + " has been taken from your bank."
                                    print "New bank sum: $" + str(user_bank)
                                    #elif user_spot == "odd" or user_spot == "even":
                            elif user_spot == "red" or user_spot == "black":
                                user_odds = 2
                                print "Your odds are 1 in 2"
                                sleep(.2)
                                print "Spinning..."
                                sleep(.2)
                                print "Three..."
                                sleep(1)
                                print "Two..."
                                sleep(1)
                                print "One..."
                                sleep(1)
                                print ""
                                print "---> " + str(rand_roll_number) + " " + rand_roll_color + " <---"
                                print ""
                                #user_spot = user_spot[0]
                                if user_spot == rand_roll_color:
                                    user_bank += user_bet * (user_odds - 1)
                                    print "YOU WON!!!"
                                    sleep(.5)
                                    print "$" + str(user_bet * (user_odds - 1)) + " has been added to your bank!"
                                    print "New bank sum: $" + str(user_bank)
                                else:
                                    user_bank -= user_bet
                                    print "You lost."
                                    sleep(.5)
                                    print "$" + str(user_bet) + " has been taken from your bank."
                                    print "New bank sum: $" + str(user_bank)
get_user_spot()
