def maxTwo(var):
    if var == 1:
        return var

    start = 0
    mx = [0,0,0]

    for i in range(0, len(var)):
        start = 0
        while 1:
            end = start + i + 1
            
            if end + 1 > len(var):
                break

            subset = var[start: end + 1]
            sort = sorted(subset, reverse = True)
            
            #print subset
            #print sort

            val = sort[0] & sort[1]
        
            if val > mx[0]:
                mx[0] = val
                mx[1] = start
                mx[2] = end
            else:
                if val == mx[0]:
                    if mx[1] != 0 and mx[2] != 0:
                        if end - start < mx[2] - mx[1]:
                            mx[1] = start
                            mx[2] = end
                    else:
                        mx[1] = start
                        mx[2] = end

            #print mx[1], mx[2]
            #print start, end   

            #print mx[1], mx[2]
            start += 1


    return [mx[1],mx[2]]

if __name__ == "__main__":
    print maxTwo([1,2,6,6])