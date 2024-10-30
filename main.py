from art import logo
print(logo)

def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount =  bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"Congrats you won {winner} with a bid of INR {highest_bid}")


bids = {} # creating an empty dictionary where we can store the name,price
continue_bidding = True
while continue_bidding : # Creating a while loop so that we can tap into the value, comparing,printing and the key.
    name = input("Enter your name ? ")
    price = int(input("Enter your bid amount : INR  "))
    bids[name] = price
    should_continue = input("Are there any other bids type 'yes' to continue type 'no' ").lower()
    if should_continue == "no":
        should_continue = False
        highest_bidder(bids)
    elif should_continue =="yes": # If the user selects no moves to the next set
        print("\n" * 50)








