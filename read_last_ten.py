filename = raw_input("enter path and filename:")
with open(filename,"r") as infile:
    try:
        data = [float(n) for n in infile.read().split()]
        lasttendata = data[(len(data)-10):len(data)]


    except (IOError, ValueError):
        data = []

#print data
print "Length of data: ",len(data)
print lasttendata
print "Average of last 10: {0:0.2f}".format(sum(lasttendata)/10)

#total = sum(data)
#average = total / len(data)
#print("Length: {length}\nTotal: {total}\nAverage: {average}".format(length=len(data),total=total,average=average))
