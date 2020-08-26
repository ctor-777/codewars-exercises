
def calculate_huge_number(lst):
    if type(lst) != list:
        raise TypeError(f"the input have to be type list, you introduced a type {type(lst)}")
    if len(lst) < 1:
        raise ValueError("the list have to have at least one element")
    if len(lst) == 1:
        return lst[0]
    else:
        

def last_digit(lst):
    