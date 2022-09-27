num_1=int(input("gb"))
num_2=int(input("inet"))

num_4=int(input("яку операцію \n1 часи \n2 хв \n3сек "))
if num_4==1:
    r=giga*8589934592
    t=int(r/inetbit/60/60)
    print("в годинах",t)
elif num_4==2:
    r=giga*8589934592
    t=int(r/ inetbit /60)
    print("в хв",t)
elif num_4==3:
    r=giga*8589934592
    t=int(r/inetbit)
    print("в сек",t)