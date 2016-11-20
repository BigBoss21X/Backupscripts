filename = raw_input("enter path and filename:")
with open(filename,"r") as infile:
    try:
        data = [float(n) for n in infile.read().split()]
    except (IOError, ValueError):
        data = []
total = sum(data)
average = total / len(data)
print("Length: {length}\nTotal: {total}\nAverage: {average}".format(length=len(data),total=total,average=average))
