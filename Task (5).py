new_dict = {'name':['Orxan','Ali','Fuad','Maqa']} 
values = new_dict.values()
a = 0
for i in values: 
    for n in i:
        a = a + 1
        print(a,".", n)

