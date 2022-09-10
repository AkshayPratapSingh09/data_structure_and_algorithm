def transformSentence(sentence):
    string = sentence
    terms=string.split()
    
    conv=[]
    changed_str=""
    for i in terms:
        changed_str+=i[0]
        #Will do traversal through each term
        for j in range(0,len(i)-1):
            #Case 1 --> y>x
            if (i[j].lower()<i[j+1].lower()):
                changed_str+=(i[j+1].upper())
            #Case 2 --> x>y
            elif (i[j].lower()>i[j+1].lower()):
                changed_str+=(i[j+1].lower())
            else:
                changed_str+=i[j+1]
        #This is the changes made every time wrt to term
        conv.append(changed_str)
        changed_str=""
    #This is the final result
    res=""

    for i in conv:
        res=res+" "+i
        final = res.strip()
        #Will return final 
    return final