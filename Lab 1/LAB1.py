"""
1- List Operations 
2- Set Operations (5) """
a = [2,3,4,4,4,5,6]
a.append('grow')
print(a)
print(a.count(4))
b =[5,6,7]
print(sum(b))
b.reverse()
print(b)

c=['apple','Chamomile','Dead outside','Alive inside']
c.pop(1)
print(c)
print(c.index('Dead outside'))
a.extend(c)
print(a)

a={'Bell','Quantized','Dirac'}
b ={'State','Hadamard','Toffoli','Bell'}
c=a.union(b)
print(c)
d=a&b
print(d)

b.intersection_update(a)
print(b)

set1={1,2,3,4}
set2={9,8,7,6}
set1.update(set2)
print(set1)
z = {'ader','nada','vectorised','chromatic'}
y={'forca','nada','chromatic','gilgamesh'}
t=z-y
print(t)
var1 = z.symmetric_difference(y)
print(var1)