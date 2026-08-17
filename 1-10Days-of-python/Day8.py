#Hacker rank Challenge 1
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

#Hacker rank Challenge 2
print(a+b)
print(a-b)
print(a*b)



def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4==0:
        leap=True
        if year % 100==0:
            leap=False
            if year % 400==0: 
                leap=True
    return leap

year = int(input())
print(is_leap(year))

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result=[]
    l=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if i+j+k!=n:
    #                 result.append([i,j,k])
    print(l)
                
