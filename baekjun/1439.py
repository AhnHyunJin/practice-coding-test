# S = input()

# cur = S[0]
# set_of = [0,0]

# for nxt_idx in range(0,len(S)):
#     if S[nxt_idx] != cur:
        
#         set_of[int(cur)] += 1
#         cur = S[nxt_idx]
#         if nxt_idx == len(S)-1:
#             cur = S[nxt_idx]
#             set_of[int(cur)]+=1

#     else:
#         if nxt_idx == len(S)-1:
            
#             set_of[int(cur)] +=1

# print(min(set_of[0],set_of[1]))


#==============풀이2==========

S = input()

len = len(S)

zero_part, one_part = 0,0

if S[0] == '0':
    zero_part = 1
else:
    one_part = 1

for nxt in range(1,len):
    if S[nxt] != S[nxt-1]:
        if S[nxt] == '0':
            zero_part +=1
        else:
            one_part +=1 

print(min(zero_part,one_part))