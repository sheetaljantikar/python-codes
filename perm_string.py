def permutations(string, step = 0):

    
    if step == len(string):
        print ("".join(string))

    
    for i in range(step, len(string)):

        
        string_copy = [character for character in string]

        
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        
        permutations(string_copy, step + 1)

s='star'
a=permutations(s,step=0)
b=len(a)
c=len(set(a))