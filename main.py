print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly? \n")
ans1 = input("What language are we writing in? ")
if ans1 == "python":
  print("Correct\n")
else:
  print("Nope🙈\n")

ans2 = int(input("Which lesson number is this? "))
if (ans2 > 12):
  print("We're not quite that far yet ")
elif (ans2 == 12):
  print("That's right!")
else:
  print("We've gone well past that!")


