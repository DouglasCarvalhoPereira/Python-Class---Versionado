t  =[1,2,3,[1,2,3,4,1],[1,2,3,4,9],8,8,9,4]
new_list = []
soma = [new_list.extend(x) if type(x) is list else new_list.append(x) for x in t]

print(sum(new_list))


