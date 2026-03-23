import random

# Welcome message to orientate the user
print("\nWelcome to your assigned voting booth human.... Read through the menu and type a selection below...")

# List of candidates prefilled, feel free to change this to make your own list
list_candidates = [
    "George Washington",
    "John Adams",
    "Thomas Jefferson",
    "James Madison",
    "James Monroe",
    "John Quincy Adams",
    "Andrew Jackson",
    "Martin Van Buren",
    "Henry Harrison",
    "John Tyler"

]

# Empty list for once the candidates are selected for election
election_candidates = []

vote_list = []

# Flag for if the program is running
is_running = True

# Loop to keep the program running
while True:

  # Menu options for the user to choose from
  print("-------------------------------------------")
  print("\n1. Continue with our selected candidates.")
  print("\n2. Enter your own candidates.")
  print("\n3. Exit the voting booth.")
  print("-------------------------------------------")

  # Getting user input for the options presented with input sanitation to handle unexpected values and errors
  try:
      menu_selection = int(input("Type 1, 2, or 3: "))
  except ValueError:
      print("-------------------------------------------")
      print("-------------------------------------------")
      print("****That is not a valid selection, try again****")
      print("-------------------------------------------")
      print("-------------------------------------------")

  # Logic for each of the menu options
  if menu_selection == 1: # Option 1 user enters two candidates

    # Two inputs to be stored in our empty list from earlier with input sanitation 
    first_canidate = input("Please enter your first candidate's name: ")
    election_candidates.append(first_canidate)

    second_canidate = input("Please enter your second candidate's name: ")
    election_candidates.append(second_canidate)

    # Random number to simulate binary voting
    random_num = random.randint(0,1)

    # Logic to convert the candidate list into numbers for random number conversion
    for i in range(len(list_candidates)):
        list_candidates[i] = vote_list.append(i)
        for i in vote_list:
            vote_list[i] = random.randint(0,1)

    print(vote_list)

    print(f"\nNow starting the race with these two candidates: {election_candidates}")
    print("Simulating the campaign trail...")
    print("Simulating the primaries...")
    print("Simulating the convenient lies...")
    print("Simulating election night...")
    print("And the winner is...")
 

    
    

    print("Menu option 1") # scaffolding
  elif menu_selection == 2:
    print("menu otion 2")
  elif menu_selection == 3:
    print("Exiting the program...")
    break

