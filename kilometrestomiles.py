#convert kilometers to miles
kilometers=float(input("Enter distance in kilometers : "))
#converstion factor : 1 kilometer = 0.621371 miles
converstion_factor=0.621371
miles=kilometers*converstion_factor
print(f"{kilometers} kilometers is equals to {miles} miles")