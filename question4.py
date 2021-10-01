import json

number={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    } 

file=open("que4.json","w")
json.dump(number,file,indent=2)
file.close()
