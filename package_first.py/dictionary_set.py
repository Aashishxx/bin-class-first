# dictionary --> is ordererd and muutable or changebale but does not allowed duplicate key

# dict={
#     "name":"ashish",
#     "age":25,
#     "adult":True,
#     "mark":98.5,
#     "subject":["python", "c", "java"],
#     "tup":(1,2,3,4)
# }
# print(dict)
# print(type(dict))
# print(dict["name"])

# dict["name"]="prience" #its always overwrite old key
# dict["surname"]="sah"
# dict[[1,2,3,4]]="aashish" # this program will not run bcuz you cant use list and dict in a key cut its changeable
# print(dict)

###########################################################
#created null dictinary
# dict={}
# dict["name"]="aashish"
# dict["age"]=25
# dict["job"]="softwarre enginner"
# dict["salary"]=20000 
# print(dict)

################################################################
#nested in dictinory:
# student={
#     "name":"aashish",
#     "subject":{ #nested dictionary
#         "physics":90,
#         "chemistry":85,
#         "math":95
        
#     }
# }
# print(student)
# print(student["subject"])
# print(student["subject"]["chemistry"])
###########################################
#method in dictionary
# print(student.keys()) # to acess key value

# print(list(student.keys())) # to covert dict key in list 

# print(len(student)).         #to find the length of dictionary

# print(student.values())      #top acess the value of dictionary

# print(list(student.values())) #to convert dict value in list

# print(student.items())       #to acess the key and value of dictionary
# pair = list(stud÷ent.items())
# print(list(student.items())) 

########
# print(student.get("subject")) # to get particular value of particular key

# print(student.update({"country":"nepal"})) #to add new key and value in dictionary
# print(student)

# print(student.pop("name"))    #to delet key and vlue in dict
# print(student)

# print(student.popitem())    #to delet last key and value in dict
# print(student)

###########################################################################
#set in python --> is unorderd and unindexed and does not allowed duplicate value.
#you cannot store any vlue in set but not list and dict becuz its mutable.

# set={1,2,3,4,5, "hello world, 19.5, 1"}
# print(set)
# print(type(set))
# print(len(set)) # you can perform this in set


# set={1,2,3,3,3, "aashish", "aashish"} #dup value will be ignored in set.
# print(set) #
##########################################################################
# set = set() #if you wantt to print empty set then do like this
# print(type(set))

#methods==>
# set.add(1)
# set.add(2)
# # set.add(3)
# # set.add(3)
# set.add("aashish")
# set.add(19.8)
# # set.add(25)
# # set.add((1,2,3))

# #===> cannot use list amd dict in set

# # (set.remove("aashish")) #to remove any set elemwnt
# # set.clear() #to clear all set value
# # print(len(set))

# set.pop() #it can pop any random value
# set.pop() 
# print(set)

# there is two more importanyt method in set==>union amd intersection
# sett1={1,2,3,4,}
# set2={2,3,4,}
# print(set.union(set2))
# print(set.union(set2))

#practrice question:q1 -->from dict
# dict={
#     "table" : ("a piece of furniture", "list of fact and figure"),
#     "cat": " a small animal"

# }
# print(dict)

#q2==>from set

# subjects={"python","java","c++", "python", "javascript",
#            "java","python","java","c++","c"}
# print(len(subjects))

#q3-->
# marks={}

# x = input("enter physics: \n")
# marks.update({"physics" : x})

# x = input("enter chemistryt: \n")
# marks.update({"chemistry" : x})

# x = input("enter Math: \n")
# marks.update({"physics" : x})

# print(marks)

# #q4
# set={
#    ("float",9.0),
#    ("int",9)
# }
# print(set)


