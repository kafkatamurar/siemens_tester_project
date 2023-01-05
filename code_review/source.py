def fool(items):

    result = []

    for i in range(len(items)):
        
        flag=False
        for j in range(len(result)):
            
            if items[i] == result[j]:
                flag=True
                break

        if not flag:
            result.append(items[i])
            
    return result
