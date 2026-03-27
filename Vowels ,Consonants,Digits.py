#Vowels,Consonants,digits:
s=input("Enter a string:")
vowels=0
consonants=0
digits=0
for ch in s:
    if ch.isdigit():
        digits+=1
    elif ch.isalpha():
        if ch.lower()=='a' or 'e' or 'i' or 'o' or 'u':
            vowels+=1
        else:
            consonants+=1
    
print(f"Vowels={vowels},Consonants={consonants},Digits={digits}")
    
