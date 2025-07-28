studentdata = {"ID":
               {"Name":"Rinmolu" ,"Age":12,"Grade":8},
               "ID2":
               {"Name":"Lore" ,"Age":12,"Grade":8},
               "ID3":
               {"Name":"Hanzhou" ,"Age":12,"Grade":8},
               "ID4":
               {"Name":"Viraaj" ,"Age":12,"Grade":8},
               "ID5":
               {"Name":"Abhang" ,"Age":12,"Grade":8},}
result = {}
for key,value in studentdata.items():
    if value not in result.values():
        result[key] = value
print(studentdata)