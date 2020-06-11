def unique_in_order_1(sequence):
    new_arr = []
    for i in range(len(sequence)):
        if sequence[i - 1] != sequence[i]:
            new_arr.append(sequence[i])
    
    return new_arr

def unique_in_order_2(sequence):
    if len(sequence) > 1:
        return [sequence[i] for i in range(len(sequence)) if sequence[i - 1] != sequence[i]]
    else:
        return list(sequence)

def unique_in_order_3(sequence):
    items = []
    for i in range(len(sequence)):
        if sequence[i] not in items:
            items.append()  


if __name__ =="__main__":
    a = 'A'
    a_new = unique_in_order_1(a)
    print(a_new)