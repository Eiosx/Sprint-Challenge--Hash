def has_negatives(a):

    """
    YOUR CODE HERE
    """
    intersectDict = {}

    for num in a:
      if num < 0:
        positiveNum = num * -1

        if positiveNum not in intersectDict:
          intersectDict[positiveNum] = "negative number present"
        else:
          if intersectDict[positiveNum] == "negative number present":
            pass
          elif intersectDict[positiveNum] == "positive number present":
            intersectDict[positiveNum] = "intersect"
          elif intersectDict[positiveNum] == "intersect":
            pass

      else: 
        if num not in intersectDict:
          intersectDict[num] = "positive number present"
        else:
          if intersectDict[num] == "negative number present":
            intersectDict[num] = "intersect"
          elif intersectDict[num] == "positive number present":
            pass
          elif intersectDict[num] == "intersect":
            pass

    result = [key for key in intersectDict if intersectDict[key] == "intersect"]

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
