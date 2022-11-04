#1. Write a Python script to sort (ascending and descending) a dictionary by value.
mydict={
    1:"y",
    2:"x",
    3:"z"
}

x=sorted(mydict.values())
print(x)
y=sorted(mydict.values(),reverse=True)
print(y)

#Write a Python script to add a key to a dictionary. 
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

mydict={
    0:10,
    1:20
}
mydict[2]=30
print ("Actualizado",mydict)

#Write a Python script to concatenate following dictionaries to create a new one. 
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dict4={**dic1,**dic2,**dic3}
print ("Diccionarios del mundo unidos",dict4)




#Write a Python script to check whether a given key already exists in a dictionary.
str_dict={
    "Perro":4,
    "Gato":4,
    "Ave":2,
    "Humano":2    
}
#search=input("Palabra a buscar: ")
for key in str_dict.keys():
    if "Perro" == key:
        print(f"La palabra '{key}' ya existe en este diccionario")
        break
else:
    print(f"La palabra  no existe todavía.")

#o solamente en condicional: 

if 8 in dict4.keys():
    print ("El elemento existe en el diccionario")
else:
    print("El elemento no existe")




#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
#n=int(input("Inserte un número: "))
multiply={i:i*i for i in range(1,6) }
print(multiply)




#7.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys. Go to the editor
#Sample Dictionary
#mydict={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

mydict={i:i*i for i in range(1,16)}
print(mydict)




#Exercise 1: Convert two lists into a dictionary
#Below are the two lists. Write a Python program to convert them into a dictionary in
# a way that item from list1 is the key and item from list2 is the value
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
mydict={keys[i]:values[i] for i in range (len(keys))}
print (mydict)
#o:
for i in range(len(keys)):
    mydict[keys[i]]=values[i]




#Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3={**dict1,**dict2}
print(dict3)




#Exercise 3: Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])




#Exercise 4: Initialize dictionary with default values
#In Python, we can initialize the keys with the same values.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

mydict={i:defaults for i in employees}
print(mydict)




#Exercise 5: Create a dictionary by extracting the keys from a given dictionary
#Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}




# Keys to extract
#keys = ["name", "salary"]
new_dict={key:value for key,value in sample_dict.items() if key=="name" or key=="salary"}
print(new_dict)
#oooo:
##########
keys = ["name", "salary"]
new_dict1={k:sample_dict[k] for k in keys}
print(new_dict1)





#Exercise 6: Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]
del sample_dict["name"]
del sample_dict["salary"]
print (sample_dict)
#ooo
########
sample_dict2 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
for key in keys:
    if key in sample_dict2:
        del sample_dict2[key]
print (sample_dict2)
#oooo
######
keys = ["name", "salary"]
sample_dict3 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
sample_dict3= {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict3)



#Exercise 7: Check if a value exists in a dictionary
#We know how to check if the key exists in a dictionary. Sometimes it is required 
# to check if the given value is present.

#Write a Python program to check if value 200 exists in the following dictionary.

sample_dict = {'a': 100, 'b': 200, 'c': 300}
#200 present in a dict

if 200 in sample_dict.values():
    print ("200 present in the dict")



  
#Exercise 8: Rename key of a dictionary
#Write a program to rename a key city to a location in the following dictionary.
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

#{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

sample_dict['location'] = sample_dict.pop('city') #sample_dict['location']crea una nueva key con el mismo value
                                                  # de sample_dict['city'] y sample_dict.pop(city) borra el registro viejo
print(sample_dict)


#Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sample_dict, key=sample_dict.get))

#Exercise 10: Change value of a key in a nested dictionary
#Write a Python program to change Brad’s salary to 8500 in the following dictionary.

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict["emp3"]["salary"]=8500
print(sample_dict)
