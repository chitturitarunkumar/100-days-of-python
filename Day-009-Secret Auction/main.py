logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
def highest_bidder(bits):
    winner = ""
    highest_bid = 0
    for key in bits:
        if bits[key] > highest_bid:
            highest_bid = bits[key]
            winner = key
    print(f"{winner} is highest bid {highest_bid}")
bits = {}
continue_bidding = True
while continue_bidding:
    name = input("Enter your name: ")
    price = int(input("what is your bit? $ "))
    bits[name] = price
    should_continue = input("Are there any other bitters? Type 'yes' to continue or 'no': ").lower()
    if should_continue == "no":
        continue_bidding = False
        highest_bidder(bits)
    elif should_continue == "yes":
        print("\n" * 20)



