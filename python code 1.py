a = 132
b = 45
n = 30
fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'
print("bitwise NOT:")
print(fmt0.format('a'), fmt1.format(a,a,a))
print('-'*n)
print(fmt0.format('~a'),fmt1.format(~a&0xFF,~a&0xFF,~a&0xFF))

a = 132
b = 45
n = 30
fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'
print("bitwise leftshift:")
print(fmt0.format('a'), fmt1.format(a,a,a))
print('-'*n)
print(fmt0.format('~a'),fmt1.format(a<<2&0xFF,a<<2&0xFF,a<<2&0xFF))

a = 132
b = 45
n = 30
fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'
print("bitwise rightshift:")
print(fmt0.format('a'), fmt1.format(a,a,a))
print('-'*n)
print(fmt0.format('~a'),fmt1.format(a>>2&0xFF,a>>2&0xFF,a>>2&0xFF))