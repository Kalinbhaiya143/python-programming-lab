f=open('file.txt',mode='w')
f.write('Abhishek likes python\n')
f.write('And he is decent.\n')
f.close()
f=open('file.txt',mode='r')
last_line=f.readlines()[-1]
print(last_line)
f.close()