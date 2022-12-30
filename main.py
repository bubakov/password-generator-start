#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# random choice from letters
user_letters = ''
for letter in range(nr_letters):
  random_letters = random.choice(letters)
  # it append chosen string to variable user_letters
  user_letters += random_letters
# print(user_letters)
# random choice from symbols
user_symbols = ''
for symbol in range(nr_symbols):
  random_symbols = random.choice(symbols)
  # it append chosen string to variable user_symbols
  user_symbols += random_symbols
# print(user_symbols)
# random choice from numbers
user_numbers = ''
for number in range(nr_numbers):
  random_number = random.choice(numbers)
  # it append chosen string to variable user_symbols
  user_numbers += random_number
# print(user_numbers)
# f-string print all variables together. It is our password
print(f"{user_letters}{user_symbols}{user_numbers}")
  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#help variables
ranked_password = user_letters + user_symbols + user_numbers
#retype variable ranked_password
ranked_password_list = list(ranked_password)
#control prints
# print(ranked_password)
# print(ranked_password_list)

result = ''
# random choice from ranked_password list without repetitions, possible to use shuffle(ranked_password_list)
random_password = random.sample(ranked_password_list, nr_letters + nr_symbols + nr_numbers)
# loop for final password with chosen randomised characters
for character in random_password:
  result += character

# print(random_password)
print(f"Your password is: {result}")