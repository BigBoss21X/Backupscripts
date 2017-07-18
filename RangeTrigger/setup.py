import os

dir_path = os.path.dirname(os.path.realpath(__file__))
userrange = raw_input("What Range to send notification? (CM) ")
newrange = float("{0:.2f}".format(float(userrange)))
timetoread = int(raw_input("How long inbetween readings? (secs) "))
timetowrite = int(raw_input("How long inbetween write to Thingspeak? (secs) "))
thingkey = raw_input("Enter thingspeak key ")

with open(dir_path + "/config.txt", "w") as configfile:
    configfile.write(str(userrange) + "\n" + str(timetoread) + "\n" + str(timetowrite) + "\n" + str(thingkey) + "\n")
