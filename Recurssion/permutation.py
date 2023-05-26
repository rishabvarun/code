from itertools import permutations

string ='abc'
perm = list(map(lambda x : ''.join(x), permutations(string)))
print(perm)

def print_perm(s, i=0):

    if i == len(s) - 1:
        print(''.join(s))
    
    for j in range(i, len(s)):
        s[i], s[j] = s[j], s[i] # Need to swap the char with itself too

        print_perm(s, i + 1)    # i is the index of the element being shifted
                                # i will be shifted with all elements in right of i (including i)
        s[i], s[j] = s[j], s[i] # Need to reverse all the shifting done 

def my_func1(s, temp, i, n): # Doesn't work for duplicates

    if i == n:
        print(temp)
    
    for x in range(n):
        if s[x] not in temp:
            my_func1(s, temp + s[x], i+1, n)

def my_func2(s, temp, i, n, hash): # Works for duplicates

    if i == n:
        print(temp)
        return
    
    for x in range(n):
        if x not in hash:
            my_func2(s, temp + s[x], i+1, n, hash | {x})

#print_perm(list(string))
print("My func") 
string = 'aacd'
my_func1(string, '', 0, len(string)) 
#my_func2(string, '', 0, len(string), set())



    


