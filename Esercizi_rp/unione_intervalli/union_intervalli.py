

def merge_intervals(intervals) -> list[list[int]]:
    
    intervals.sort(key=lambda n: n[0])
    
    nuova_lista: list[list[int]] = []

    for i in range(len(intervals)):
        for k in range(len(intervals[i])):
            if k == 1:
                num_end = intervals[i][k]
            elif k == 0 and i != 0:
                num_start = intervals[i][k]
                if num_end >= num_start:
                    nuova_lista.append([intervals[i-1][0], intervals[i][k+1]])
                else:
                    nuova_lista.append([intervals[i][0], intervals[i][k+1]])
            
    
    return nuova_lista

intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals)) # restituisce [[1, 5]]     