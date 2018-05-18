date = '1000,Cathy,女'
mydict = {}
(mydict['id'],mydict['name'],mydict['sex']) = date.split(',')

print('id:' + mydict['id'])
print('name:' + mydict['name'])
print('sex:' + mydict['sex'])
