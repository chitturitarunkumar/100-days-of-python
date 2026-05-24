import random

logo = """
 _   _ _       _               
| | | (_) __ _| |__   ___ _ __ 
| |_| | |/ _` | '_ \\ / _ \\ '__|
|  _  | | (_| | | | |  __/ |   
|_| |_|_|\\__, |_| |_|\\___|_|   
         |___/                 
"""

vs = """
__   _____
\\ \\ / / __|
 \\ V /\\__ \\
  \\_/ |___/
"""

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country': 'India'
    }
]


def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)

score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(
        guess,
        a_follower_count,
        b_follower_count
    )

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
