def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    
    mx=list_num[0]
    
    if mx<list_num[-1]:
        mx=list_num[-1]
        
        
    
    return mx

print(main([2,3,5,4]))