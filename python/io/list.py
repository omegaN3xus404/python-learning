f=open("list.txt")
# this red the line from 1 line to last line
lines=f.readlines()
print(lines,type(lines))
f.close()