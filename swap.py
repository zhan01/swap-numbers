def swapPositions(list, pos1, pos2): 
  
    get = list[pos1], list[pos2] 
     
    list[pos2], list[pos1] = get 
       
    return list

List = [23, 65, 19, 90, 77, 85] 
  
pos1, pos2  = 1, 6
print(List)
print("\nSwaped list")
print(swapPositions(List, pos1-1, pos2-1)) 