H,M=map(int,input().split())
T=int(input())
print((H*60+M+T)//60%24,(H*60+M+T)%60)