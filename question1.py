# Q.1 Json data ko python object main convert karne ka program likho?. 

import json
dict1={"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }


file=open("que1.json","w")
json.dump(dict1,file,indent=2)
file.close()

file=open("que1.json","r+")
a=json.load(file)
print(a)
file.close()