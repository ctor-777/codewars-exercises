

def dots_and_boxes(ar):
    first, second = zip(*ar)

    max_in_ar = max(max(first), max(second))
    square_length = (max_in_ar + 1)** 0.5
    print(max_in_ar, square_length)

if __name__ == "__main__":
    dots_and_boxes(((1,2),(1,5), (8,0)))