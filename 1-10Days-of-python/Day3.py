
name_list=["Rohith","Itagi","Davangere","Bangalore"]
print(name_list[1])
print(name_list[2:6])
print(name_list[-1])
print(name_list)

name_list[1]="Black Town"
print(name_list)
name_list[1:3]= ["Hey" ,"Bro"]
print(name_list)
name_list.append("Niranjan")
print(name_list)
name_list.insert(1,"Jayalakshmi")
print(name_list.pop(1))
print(name_list)
name_list.remove("Bro")
print(name_list)

for x in range(len(name_list)):
    print(name_list[x])

i=0
while i <len(name_list):
    i+=1
    print(i)

#list compression
[print(x) for x in name_list]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list=[x for x in fruits if 'a' in x]
print(new_list)

#Tuple
Fruits=("Orange","Apple","Bannana","promogranet","Pappaya")
y=list(Fruits)
y.append("Mango")
print(Fruits[1:3])
print(fruits)

#Concatinating tuples
tuple_1=(1,2,3,4,5,5)
tuple_2=(6,7,5,8,9)
new_tuple= tuple_1 +tuple_2
print(new_tuple)
print(new_tuple.count(5))
print(new_tuple.index(5))
set1={"1","2","3","4","5"}
set2={"5","6","7","8","9"}

print(set1|set2)
print(set1&set2)
print(set1-set2)

set1.add("4")
print(set1)

# print(set2.remove("10"))
# print(set2.discard("10"))
set1.pop()
print(set1)
set1.clear()
print(set1)

new_type=["1","2","3","4","5"]
new_tuple=tuple(new_type)
new_set=set(new_type)
print(new_set)
print(new_tuple)

#Dictionary
my_dict={
    "Name":"Rohith",
    "Age":22,
    1:"DSa"
}
print(my_dict.get("Name"))
print(my_dict["Age"])
print(my_dict.keys())
print(my_dict.values())
print(len(my_dict))
my_dict["Birthday"]="02-02-2025"
print(my_dict)
my_dict["Birthday"]="05-11-2025"
print(my_dict)
my_dict.update({"Birthday":"05-01-2024"})
print(my_dict)
del my_dict["Birthday"]
print(my_dict)

#loop through dictionaries
for x in my_dict:
    print(my_dict[x]) 
for x in my_dict.keys():
    print(x)
for x in my_dict.items():
    print(x)

#Neseted Dictionary
my_dict_1={
    "child1":{
        "Name":"Rohan",
        "Age":22,
        "year":2005
        },
     "child2":{
        "Name":"Roith",
        "Age":22,
        "year":2002
        },
    "child3":{
        "Name":"Rohi",
        "Age":22,
        "year":2004
        },
}
print(my_dict_1["child1"]["Name"])
for key,values in my_dict_1.items():
    print(values['Name'])
    
list_1=[1,2,3,[1,4,5,6],[3,5,9]]#list inside list
print(list_1[3][1])

my_list=[1,2,3,4,(1,2,3,4),{1,2,3},{"1"}]
