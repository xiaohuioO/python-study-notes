for i in range(2,11) :
    for j in range(2,i) :
        if i%j==0 :
            print(i,'=',j,'*',i//j)
            break
    else :
        print(i,"是素数")
