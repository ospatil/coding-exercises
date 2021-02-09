# Bitwise AND: &
print(f"{3:>2} = {3:>08b}")  # 3 = 00000011
print(f"{6:>2} = {6:>08b}")  # 6 = 00000110
print(f"3 & 6 = {3&6:>08b}")  # 3 & 6 = 00000010


# bitwise OR: |
print(f"3 = {3:08b}")  # 3 = 00000011
print(f"6 = {6:08b}")  # 6 = 00000110
print(f"3 | 6 = {3|6:08b}")  # 3 | 6 = 00000111


# bitwise XOR: ^
# Returns 1 when 2 bits are different else 0
print(f"3 = {3:08b}")  # 3 = 00000011
print(f"6 = {6:08b}")  # 6 = 00000110
print(f"3 ^ 6 = {3^6:08b}")  # 3 ^ 6 = 00000101

# bitwise NOT: ~
"""
Negative numbers are stored as two's complement.
Their leading bit is 1.

Now consider an example:
x  = 000 ... 01
~x = 111 ... 10

For 32-bit numbers, (2^32 - 1) is all 1 bits.
For a -ve number x, 2s complement is (2^32 - x)

Basically we took away 1 from (2^32 -1) so the value is
(2^32 - 1 - 1) i.e. (2^32 - 2)
Comparing it to (2^32 - x)
x = -2

Another example:
x = 5 i.e. 000 ... 0101
~x = 111 ... 1010

So, basically we subtracted 5 in case of ~x (i.e. inset bits for 5)
i.e. 2^32 - 1 - 5 = 2^32 - 6
Therefore, x = -6
"""
print(f"5 = {5:08b}")  # 5 = 00000101
print(f"~5 = {~5:08b} = {~5}")  # ~5 = -0000110 = -6


# Left shift: <<
print(f"3 = {3:08b} = 3 * 2^0")  # 3 = 00000011 = 3 * 2^0
print(f"3 << 1 = ({3 << 1:08b}) = 3 * 2^1")  # 3 << 1 = (00000110) = 3 * 2^1
print(f"3 << 2 = ({3 << 2:08b}) = 3 * 2^2")  # 3 << 2 = (00001100) = 3 * 2^2
print(f"3 << 3 = ({3 << 3:08b}) = 3 * 2^3")  # 3 << 3 = (00011000) = 3 * 2^3


# Right shift: >>
x = 33
print(f"{x} = {x:>08b} = {x} // 2^0")
# 33 = 00100001 = 33 // 2^0

print(f"{x} >> 1 = ({x >> 1:08b}) = {x >> 1} = {x} // 2^1")
# 33 >> 1 = (00010000) = 16 = 33 // 2^1

print(f"{x} >> 2 = ({x >> 2:08b}) = {x >> 2} = {x} // 2^2")
# 33 >> 2 = (00001000) = 8 = 33 // 2^2

print(f"{x} >> 3 = ({x >> 3:08b}) = {x >> 2} = {x} // 2^3")
# 33 >> 3 = (00000100) = 8 = 33 // 2^3
