from time import sleep

i = "x"
filenum = 0

print("Please ensure this file is in a folder without any files already named cheese.")
start = input("Do you wish to commence the cheese? y/n\n")

if start == "y":
    while i == "x":
        f = open("cheese" + str(filenum) + ".txt", "w")
        f.write("cheese")
        f.close()
    
        int(filenum)
        filenum = filenum + 1
    
        #sleep(0.5)
        continue
    
else:
    exit()