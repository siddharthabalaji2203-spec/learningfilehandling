greeting  = "Hey! , What happened today ? "
print( greeting )
response = input()
with open("journal.txt","a") as file:
    file.write("---------" + "\n" + response + "\n")

