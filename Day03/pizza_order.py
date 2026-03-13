print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

#if size == "S":
 #   bill = 15
  #  print("You picked a S pizza")
   # if pepperoni == "Y":
    #    bill += 2
     #   print("You added pepperoni")
    #else:
     #   print("No pepperoni")
    #if extra_cheese == "Y":
     #   bill += 1
      #  print("You added extra cheese")
    #else:
     #   print("No extra cheese")
#elif size =="M":
 #   bill = 20
  #  print("You picked a M pizza")
   # if pepperoni == "Y":
    #    bill += 3
     #   print("You added pepperoni")
   # else:
    #    print("No pepperoni")
    #if extra_cheese == "Y":
     #   bill +=1
      #  print("You added extra cheese")
    #else:
     #   print("No extra cheese")
#else:
 #   bill = 25
  #  print("You picked a L pizza")
   # if pepperoni == "Y":
    #    bill += 3
     #   print("You added pepperoni")
    #else:
     #   print("No pepperoni")
    #if extra_cheese == "Y":
     #   bill += 1
      #  print("You added extra cheese")
    #else:
     #   print("No extra cheese")
#print(f"Your final bill is {bill}")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size  == "L":
    bill += 25
else:
    print("Not a valid input")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
