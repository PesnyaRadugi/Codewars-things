''''You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N'''

def find_outlier(integers):
    odds, evens = [], []
    for i in integers:
        if i % 2 == 1:
            odds.append(i)
        else:
            evens.append(i)
    if len(odds) > len(evens):
        return evens[0]
    else:
        return odds[0]
    
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))