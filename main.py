from dynamicVector import DynamicVector

vec = DynamicVector()
vec.push(10)
vec.push(20)
vec.push(30)
vec.pop()
vec.push(40)

print("Vector:", vec)
print("Longitud:", len(vec))
print("Elemento en la posición 1:", vec[1])
print(vec.__repr__())
