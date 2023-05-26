res = []

def subseq(string, cur, k):
    if k == len(string):
        res.append(cur)
        print(cur)
        return                 # Remember to return from base case
    subseq(string, cur, k + 1) # Either do not add char in subseq
    subseq(string, cur + string[k], k + 1) # Or add char in subseq for each char in string

subseq('abc', '', 0)
print(res)
