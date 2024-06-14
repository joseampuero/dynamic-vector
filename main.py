from dynamicVector import DynamicVector
from tlb import TLB
import constants

# vec = DynamicVector()
# vec.push(1)
# vec.push(2)
# vec.push(3)
# vec.pop()
# vec.push(4)
# vec.push(5)
# vec.push(6)
# vec.push(7)
# vec.push(8)
# vec.push(9)
# vec.push(10)
# vec.push(11)
# vec.push(12)

# print("Vector:", vec)
# print("Longitud:", len(vec))
# print("Elemento en la posición 1:", vec[1])
# print(vec.__repr__())


tlb_fifo = TLB(size=4, replacement_policy=constants.FIFO)

tlb_fifo.update(0x100, 0x200)
tlb_fifo.update(0x200, 0x300)
tlb_fifo.update(0x300, 0x400)
tlb_fifo.update(0x400, 0x500)

direccion_fisica = tlb_fifo.lookup(0x100)
print("Dirección física para la dirección virtual 0x100:", direccion_fisica)  # Salida esperada: 0x200

direccion_fisica = tlb_fifo.lookup(0x500)
print("Dirección física para la dirección virtual 0x500:", direccion_fisica)  # Salida esperada: None

for clave, valor in tlb_fifo.entries.items():
    print(f"{hex(clave)}, {hex(valor)}")