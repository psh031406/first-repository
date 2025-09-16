# data = [41,32,30,23,24,32,11,39,24,46,50,18,41,14,33,50,38,25,32,16,43,19,35,22,46,43,10,22,17,47,66,48,25,43,28,31,12,25,12,48]

# min_value = min(data)
# max_value = max(data)
# print("최솟값:", min_value)
# print("최댓값:", max_value)


# w = (max_value-min_value)/6

# print("올림 전:", w)

# def ceil(x):
#     if int(x) == x:
#         return int(x)
#     elif x > 0:
#         return int(x) + 1
#     else:
#         return int(x)


# print("올림 후:", ceil(w)) 
# w_ceil = ceil(w)


# A = 9.5
# B = A+w_ceil
# C = B+w_ceil
# D = C+w_ceil
# E = D+w_ceil
# F = E+w_ceil
# G = F+w_ceil



# a1_count = len([x for x in data if A <= x < B])
# a2_count = len([x for x in data if B <= x < C])
# a3_count = len([x for x in data if C <= x < D])
# a4_count = len([x for x in data if D <= x < E])
# a5_count = len([x for x in data if E <= x < F])
# a6_count = len([x for x in data if F <= x <= G])


# b1 = a1_count/40
# b2 = a2_count/40
# b3 = a3_count/40
# b4 = a4_count/40
# b5 = a5_count/40
# b6 = a6_count/40

# c1 = (a1_count)
# c2 = (a1_count+a2_count)
# c3 = (a1_count+a2_count+a3_count)
# c4 = (a1_count+a2_count+a3_count+a4_count)
# c5 = (a1_count+a2_count+a3_count+a4_count+a5_count)
# c6 = (a1_count+a2_count+a3_count+a4_count+a5_count+a6_count)

# d1 = (a1_count)/40
# d2 = (a1_count+a2_count)/40
# d3 = (a1_count+a2_count+a3_count)/40
# d4 = (a1_count+a2_count+a3_count+a4_count)/40
# d5 = (a1_count+a2_count+a3_count+a4_count+a5_count)/40
# d6 = (a1_count+a2_count+a3_count+a4_count+a5_count+a6_count)/40

# e1 = (A+B)/2
# e2 = (B+C)/2
# e3 = (C+D)/2
# e4 = (D+E)/2
# e5 = (E+F)/2
# e6 = (F+G)/2


# a = print("1계급", "ㅣ계급간격ㅣ",A,"~", B, "ㅣ도수ㅣ", a1_count, "ㅣ상대도수ㅣ", b1, "ㅣ누적도수ㅣ",c1, "ㅣ누적상대도수ㅣ",d1, "ㅣ계급값ㅣ",e1)
# b = print("2계급", "ㅣ계급간격ㅣ",B,"~", C, "ㅣ도수ㅣ", a2_count, "ㅣ상대도수ㅣ", b2, "ㅣ누적도수ㅣ",c2, "ㅣ누적상대도수ㅣ",d2, "ㅣ계급값ㅣ",e2)
# c = print("3계급", "ㅣ계급간격ㅣ",C,"~", D, "ㅣ도수ㅣ", a3_count, "ㅣ상대도수ㅣ", b3, "ㅣ누적도수ㅣ",c3, "ㅣ누적상대도수ㅣ",d3, "ㅣ계급값ㅣ",e3)
# d = print("4계급", "ㅣ계급간격ㅣ",D,"~", E, "ㅣ도수ㅣ", a4_count, "ㅣ상대도수ㅣ", b4, "ㅣ누적도수ㅣ",c4, "ㅣ누적상대도수ㅣ",d4, "ㅣ계급값ㅣ",e4)
# e = print("5계급", "ㅣ계급간격ㅣ",E,"~", F, "ㅣ도수ㅣ", a5_count, "ㅣ상대도수ㅣ", b5, "ㅣ누적도수ㅣ",c5, "ㅣ누적상대도수ㅣ",d5, "ㅣ계급값ㅣ",e5)
# f = print("6계급", "ㅣ계급간격ㅣ",F,"~", G, "ㅣ도수ㅣ", a6_count, "ㅣ상대도수ㅣ", b6, "ㅣ누적도수ㅣ",c6, "ㅣ누적상대도수ㅣ",d6, "ㅣ계급값ㅣ",e6)


# counts = [a1_count, a2_count, a3_count, a4_count, a5_count, a6_count]
# labels = ["1", "2", "3", "4", "5", "6"]

# max_height = max(counts)

# for level in range(max_value, 0, -1):
#     for count in counts:
#         if count >= level:
#             print(" * ", end="")
#         else:
#             print("   ", end="")
#     print()

