
#Python Dictionaries are data type
#Dictionaries are used to store data values in key:value pairs.Dictionaries are created by enclosinga comma-separated list of key-value pairs in curly braces { }.
#key should be unique.

data={
    "name": "shashi",
    "address":"nepal",
    "age":22,
    "phone":[980,9855],
    "percentage":72.5,

#Dictionary Items
#Dictionary items are ordered, muteable(changeable), and does not allow duplicates.
    "name":"55" # if there is same key, value is  updated by latest value. also length will be same.i.e change the value in the dictionary
}
print(type(data))
print(data)
print(len(data)) ## To determine how many items dictionary have, use the len() function.
print(data["percentage"])
#print(data["agent"]) # keyerror
print(data.keys())# The keys() method returns the keys of the dictionary as a list.
print(data.values()) #The values() method returns the values of the dictionary as a list.

#update value -->change the value in the dictionary.
data["age"]=45
print (data)

data["percentage"]=100
print(data)

# add temp_num to the dictionary
data['temp_num']=98765 # if there is no value in dict it will create new value in dict.
print(data)

# The update() method is also used to change the the value in the
data["age"]=99
data["home"]="nawolpur"
data.update(
    {'age':22,
    "temp_num":100
    }
 ) 
print(data)


#Remove Dictionary Items
#1.pop--> the pop() method removes the item with the specified key name
data1={
    "name":"araa",
    'roll':20,
    "class":10,
    "phone":98765432,
    "sub":"math"
}
print(data1)
data1.pop("name")
print(data1)
 

#2.Popitem--> The popitem() method removes the last inserted item
data1.popitem()
print(data1)
#data1={}
#data.popitem()# error occur cause of empty dict

#3.clear --> The clear() method empties the dictionary
data1.clear()
print(data1)


#4.Del---> The del keyword removes the item with the specified key name
boy = {
    'Name': 'Ali',
    'Age': 21,
    'Hieght': 6,
    'Weight': 68,
    'City':'Peshawar', 
    'Religion': 'Muslim'}
# delete any item from the dictionary
del boy['Hieght']
print(boy)
# result={'Name': 'Ali', 'Age': 21, 'Weight': 68, 'City': 'Peshawar','Religion': 'Muslim'}

# The del keyword can also delete the dictionary completely
boy = {'Name': 'Ali',
     'Age': 21, 
     'Hieght': 6, 
     'Weight': 68, 
     'City':'Peshawar',
     'Religion': 'Muslim'}

# delete the dictionary
#del boy
#print(boy) # This will cause an error because the dictionary boy no longer exists



#get()---> The get() method returns the value of the item with the specified key
#if there is a no key it will result none if there is key with value it will print as it is. 

value={
    "city":'usa',
    "status":"happy",
    "background":'rich',
    "income":9876543,
}
print(value.get('status'))# get the value of the item

education = value.get('education','Undergraduate') ## Try to return the value of an item that do not exist, i.e Undergraduate is default value
print(education) 

#Nested Dictionaries -----> A dictionary can contain dictionaries, this is called nested dictionaries.
data1={
    "name":"araa",
    'roll':20,
    "class":10,
    "phone":{
        "ntc":9876,
        "ncl":87
    },
    "sub":"math"
    
    }
print(data1["phone"]["ncl"])


#question:  
data={
    "name":"hari",
    "address":"nepal",
    "age":12,
    "phone":[
        {
            "type":"ntc",
            "num":9877
        },
        {
            "type":"ncl",
            "num":9800

        },
    ],
    "percentage":1000
}
print(data)
print(data['name'],data['phone'][0]['type'],"number is",data['phone'][0]['num'])
print(data['name'],data['phone'][1]['type'],"numbwr is",data['phone'][1]['num'])


#F_string
print(f"{data['name']} {data['phone'][0]['type']} number is {data['phone'][0]['num']} ")
print(f"{data['name']} {data['phone'][1]['type']} number is {data['phone'][1]['num']} ")