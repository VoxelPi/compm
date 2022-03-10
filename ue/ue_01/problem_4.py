d = {'key1':[1,2,{'key2':['do not get confused',{'tough':[1,2,[['get me']]]}]}]}
print(f"The string is: {d['key1'][2]['key2'][1]['tough'][2][0][0]}")

d = {'key2':[1,[[],{'bug':{'bug':'get me'}}]]}
print(f"The string is: {d['key2'][1][1]['bug']['bug']}")

def reverse_dict(dict):
    output = {}
    for (key, value) in dict.items():
        output[key[::-1]] = value
    return output

print(reverse_dict({'key1' : 'val1', 'key2' : 'val2'}))
