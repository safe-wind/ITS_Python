#es 5_11

ord_num :list[int] =list(range(1, 10))

for i in ord_num:

    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    elif i >=4 and i <= 9:
        print(f"{i}th")
    else:
        print("Error")