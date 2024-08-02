# Function to calculate love score
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lowercase_name = combined_names.lower()

    t = lowercase_name.count("t")
    r = lowercase_name.count("r")
    u = lowercase_name.count("u")
    e = lowercase_name.count("e")
    true_sum = t + r + u + e

    l = lowercase_name.count("l")
    o = lowercase_name.count("o")
    v = lowercase_name.count("v")
    e = lowercase_name.count("e")
    love_sum = l + o + v + e

    love_score = int(str(true_sum) + str(love_sum))
    return love_score


# Main loop to ask for names and calculate score
while True:
    print("The Love Calculator is calculating your score...")

    name1 = input("What is your name? ")
    name2 = input("What is their name? ")

    love_score = calculate_love_score(name1, name2)

    if love_score < 10 or love_score > 90:
        print(f"Your score is {love_score}, you go together like coke and mentos.")
    elif 40 <= love_score <= 50:
        print(f"Your score is {love_score}, you are alright together.")
    else:
        print(f"Your score is {love_score}.")

    # Ask if the user wants to calculate another score
    play_again = input("Do you want to calculate another score? Type 'yes' or 'no':\n").lower()
    if play_again != 'yes':
        print("Thanks for using the Love Calculator!")
        break
