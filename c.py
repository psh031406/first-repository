
# data = [41,32,30,23,24,32,11,39,24,46,50,18,41,14,33,50,38,25,32,16,43,19,35,22,46,43,10,22,17,47,66,48,25,43,28,31,12,25,12,48]

# min = min(data)
# max = max(data)
# print("최솟값:", min)
# print("최댓값:", max)


#-------------------------난수------------------------------#
import random
random_n = random.choices(range(10, 1000), k=40)
print(random_n)

min = min(random_n)
max = max(random_n)
print(min, max)
#-------------------------난수------------------------------#



w = (max-min)/6
print(w)

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


A = 9.5
B = A+w_ceil
C = B+w_ceil
D = C+w_ceil
E = D+w_ceil
F = E+w_ceil
G = F+w_ceil



# a1_count = len([x for x in data if A <= x <= B])
# a2_count = len([x for x in data if B <= x <= C])
# a3_count = len([x for x in data if C <= x <= D])
# a4_count = len([x for x in data if D <= x <= E])
# a5_count = len([x for x in data if E <= x <= F])
# a6_count = len([x for x in data if F <= x <= G])

#-------------------------난수------------------------------#
a1_count = len([x for x in random_n if A <= x <= B])
a2_count = len([x for x in random_n if B <= x <= C])
a3_count = len([x for x in random_n if C <= x <= D])
a4_count = len([x for x in random_n if D <= x <= E])
a5_count = len([x for x in random_n if E <= x <= F])
a6_count = len([x for x in random_n if F <= x <= G])
#-------------------------난수------------------------------#

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


a =print("1계급", "계급간격ㅣ",A,"~", B, "도수ㅣ", a1_count, "상대도수ㅣ", b1, "누적도수ㅣ",c1, "누적상대도수ㅣ",d1, "계급값ㅣ",e1)
b =print("2계급", "계급간격ㅣ",B,"~", C, "도수ㅣ", a2_count, "상대도수ㅣ", b2, "누적도수ㅣ",c2, "누적상대도수ㅣ",d2, "계급값ㅣ",e2)
c =print("3계급", "계급간격ㅣ",C,"~", D, "도수ㅣ", a3_count, "상대도수ㅣ", b3, "누적도수ㅣ",c3, "누적상대도수ㅣ",d3, "계급값ㅣ",e3)
d =print("4계급", "계급간격ㅣ",D,"~", E, "도수ㅣ", a4_count, "상대도수ㅣ", b4, "누적도수ㅣ",c4, "누적상대도수ㅣ",d4, "계급값ㅣ",e4)
e =print("5계급", "계급간격ㅣ",E,"~", F, "도수ㅣ", a5_count, "상대도수ㅣ", b5, "누적도수ㅣ",c5, "누적상대도수ㅣ",d5, "계급값ㅣ",e5)
f =print("6계급", "계급간격ㅣ",F,"~", G, "도수ㅣ", a6_count, "상대도수ㅣ", b6, "누적도수ㅣ",c6, "누적상대도수ㅣ",d6, "계급값ㅣ",e6)


#----------------------------------------------그래프 그리기------------------------------------------------------#
