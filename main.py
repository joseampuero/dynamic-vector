from dynamicVector import DynamicVector

vec = DynamicVector()
vec.push(1)
vec.push(2)
vec.push(3)
vec.pop()
vec.push(4)
vec.push(5)
vec.push(6)
vec.push(7)
vec.push(8)
vec.push(9)
vec.push(10)
vec.push(11)
vec.push(12)

print("Vector:", vec)
print("Longitud:", len(vec))
print("Elemento en la posición 1:", vec[1])
print(vec.__repr__())
