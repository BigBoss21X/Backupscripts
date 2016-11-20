from time import sleep
#from shutil import copyfile
import os
#path
filename = "/home/pi/Documents/temp_temp.txt"
#newfilename = "/home/pi/Documents/temp_temp2.txt"
avgfile = open("/home/pi/Documents/last_ten_average_temp.txt","w")


def read():
    with open(filename,"r") as infile:
        try:
            data = [float(n) for n in infile.read().split()]
            lasttendata = data[(len(data)-10):len(data)]
            average = (sum(lasttendata))/10
            return average
    
        except (IOError, ValueError):
            destroy()
def loop():
    while True:
        if read() != None:
            print "Writing average to file: %0.2f" % read() 
#            copyfile(filename,newfilename)
            avgfile.write("%0.2f\n" % read())
            avgfile.flush()
            os.fsync(avgfile)
            sleep(5)

def destroy():
    data = []
    avgfile.close()
    pass

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


#with open(filename,"r") as infile:
#    try:
#        data = [float(n) for n in infile.read().split()]
#        lasttendata = data[(len(data)-10):len(data)]
#        average = (sum(lasttendata))/10
#        avgfile.write(float(average[2:]+"\n")
#        sleep(5)
#    except (IOError, ValueError):
#        data = []
#        avgfile.close()
#    except KeyboardInterrupt:
#        print lasttendata
#        avgfile.close()
#print data
#print "Length of data: ",len(data)
#print lasttendata
#print "Average of last 10: {0:0.2f}".format(sum(lasttendata)/10)

#total = sum(data)
#average = total / len(data)
#print("Length: {length}\nTotal: {total}\nAverage: {average}".format(length=len(data),total=total,average=average))
