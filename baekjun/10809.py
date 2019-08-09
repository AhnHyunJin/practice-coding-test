S = input()

a_ascii = ord("a")
z_ascii = ord("z")

_range = z_ascii - a_ascii
_dict = {}

for i in range(_range):
    idx = chr(a_ascii + i)    
    _dict[idx] = "-1"


for i, alpha in enumerate(S):
    if _dict[alpha] == "-1":
        _dict[alpha] = str(i)

tmp = ""

for i in _dict.values():
    tmp = tmp + i + " "
print(tmp)