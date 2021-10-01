
import json
dict_2 ={"name": "David",
     "class":"I",
     "age": 6  
 }
file=open("que2.json","w")
json.dump(dict_2,file,indent=2)
file.close()

file=open("que2.json","r+")
a=json.load(file)
print(a)
file.close() 