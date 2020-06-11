def catch_words(string):
    words = string.split(" ")
    words_arr = [list(i) for i in words]
    for i in range(len(words_arr)):
        if len(words_arr[i]) >= 5:
            words_arr[i].reverse()

    splited_lst = []
    for k in range(len(words_arr)):
        splited_lst.insert(k," ")
        for x in words_arr[k]:
            splited_lst[k] += x

    splited_str = ""
    for j in splited_lst:
        splited_str += j
    splited_str = splited_str[1:]
    return splited_str

    
if __name__ == "__main__":
    
    x = "hello word overwatch chocolate hidrofobic niggas"
    print(x)
    splited = catch_words(x)
    print(splited)