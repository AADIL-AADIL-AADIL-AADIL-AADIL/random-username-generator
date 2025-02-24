import random

#Predefined adjectives and nouns.

adjectives = ["Crazy","Cool","Brave","Bold", "Fierce", "Smart", "Radiant", "Mystic", "Lone" , "Stoic"]
nouns = ["Warrior","Knight", "Dragon", "Beast","King","Captain","Hero"]

# Function to generate usernames.

def generate_username(include_numers,include_char,length):
   adjective = random.choice(adjectives)
   noun = random.choice(nouns)

   username = adjective + noun 

   # for including numbers

   if include_numers :
      username += str(random.randint(0,99))

   # for including special characters

   if include_char:
      char = ["!","@","#","$","&","*"]
      username += str(random.choice(char))   

   if length and len(username) > length:
     username = username[:length]

   return username
 
 #Function to save a username

def save_usernames(usernames,filename = "username.txt"):
  file = open(filename, "w")
  for username in usernames:
     file.write(username + "\n")
     file.close()
     print(f"Your username has been saved to {filename}")
     


# Main function

def main ():
  
  print("Welcome to random username generator!!")
  
  include_numbers = input("Would you like to include numbers? [Y/N] : ").upper() == "Y"
  include_char = input("Would you like to include special characters? [Y/N] : ").upper() == "Y"
  length = input("Set a length for your username [leave blank for no limit] : ")
  length = int(length) if length.isdigit() else None

# Generate username

  usernames = [generate_username(include_numbers, include_char, length) ]

# Generated username

  print("\nYour Generated Username is : ")
  for username in usernames :
    print(username)


# Saving the usernames to a file
    save_option = input("\nWould you like to save the usernames to a file? [Y/N]: ").upper() == "Y"
    if save_option:
        save_usernames(usernames)

# Run the program

if __name__ == "__main__":
    main()

