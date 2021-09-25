with open("artifacts01.txt", "r") as fi:
     with open("artifacts02.txt", "w") as fo:
         fo.write(fi.read())
print("End of last stage")