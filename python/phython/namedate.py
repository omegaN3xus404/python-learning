name = input("enter the name of the person ")
d = input("enter the date of the letter ")
lettel = "dear <name>\n your selected date \ntime"
print(lettel.replace("<name>",name).replace("date",d))
          
