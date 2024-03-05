user_name = input("what is your name? ")
user_age = int(input("How old are you? "))
print (f"Hello {user_name}")
if user_age <= 15:
    print("woah, you are young")
elif user_age <= 25:
    print("Hitting your prime")
elif user_age <= 40:
    print("Becoming wise")
else:
    print("you are a wise old man")