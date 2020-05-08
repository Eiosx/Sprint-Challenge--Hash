def intersection(arrays):

    numDict = {}

    for numArr in arrays:
      for element in numArr:
        if element in numDict:
          numDict[element] += 1
        else:
          numDict[element] = 1

    result = []

    for key in numDict:
      if numDict[key] == len(arrays):
        result.append(key)
          
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
