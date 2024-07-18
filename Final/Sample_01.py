"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
"""
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

row = int(input("enter a row number"))

for i in range(row+1,1,-1):
    for j in range(1,i):
        print(j, end="")
    print()

