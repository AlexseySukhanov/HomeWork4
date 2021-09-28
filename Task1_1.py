num=1322 #решение для четырёхзначного числа
x=list(str(num))
if int(x[0])+int(x[1])==int(x[2])+int(x[3]):
    print("Number lucky")
else:
    print("Number not lucky")
