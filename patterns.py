# # # print a pattern of stars in a 2 shape

rows=5
mid=(rows//2)+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i<=3: 
            if i==1 or i==mid or j==rows:
                res+="*"+" "
            else:
                res+=" "+" "
        else:
            if i==rows or j==1:
                res+="*"+" "
            else:
                res+=" "+" "
    print(res) 
    
    #print a pattern of stars in a 3 shape

rows = 5
mid = (rows // 2) + 1

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == 1 or i == mid or i == rows:      # top, middle, bottom lines
            print("*", end=" ")
        elif (i < mid and j == rows) or (i > mid and j == rows):  # right side lines
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

