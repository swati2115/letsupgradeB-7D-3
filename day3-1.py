s=int(input("enter the altitude in ft:"))
if s<=1000:
	print("SAFE TO LAND")
elif s<=4500:
	print("COME DOWN TO 1000ft")
else:
	print("GO AROUND AND TRY LATER")
