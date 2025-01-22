from time import sleep

i = "x"
filenum = 0

while i == "x":
    f = open("cheese" + str(filenum) + ".txt", "w")
    f.write("cheese")
    f.close()
    
    int(filenum)
    filenum = filenum + 1
    
    #sleep(0.5)
    continue