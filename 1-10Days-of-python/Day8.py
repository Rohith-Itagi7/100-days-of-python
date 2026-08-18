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

#Leap year problem
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

#list comprehension problem
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

#tuple problem hacker rank
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t=tuple(integer_list)

    print(hash(t))
    
#Swapcase
def swap_case(s):
    final=''
    for ch in s:
        if ch.isupper():
            ch = ch.lower()
            final+=ch
        else:
            ch = ch.upper()
            final+=ch
    return final

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#String delimiter
def split_and_join(line):
    # write your code 
    line=line.split(" ")
    line="-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


                
