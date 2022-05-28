lst=[]
for i in range(int(input())):
       x=list(map(int,input().split(" ")))
       out=min(x[0]*x[1],x[0]+x[2])
       lst.append(out)
for i in lst:
       print(i)
       
       
       
