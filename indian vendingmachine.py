cost = eval(input("Enter the cost (in Rands): "))
dep = 0
while dep < cost:
  dep = dep + eval(input("Deposit a coin or note (in Rand): "))
print("Your change is:")
change = dep - cost
if change >= 50:
  fifty = change // 50
  print("{0} x R50".format(fifty))
  change = change - fifty * 50
if change >= 20:
  twenty = change // 20
  print("{0} x R20".format(twenty))
  change = change - twenty * 20
if change >= 10:
  ten = change // 10
  print("{0} x R10".format(ten))
  change = change - ten * 10
if change >= 5:
  five = change // 5
  print("{0} x R5".format(five))
  change = change - five * 5
if change >= 2:
  two = change // 2
  print("{0} x R2".format(two))
  change = change - two * 2
if change >= 1:
  one = change
  print("{0} x R1".format(one))