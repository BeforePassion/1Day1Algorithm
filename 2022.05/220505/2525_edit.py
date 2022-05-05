A,B=map(int,input().split())
C=int(input())
if A==23:
    if (60-B)<C:
        print(((B+C)//60)-1,(B+C)%60)
    elif B==30:
        print(0,(B+C)%60)
    else: print(A,B+C)
elif 0<=A<7:
    if (60-B)<C:
        print(A+((B+C)//60),(B+C)%60)
    elif B==30:
        print(A+1,(B+C)%60)
    else: print(A,B+C)
elif A==7:
    if 40<=B:
        if (60-B)<C:
            print(A+((B+C)//60),(B+C)%60)
        else: print(A,B+C)
    elif B==30:
        print(A+1,(B+C)%60)
    else:
        if C<(60-B):
            print(A,B+C)
        else:
            if A+((B+C)//60)<24:
                if (60-B)<C:
                    print(A+((B+C)//60),(B+C)%60)
                else: print(A,B+C)
            else: print(A+((B+C)//60)-24,(B+C)%60)
else:
    if C<(60-B):
        print(A,B+C)
    elif B==30:
        print(A+1,(B+C)%60)
    else:
        if A+((B+C)//60)<24:
            if (60-B)<C:
                print(A+((B+C)//60),(B+C)%60)
            else: print(A,B+C)
        else: print(A+((B+C)//60)-24,(B+C)%60)