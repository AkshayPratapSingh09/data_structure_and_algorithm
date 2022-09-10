string = "8hypotheticall024y6wxz"
# # ls_al = ["a", "f","c", "g","r", "h","e","t","b"]
# # ls_al.sort()
# # ls_num = ["1", "55", "22","56","67","32","89"]
# # ls_num.sort()
# print(ls_num)
ls_al = []
ls_al_mis = []
ls_num = []
ls_num_mis = []
for i in string:
    # print(i)
    if ord(i)>=97 and ord(i)<123:
        ls_al.append(i)
    else:
        ls_num.append(i)
ls_al.sort()
ls_num.sort()
# print(ls_al)
# print("".join(ls_num+ls_al))
for i in range(97,123):
#     for j in range(len(ls_al)):
        if chr(i) not in ls_al:
            # print(chr(i), end = " ")
            ls_al_mis.append(chr(i))
for i in range(0,10):
    if str(i) not in ls_num:
        # print(i, end= " ")
        ls_num_mis.append(str(i))

# print(ls_al_mis)
# print(ls_num_mis)
print(string)
print("".join(ls_num_mis+ls_al_mis))

