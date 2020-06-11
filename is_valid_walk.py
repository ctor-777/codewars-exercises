def is_valid_walk(walk):
    position = [0,0]
    time = 10

    if len(walk) > time or len(walk) < time:
        print("should return False")
        return False
 
    for i in range(time):
        if walk[i] == "n":
            position[0] += 1
        elif walk[i] == "s":
            position[0] -= 1
        elif walk[i] == "w":
            position[1] -= 1
        elif walk[i] == "e":
            position[1] += 1
        else:
            print(f"{walk[i]} is not a valid direccion")

    if position[0] == 0 and position[1] == 0:
        print("should return True")
        return True
    else:
        print("should return False")
        return False
    
    

if __name__ =="__main__":
    walk = ['n','s','n','s','n','s','n','s','n','s']
    print(len(walk))