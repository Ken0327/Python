# Two polynomial sum by array
# A(x) = 3x^4 + 7x^3 + 6x + 2
# B(x) = x^4 + 5x^3 + 2x^2 + 9
PolyA = [4,3,7,0,6,2]
PolyB = [4,1,5,2,0,9]
Items = 6

def PrintPoly(poly, items):
	MaxExp = poly[0]
	for i in range(1, poly[0]+2):
		MaxExp -=1
		if (poly[i] != 0):
			if (MaxExp + 1 != 0):
				print('%dX^%d' %(poly[i], MaxExp + 1), end='')
			else:
				print('%d' %poly[i], end='')
			if MaxExp >=0:
				print('%c' %'+', end='')
	print()

def PolySum(poly1, poly2):
    result = [None] * Items
    result[0] = poly1[0]
    for i in range(1, poly1[0]+2):
        result[i] = poly1[i] + poly2[i]
    PrintPoly(result, Items)

print('Polynomial A=> ', end='\t')
PrintPoly(PolyA, Items)
print('Polynomial B=> ', end='\t')
PrintPoly(PolyB, Items)
print('A + B => ', end='\t')
PolySum(PolyA, PolyB)