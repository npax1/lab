num_1=int(input("веди діаметр"))
x=3.14
s=int(input("яка операція \n 1периметр \n 2площа"))
if s==1:
    p=(x*num_1*num_1)
if s ==2:
    p=(x*num_1*2)
print(f'p={p}')