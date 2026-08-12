numbers=[1,2,3,4,5,6]
k=5
k=k%(len(numbers))
rotated = numbers[-k:]
print(rotated)
print(numbers[:-4])
print(numbers[-4:])

#find pairs that equals to target
nums = [2, 4, 3, 5, 7, 8]
target = 10

pairs = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((nums[i], nums[j]))

print(pairs)

#Findinf missing vales
nums = [1, 2,3, 4, 5]
n=len(nums)

expected=n(n*1)//2
actual=sum(nums)
total=expected- actual
print(total)

#Moving all zeros
numbers=[1,3,0,5,6,0,1,0]
num_1=[]
num_2=[]
for ch in numbers:
    if ch==0:
        num_1.append(ch)
    else:
        num_2.append(ch)

print(num_2+num_1)

numbers = [1, 3, 0, 5, 6, 0, 1, 0]

pos = 0

for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[pos] = numbers[i]
        pos += 1

while pos < len(numbers):
    numbers[pos] = 0
    pos += 1

print(numbers)

#separting even and odd
numeric=[1,2,3,4,5,6,7,8,9]
even_list=[]
odd_list=[]
for num in numeric:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
print("Even list",even_list)
print("Odd list",odd_list)

#Finding duplicate
duplicate_num=[1,1,3,4,5,6,7,3,1]
seen=set()
duplicate=set()
for num in duplicate_num:
    if num in seen:
        duplicate.add(num)
    else:
        seen.add(num)

print(duplicate)

#flatten loops
nums = [[1, 2], [3, 4], [5, 6]]
final_list=[]
for x in nums:
    for num in x:
        final_list.append(num)
print(final_list)

#frequecy count
duplicate_num=[1,1,3,4,5,6,7,3,1]
my_dict={}
for num in duplicate_num:
    if num in my_dict:
        my_dict[num]+=1
    else:
        my_dict[num]=1
print(my_dict)
    
occurances=[1,1,2,3,6,6,2,3,4,5]
target=2
total=[]
for num in occurances:
    if num!=target:
        total.append(num)
    else:
        pass
print(total)

my_dict={
    "Raju":30,
    "Manu":40,
    "Rohi":60,
}
total=0
for key,val in my_dict.items():
    if val>total:
        total=val

print(total)

dict_1={
    "name":"Rohii",
    "bge":22 
}

dict_2={
    "city":"Roh",
    "a":24
}

final_dict={}
for key,value in dict_1.items():
    final_dict[key]=value
for key,value in dict_2.items():
    final_dict[key]=value
    

print(final_dict)

student = {
    "Rohith": 101,
    "John": 102,
    "Alice": 103
}

final_dict={}
for key,value in student.items():
    final_dict[value]=key
print(final_dict)


sentence = "apple banana apple mango banana apple".split()

sent={}
for ch in sentence:
    if ch not in sent:
        sent[ch]=1
    else:
        sent[ch]+=1
print(sent)
 
my_dict={
    "Raju":1000,
    "Manu":900,
    "Rohi":60,
}
final_dict= sorted(my_dict.values)
print(final_dict)

text = "aabbcde"
d={}

for ch in text:
    if ch not in d:
        d[ch]=1
    else:
        d[ch]+=1

for  ch in text:
    if d[ch]==1:
       print(ch)
       break

sentence = "apple banana mango watermelon".split()
longest=sentence[0]
for word in sentence:
    if len(word)>len(longest):
        longest=word
print(longest)

list_1=[1,2,3,4,5,6,7,8]
list_2=[x**2 for x in list_1 if x%2==0]
for num in list_1:
    if num%2==0:
        list_2.append(num**2)
    
print(list_2)

sentence = "I love Python"
result=[]
for ch in sentence:
    if ch in "aeiouAEIOU":
        result.append(ch)
print(result)

list_1=[1,2,3,4,5,6,7,8]
for x in list_1:
    print(f"2 x {x}={2*x}")

nums = [1, 2, 3, 4, 5, 6]
groups={
    "even":[],
    "odd":[]
}
for num in nums:
    if num%2==0:
        groups["even"].append(num)
    else:
        groups["odd"].append(num)
print(groups)

duplicate_num=[1,1,3,4,5,6,7,3,1]
my_dict={}
max_key=None
total=0
for num in duplicate_num:
    if num in my_dict:
        my_dict[num]+=1
    else:
        my_dict[num]=1
for key, x in my_dict.items():
    if x > total :
        total=x
        max_key=key
print(max_key)

students = [
    {"name":"Roy","marks":90},
    {"name":"John","marks":70},
    {"name":"Alice","marks":85}
]

max_marks=0
for values in students:
    if values["marks"] > max_marks:
        max_marks=values["marks"]

print(max_marks)

data = [
    ("Roy", 90),
    ("John", 70),
    ("Alice", 85)
]


result=sorted(data,key=lambda x:x[1])
print(result)

