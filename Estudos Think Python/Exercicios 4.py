t  =[1,2,3, [1,2,3,4,1],[1,2,3,4,9]]
new_list = []
soma = [new_list.extend(x) if type(x) is list else new_list.append(x) for x in t]

print(new_list)


