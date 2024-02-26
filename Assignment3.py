dict=[{"id":1,"name":"Aaliya"},{"id":2,"name":"Fathima"},{"id":3,"name":"Liba"}]
id=33
filter=list(filter(lambda item: item["id"]==id, dict))
if filter:
    print(filter)
else:
    print("Not Found")