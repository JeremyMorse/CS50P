#Version 2
def hello(to="world"):
    print("Hello", to)

def main():
    name = input ("What's your name? ")
    hello(f"{name}")

main()

#VERSION 1
#Ask for name, strip, and title
#name = input ("What's your name? ").strip().title()



#Split users name into first + last
#name = name.split(" ")

#Say "Hello" to user
#print ("hello," + " " + name)
#-
#print ("hello,", name)
#-
#print ("hello, ", end="")
#print(name)
#-
#print (f"hello, {name}")


#Cornercase: quotes in quotes
#print ("hello, \"friend\"")
#-
#print ("hello, 'friend'")