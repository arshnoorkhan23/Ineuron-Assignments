# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# question number 1

n=9   # nos of rows
#r=  n//2+1   # rows after which inflection occurs

if n%2==0:
    r=n/2
else:
    r=n//2+1
for i in range(1,n+2):
    if i<=r:
        for j in range(0,i):
            print('*',end='')
        print('\n')
    else:
        for j in range(n-i+1,0,-1):
            print('*',end='')
        print('\n')


######################################

# question number 2
name=str(input('Enter the name'))
print(name)
rev_name=name[::-1]
print(rev_name)