# We want to read the content of this file. Below is the implementation.
    
# import json
  
# # Opening JSON file
#  f = open('data.json',)
  
# # returns JSON object as 
# # a dictionary
#  data = json.load(f)
  
# # Iterating through the json
# # list
# for i in data['emp_details']:
#     print(i)
  
# # Closing file
# f.close()

# import json
  
  
# # JSON string
# a = '{"name": "Bob", "languages": "English"}'
  
# # deserializes into dict 
# # and returns dict.
# y = json.loads(a)
  
# print("JSON string = ", y)
# print()
  
  
  
# # JSON file
# f = open ('data.json', "r")
  
# # Reading from file
# data = json.loads(f.read())
  
# # Iterating through the json
# # list
# for i in data['emp_details']:
#     print(i)
  
# # Closing file
# f.close()