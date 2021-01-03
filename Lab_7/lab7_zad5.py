inp1 = input("Podaj pierwsze słowo: ")
inp2 = input("Podaj drugie słowo: ")

tup1 = (inp1)
tup2 = (inp2)

def anagram(t1, t2):
    if len(t1) == len(t2):
        for x in t1:
            if x not in t2:
                print("Słowa nie są anagramami.")
                break
        print("Słowa są anagramami")
    else:
        print("Słowa nie są anagramami")

s1 = ("niedziela")
s2 = ("dzielenia")

print(s1, s2)
anagram(s1, s2)

print(inp1, inp2)
anagram(tup1, tup2)
