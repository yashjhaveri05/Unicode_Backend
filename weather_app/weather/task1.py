def Task1(x,y):
    dictionary = {}
    for i in range(x, y):
        dictionary[i] = "11" in bin(i)[2:]
    return dictionary

"""
# Saw this on geeksforgeeks but did not understand
# Maybe this might be a better way

def adjacentSet(n): 
    return (n & (n >> 1)) 
  
# Driver Code 
if __name__ == '__main__': 
    n = 3
    if (adjacentSet(n)): 
        print("Yes") 
    else: 
        print("No") 
"""