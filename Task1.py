num=1323531235 #решение для любого числа
sum1=0
sum2=0
x=list(str(num))
if not (len(x))%2:
    for i in range(int(len(x)/2)):
        sum1+=int(x[i])
        sum2+=int(x[i+int(len(x)/2)])
    if sum1==sum2: print("Number lucky")
    else: print("Number not lucky")
else:
    print("Can`t calculate `lucky number` ")

