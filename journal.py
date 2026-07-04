greeting  = "Hey! , What happened today ? "
print( greeting )
response = input()
file = open("journal.txt","a")
file.write("---------" + "\n" + response + "\n")
file.close()
