# first letter of all the words remain unchanged.
string = "a Blue MOON"
ls_words = string.split(" ")
# print(ls_words[1:])
ls_op = ls_words[1:]
# print(len(ls_op[0]))

st = ""
st1 = ""
for i in range(len(ls_op)):
    term = ls_op[i] 
    for j in range(len(term)-1):
        y = term[j+1]
        x = term[j] 
        print("x:",x,"Y:",y)
        if y.lower()<x.lower():
            st += term[j].upper()
        if x.lower()<y.lower():
            st +=term[j].lower()
            # print("x Greater than y")
        print(st)
    st1 += st+" "
print(ls_op)
print(st1)