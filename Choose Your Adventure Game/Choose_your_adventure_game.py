def main():
  name = input("Type your name: ")
  print("Welcome", name, "to this adventure game!")

  answer = input("\nRoad ends...\n\nChose your path (left/right) ").lower()
  if answer == "left":
      answer = input(
          "You came to a river...\nChoose your path (swim/walk) ").lower()

      if answer == "swim":
          print("\n\nYou swim acrross the river and you eaten by the shark....\n\n!!! YOU LOST THE GAME !!!")
      elif answer == "walk":
          print("You walked for many miles, ran out of water...\n\n!!! YOU LOST THE GAME !!!")
      else:
          print('Not a valid option. You lose.')

  elif answer == "right":
      answer = input(
          "\nYou come to a bridge...\nChoose your path(cross/back)? ").lower()

      if answer == "back":
          print("You went back...\n\n!! YOU LOST THE GAME !!!")
      elif answer == "cross":
          answer = input(
              "\nYou cross the bridge and you see your teacher...\nDo you like to talk to them? (yes/no) ").lower()

          if answer == "yes":
              print("\nYou talked to the teacher...\n\n!!! YOU WON THE GAME !!!")
          elif answer == "no":
              print("\nYou ignored your techaer...\n\n!!! YOU LOST THE GAME !!!")
          else:
              print('Not a valid option. You lose.')
      else:
          print('Not a valid option. You lose.')

  else:
      print('Not a valid option. You lose.')

  print("\n\nGood try \U0001f600", name)
main()