# for label in labels:
#     print(f" {label} ", end="")
# print()



#------------------------------------------------------------------------------------------난수------------------------------------------------------------------------------------------#

import random
random_n = random.choices(range(10, 1000), k=40)
print(random_n)

min_value = min(random_n)
max_value = max(random_n)
print(min_value, max_value)


w = (max_value-min_value)/6


print("올림 전:", w)

def ceil(x):
    if int(x) == x:
        return int(x)
    elif x > 0:
        return int(x) + 1
    else:
        return int(x)


print("올림 후:", ceil(w)) 
w_ceil = ceil(w)


A = min_value-0.5
B = A+w_ceil
C = B+w_ceil
D = C+w_ceil
E = D+w_ceil
F = E+w_ceil
G = F+w_ceil

a1_count = len([x for x in random_n if A <= x < B])
a2_count = len([x for x in random_n if B <= x < C])
a3_count = len([x for x in random_n if C <= x < D])
a4_count = len([x for x in random_n if D <= x < E])
a5_count = len([x for x in random_n if E <= x < F])
a6_count = len([x for x in random_n if F <= x <= G])


b1 = a1_count/40
b2 = a2_count/40
b3 = a3_count/40
b4 = a4_count/40
b5 = a5_count/40
b6 = a6_count/40

c1 = (a1_count)
c2 = (a1_count+a2_count)
c3 = (a1_count+a2_count+a3_count)
c4 = (a1_count+a2_count+a3_count+a4_count)
c5 = (a1_count+a2_count+a3_count+a4_count+a5_count)
c6 = (a1_count+a2_count+a3_count+a4_count+a5_count+a6_count)

d1 = (a1_count)/40
d2 = (a1_count+a2_count)/40
d3 = (a1_count+a2_count+a3_count)/40
d4 = (a1_count+a2_count+a3_count+a4_count)/40
d5 = (a1_count+a2_count+a3_count+a4_count+a5_count)/40
d6 = (a1_count+a2_count+a3_count+a4_count+a5_count+a6_count)/40

e1 = (A+B)/2
e2 = (B+C)/2
e3 = (C+D)/2
e4 = (D+E)/2
e5 = (E+F)/2
e6 = (F+G)/2


a = print("1계급", "ㅣ계급간격ㅣ",A,"~", B, "ㅣ도수ㅣ", a1_count, "ㅣ상대도수ㅣ", b1, "ㅣ누적도수ㅣ",c1, "ㅣ누적상대도수ㅣ",d1, "ㅣ계급값ㅣ",e1)
b = print("2계급", "ㅣ계급간격ㅣ",B,"~", C, "ㅣ도수ㅣ", a2_count, "ㅣ상대도수ㅣ", b2, "ㅣ누적도수ㅣ",c2, "ㅣ누적상대도수ㅣ",d2, "ㅣ계급값ㅣ",e2)
c = print("3계급", "ㅣ계급간격ㅣ",C,"~", D, "ㅣ도수ㅣ", a3_count, "ㅣ상대도수ㅣ", b3, "ㅣ누적도수ㅣ",c3, "ㅣ누적상대도수ㅣ",d3, "ㅣ계급값ㅣ",e3)
d = print("4계급", "ㅣ계급간격ㅣ",D,"~", E, "ㅣ도수ㅣ", a4_count, "ㅣ상대도수ㅣ", b4, "ㅣ누적도수ㅣ",c4, "ㅣ누적상대도수ㅣ",d4, "ㅣ계급값ㅣ",e4)
e = print("5계급", "ㅣ계급간격ㅣ",E,"~", F, "ㅣ도수ㅣ", a5_count, "ㅣ상대도수ㅣ", b5, "ㅣ누적도수ㅣ",c5, "ㅣ누적상대도수ㅣ",d5, "ㅣ계급값ㅣ",e5)
f = print("6계급", "ㅣ계급간격ㅣ",F,"~", G, "ㅣ도수ㅣ", a6_count, "ㅣ상대도수ㅣ", b6, "ㅣ누적도수ㅣ",c6, "ㅣ누적상대도수ㅣ",d6, "ㅣ계급값ㅣ",e6)

counts = [a1_count, a2_count, a3_count, a4_count, a5_count, a6_count]
labels = ["1", "2", "3", "4", "5", "6"]

max_height = max(counts)

for level in range(max_value, 0, -1):
    for count in counts:
        if count >= level:
            print(" @ ", end="")
        else:
            print("   ", end="")
    print()

for label in labels:
    print(f" {label} ", end="")
print()

# #------------------------------------------------------------------------------------------난수------------------------------------------------------------------------------------------#


