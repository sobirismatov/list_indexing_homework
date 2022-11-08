def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i=1
    k=0
    while i<len(list1):
        if list1[i-1]==list1[i]:
            k=True
        else :
            k=False
        i+=1
    return k
print(main([1,1,1,1]))