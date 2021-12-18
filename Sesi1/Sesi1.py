print(123123123123123123123123123123123123123123123123 + 1)
print(10)
print(2**2)

print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)

print()

print("Hacktiv8")
print(type("Hacktiv8"))
print("This string contains a single quote (') character.")
print("This string contains a double quote (\") character.")

print()

print(type(True))
print(type(False))
print(100 > 200) #False
print(100 == 200) #False
print(100 < 200) #True

print()

n = 300
print(n)
a = b = c = n
print(a, b, c)

print()


name = "Hacktiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)

print()

a = 10
b = 20
print(a + b)
# print(a + b – 5)

print()

a = 4
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

print()

a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

print()

s = 'foo'
t = 'bar'
print(s + t )
print(s * 4)
print(s.capitalize())
print(s.lower())
print(s.swapcase())

print()

a = ['foo', 'bar', 'baz', 'qux']
a[2] = 10
a[-4] = 20
print(a)


print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)

print()

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(t[0])
print(t[-1])

(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')
print(s1,s2)

print()

MLB_team = {    'Colorado': 'Rockies',    'Boston': 'Red Sox',    'Minnesota': 'Twins'}
print(MLB_team['Minnesota'])
MLB_team['Kansas City'] = 'Royals'
print(MLB_team)

del MLB_team['Minnesota']
print(MLB_team)

print ("MLB_team['Colorado']: ", MLB_team['Colorado'])

print(MLB_team.items())
print(MLB_team.keys())
print(MLB_team.values())




print()

person = {}
person['fname'] = 'Hack'
person['lname'] = '8'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person)
print(person['children'][1])
print(person['pets'])