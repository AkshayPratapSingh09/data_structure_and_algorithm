a = "[a+b}"
b = list(a)
print(b)
# print("{" in b and "}" in b)
if ("[" in b and "]" in b):
    if (b.index("[") < b.index("]")):
        print("The string",a,"Balanced")

elif ("{" in b and "}" in b):
    if (b.index("{") < b.index("}")):
        print("The string",a,"balanced") 

elif ("(" in b and ')' in b):
    if (b.index("(")< b.index(")")):
        print("The string",a,"is Balanced")

else:
    print("The string",a,"is Unbalanced")
