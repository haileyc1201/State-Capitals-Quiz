import random

#Names: Hailey Clark and Lexi Nguyen (Group 1, Lab 3)
#Date: 2/13/24 
#This program is a game where the user is quizzed on their knowledge of state capitals. 

def read_file(file_name):
  '''Reads each line in text file to add the state and capital to a 2D list. '''
  #Opening text file with state and corresponding capital pairs on each line
  file = open(file_name, "r")

  #Making a 2D list to store the state and capital pairs + filling it from the text file
  states = []
  for row in file:
      items = row.split(",")
      list = []
      for item in items:
          list.append(item)
      states.append(list)
  return states
  
def get_random_state(states):
  '''Returns a random state + capital pair from the whole state list.'''
  #Randomly selecting a number between 0 and 49, inclusive
  random_num = random.randint(0, len(states)-1)
  state = states[random_num]
  #Returning state from that index
  return state
  
def get_random_choices(states, correct_capital):
  '''Returns a set of 4 capital choices, 3 randomly chosen and 1 correct choice.'''
  #Initializing a list and adding the correct capital choice to it
  choices = []
  choices.append(correct_capital)
  i = 0
  #Adding three other random capital
  while i < 3:
    unique = True
    random_pair = get_random_state(states)
    random_capital = random_pair[1]
    #If matches another answer, it's not added and an additional iteration will be made
    for i in range (len(choices)):
       if (random_capital==choices[i]):
         unique = False
    #Added if it doesn't match
    if unique:
      choices.append(random_capital)
      i += 1

  #Returning list of shuffled capital answer choices
  random.shuffle(choices)
  return choices
  
def ask_question(correct_state, possible_answers):
  '''Asks the user what the capital of a random state is and gives 4 options'''
  #Printing the question and possible answers
  print("The capital of", correct_state, " is: \n")
  alphabet = ["  A. ", "  B. ", "  C. ", "  D. "]
  valid_inputs = ["A", "B", "C", "D"]    
  
  #Adding the letter choices to the start of answer choices and printing
  for index in range(4): 
    print(alphabet[index],  possible_answers[index])

  #Getting user input for answer choice and check if it is valid
  user_input = input("Enter Selection: ").upper()
  while ((user_input.isalpha() is False) or (len(user_input) != 1) or (user_input not in valid_inputs)):
    print("Invalid input. Input choices A-D.")
    user_input = input("Enter Selection: ").upper()
  
  if user_input == "A":
    return 0
  elif user_input == "B":
    return 1
  elif user_input == "C":
    return 2
  else: 
    return 3

def main():
  rep = True
  while (rep is True):
    #Question number starts at 1 and user points starts at 0. File is read. 
    current_num_Q = 1 
    user_points = 0 
    states_list = read_file("statecapitals.txt")

    #Quiz begins. 
    print("- State Capital Quiz - \n")
    
    #Quiz continues until user has answered question 10. 
    streak = 0
    longest_streak = 0
    while current_num_Q <= 10:
      #Quiz chooses a random state and its capital that will be the correct answer. 
      correct_pair = get_random_state(states_list)
      states_list.remove(correct_pair)
      correct_state = correct_pair[0]
      correct_capital = correct_pair[1]

      #Quiz gets random answer choices
      capital_choices = get_random_choices(states_list, correct_capital)
      print(str(current_num_Q)+ ". ", end = ""),
      user_number = ask_question(correct_state, capital_choices)

      #Counts longest streak and how many correct answers user got. 
      if correct_capital == capital_choices[user_number]:
        print("Correct! \n")
        user_points += 1
        streak +=1
      #Reveals correct answer and resets streak if user chooses incorrect choice
      else: 
        print("Incorrect! The correct answer is: ", correct_capital, "\n" )
        if streak > longest_streak:
          longest_streak = streak
        streak = 0
        
      #Current question number is increased.   
      current_num_Q += 1
      
    #Updates streak   
    if streak > longest_streak:
      longest_streak = streak
    streak = 0

    #End of test after 10 Qs, reveals how many correct answers user has and streak. 
    print("End of test. You got ", str(user_points), "/10 correct. Your longest streak was", str(longest_streak), ". \n" )
    
    #Prints message based on how many correct choices user has. 
    if user_points >= 8:
      print("Congratulations! You are a state capitals master! \n")
    else:
      print("Keep trying, you can do it! Aim for an 8/10 next time. \n")

    #Asking user if they want to play again.
    repStr = input("Would you like to play again? (Y/N): ").upper()
    while (repStr != "Y" and repStr != "N"):
      repStr = input("Hmm... That wasn't a Y or an N. Would you like to play again? Y for yes or N for no: ").upper()
    if repStr == "Y":
      rep = True
      print("Great! Good luck! \n")
    else:
      rep = False
      print("Thanks for playing! \n")
      
main()