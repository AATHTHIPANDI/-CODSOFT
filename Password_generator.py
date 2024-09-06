import random

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', \
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

sp = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=']
pas = ""
no_alph = int(input("ENTER NO. OF ALPHABETS IN YOUR PASSWORD "))
no_num = int(input("ENTER NO. OF NUMBERS IN YOUR PASSWORD "))
no_sp = int(input("ENTER NO. OF SPECIAL CHAR IN YOUR PASSWORD "))
shuffle_pass = ""
for i in range(1, no_alph + 1):
    a = random.choice(alph)
    pas += a

for i in range(1, no_num + 1):
    n = str(random.choice(num))
    pas += n

for i in range(1, no_sp + 1):
    s = random.choice(sp)
    pas += s
pss_lst = list(pas)
random.shuffle(pss_lst)

for i in pss_lst:
    shuffle_pass += i
print("YOUR PASSWORD is",shuffle_pass)

