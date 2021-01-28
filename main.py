from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art 
print(art.logo)

storage = []

def play():
	for x in range(1):
		in_dictionary = {}
		in_dictionary["name"] = input("What is your name? ")
		in_dictionary["money"] = int(input("How much are you bidding? $"))
		storage.append(in_dictionary)

		# What makes the function repeat
		go_again = input("Is there anyone else bidding? y / n: ")

		while go_again != "y" and go_again != "n":
			go_again = input("Invalid Input, Please answer y / n: ")

		if go_again == "y":
			clear()
			print(art.logo)
			play()
		elif go_again == "n" :
			max_money = []
			for x in range(0, len(storage)):
				max_money.append(storage[x]["money"])
			largest_bid = max(max_money)

			who_has_max = max_money.index(largest_bid)
			name_of_who_has_max = storage[who_has_max]["name"]
			money_of_the_max_bid = storage[who_has_max]["money"]
			print(f"The winner with the highest bid is {name_of_who_has_max} with a bid of ${money_of_the_max_bid}")
			break;

play()

