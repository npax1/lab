a=int(input("ведіть час в секунди"))
q=int(input("ведіть час в 1 2 xb 3"))
if q==1:
    s=a-86400
    print(s)
elif q==2:
    d=a/60
    f=d-1440
    print(f)
elif q==3:
    g=a/3600
    h=g-24
    print(h)
else:
    print("введи 1 2 чи 3")