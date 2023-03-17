# EXERCISE 2
def bigger_is_greater(w)
    words = [w for w in str(w)]
        
        for x in range(len(words)-1,0,-1):
            
            if words[x-1] < words[x]:
                i = x
                
                for y in range(x, len(words)):
                    if words[y] < words[i] and words[y] > words[x-1]:
                        i = y
                        
                words[x-1], words[i] = \
                words[i], words[x-1] 
                
                r1 = ''.join(words[:x])
                s = words[x:]
                s.sort()
                r2 = ''.join(s)       
                
                return f'{r1}{r2}'
                
        return 'no answer'
