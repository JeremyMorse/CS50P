#Ask for name, strip, and title
name = input ("What's your name? ").strip().title()

#Say "Hello" to user
#print ("hello," + " " + name)
#-
#print ("hello,", name)
#-
#print ("hello, ", end="")
#print(name)
#-
print (f"hello, {name}")


#Cornercase: quotes in quotes
#print ("hello, \"friend\"")
#-
#print ("hello, 'friend'")