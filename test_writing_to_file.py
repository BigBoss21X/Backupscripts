
f= open("/home/pi/scripts/workfile.txt", "a")

j=raw_input("Enter what to write to workfile: ")

f.write(j + "\n")
