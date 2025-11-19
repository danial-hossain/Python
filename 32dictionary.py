info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible')) # get wont throw error if the item is not in the dictionary,while []does

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())


for key in info.keys():
  print(info[key])
  #print(f"The value to the {key} is {infor[key]}")




info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

for key,value in info.values():
   print(f"The value to the {key} is {info[key]}")

