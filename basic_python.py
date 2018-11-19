##basic python mathmatics
name = ""
bool = "true"
while bool == "true":
    print("What is your name")
    name = raw_input()
    nameLow = name.lower()
    if nameLow == "shiloh":
	print("I love you Shiloh")
    elif nameLow == "theresa" or  nameLow == "mom" or nameLow == "terri":
	print("You are the best Mom ever")
    elif nameLow == "cj" or nameLow ==  "christopher":
	print("Hello Brother")
    elif nameLow == "patrick" or nameLow == "dad" or nameLow == "pat":
	print("Thank you for all that you do")
    else:
	print("I do not know you")
    print("Press 1 if you are finished")
    x = raw_input()
    if x == "1":
	print("Goodbye " +  nameLow)
	bool = "false"
    else:
	print("Lets go again")

