# Complete the solution so that it splits the string into pairs of 
# two characters. If the string contains an odd number of characters 
# then it should replace the missing second character of the final pair 
# with an underscore ('_').

def solution(s):
    arr = []
    if len(s) % 2 != 0:
        s += "_"
    
    if len(s) >=2:
        for i,x in enumerate(s):
            sub = ""
            if i % 2 != 0:
                sub += s[(i-1)] + s[(i)] 
                arr.append(sub)
                sub = ""
            
    return arr
                


print(solution("1234567"))

