def rabin(text,pattern):
    textHash = patternHash = 0
    prime = 37
    dPrime = 13

    for i in range(len(pattern)):
        textHash = (textHash*prime + ord(text[i]))%dPrime
        patternHash = (patternHash*prime + ord(pattern[i]))%dPrime 

    for i in range(len(text)-len(pattern)+1):
        if textHash == patternHash :
            j = 0
            while j < len(pattern) and text[i+j]==pattern[j] :
                j+=1
            if j==len(pattern):
                print(f'found pattern @ index {i}')

        if i < len(text)-len(pattern):
            textHash = ((textHash-(ord(text[i])*pow(prime,len(pattern)-1))) * prime + ord(text[i+len(pattern)]))%dPrime
            
            



rabin('Can you find me!','ou fi')