
def ordinamento(numeri:list[int]) -> list[int]:
    for i in range(len(numeri)):
        for ii in range(len(numeri)):
            if list[i] <= list[ii]:
                list[ii] = list[i]
                list[i] = list[ii]