Greeting  = " Hey! , What happened today ? "
print( Greeting )
response = input()
file = open("journal.txt","a")
add = file.write(response)
file.close()
