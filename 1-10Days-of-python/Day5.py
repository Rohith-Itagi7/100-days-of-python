numbers = [x for x in range(1,11)]
doubled = [num*2 for num in numbers if num%2==0]
print(doubled)

names=["Rohith","Brother","Pacchi"]
cl={name:len(name) for name in names}
print(cl)

city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_pop={city:value for city,value in city_population.items() if value>10}
print(large_pop)



l=["Benne Dosa","Fish","Chicken biriyani"]
d=[x.upper() for x in l]
print(d)

dict_1={
    "Apple": 20,
    "Mango": 30,
    "Bannana":40
}
total=0
for key,values in dict_1.items():
    total+=values

print(total)

list_1=[
    {"name":"Rohith ",
     "Age":22  ,
     "marks":"100 "},
     {"name" :"Manohar",
      "Age":25,
      "marks":"80"
     }
]
for student in list_1:
    print(student["name"] ,"-", str(student["Age"]),"-" ,student["marks"])


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print(row)
    r=0
    for i in row:
        r+=i
    print(r)

#Coding challenges
l=[9,1,2,3,5,1,7,9,1]
print(max(l))
l_1=l[0]
for i in l:
    if i<l_1:
       l_1=i
print(l_1)

#sum of all numbers
i=0
for num in l:
    i+=num
print(i)

l_2=sorted(l)
print(l_2[-2])

print(l.count(1))
print(l[::-1])
   
set_1=set(l)
l_2=list(set_1)

l_2.sort()
print(l_2[-2])


rohi=[2,3,4,4,"trh","True"]
raks=[3,5,6,2,8,"Brother","ok"]
manu=rohi+raks
print(manu)

    
name="Bajeragoi"
vowels="aieo"
count=0
for char in name:
    if char in vowels:
        count+=1
print(count)
print(name[::-1])

cities="Bangalore"

t_cities=cities[::-1]

if t_cities==cities:
    print("Palindrome")
else:
    print("It's not Palindrome")

cricket="ViRat"
count=0
count_1=0
for char in cricket:
    if char.isupper():
        count+=1
    if char.islower():
        count_1+=1

print(count)
print(count_1)

drink="Red remender"
result={}
for char in drink:
    if char in  result:
        result[char]+=1
    else:
        result[char]=1
print(result)

tuple=(1,2,3,4,"True",True)
print(list(tuple))
fruits=["apple","bannana","Strawberry"]
h1=tuple(fruits)
print(h1)

set_1={2,3,3,6,7,8}
set_2={"True",True,"1",2,3,4,3,7}

print(set_1|set_2)

