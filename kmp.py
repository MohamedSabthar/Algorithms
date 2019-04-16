def prefix(pattern):
    pi = [0]*(len(pattern))
    pi[0]=0
    k=0
    for q in range(1,len(pattern)):
        while k>0 and pattern[k]!=pattern[q]:
            k=pi[k-1]

        if(pattern[k]==pattern[q]):
            k+=1
        pi[q]=k
        
    return pi


def kmp(pattern,text):
    pi=prefix(pattern)
    k=0
    for i in range(0,len(text)):
        while k > 0 and text[i]!=pattern[k]:
            k=pi[k-1]
        if(pattern[k]==text[i]):
            k+=1
        if(k==len(pattern)):
            print(f'found {i-k+1}')            
            k=pi[k-1]

kmp('abc','abcabcabc')