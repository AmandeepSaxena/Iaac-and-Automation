import json
req_file = "myfile.json"

#to convert json to dict data json.load(file_object)
fo = open(req_file,'r')
print(json.load(fo))

#to get a key value 
print(json.load(fo).get('key'))

#to store data in json
my_dict = {'Name':'Rocky','Age':20 }
fo = open(req_file,'w')
json.dump(my_dict,fo, indent=4) #indent gives indentation to final json file

fo.close

