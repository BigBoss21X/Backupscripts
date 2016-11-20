number_list=[1,2,4,8]
othernumber_list=[]

pickone=raw_input("Pick either 1 or 2...")


if int(pickone) == 1:
    print number_list
    for squared in number_list:
        othernumber_list.append(squared**2)

    print othernumber_list
elif int(pickone) == 2:
    print othernumber_list
else:
    print "wrong selection"

