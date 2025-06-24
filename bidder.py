def winner(bidder_details):
    highest_bid = 0
    winner=""
    for bidder in bidder_details:
        bidder_price = bidder_details[bidder]
        if bidder_price>highest_bid:
            highest_bid=bidder_price
            winner=bidder
    print(f"winner is {winner}")

bidder_list={}
while True:
    name = input("enter the name:\n")
    price = int(input("enter your price:\n"))
    bidder_list[name] = price
    more = input('are there more bidders? type yes or no').lower()
    if more=='no':
        winner(bidder_list)
        break


