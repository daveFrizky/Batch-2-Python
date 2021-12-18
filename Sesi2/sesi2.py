# x = 10 - 15 --> tampil
x = 13
sunny = True
# sunny = False
# if x >= 10 and x <= 15 and sunny == False:
# if x >= 10 and x <= 15 and not sunny:
 
# if x >= 10 and x <= 15 and sunny == True:
if x >= 10 and x <= 15 and sunny:
    print(x)


total_purchase = 1000
var=10
# if 'a' in 'bar':
if 'aa' in 'bar':
    print('foo')
elif total_purchase >= 850:
    print('discount 30%')
elif 1/0:
    print("This won't happen")
elif var:
    print("This won't either")


# raining = False # --> 'beach
raining = True    # --> library
print("Let's go to the", 'beach' if not raining else 'library')
# prin("a", "haaia")
 
# 'beach' if not raining else 'library'
# <expr1> if <conditional_expr> else <expr2>
# if not raining --> if raining == False
#                        False  == False ==> True ==> Beach // expr1
# output:
# Let's go to the



#  ternary if contoh 1
#Ternary if #1
# # raining = False # --> 'beach
raining = True    # --> library
print("Let's go to the", 'beach' if not raining else 'library')
# if not raining:
#     print("Let's go to the beach")
# else:
#     print("Let's go to the library")
# # prin("a", "haaia")
 
# # 'beach' if not raining else 'library'
# # <expr1> if <conditional_expr> else <expr2>
# # if not raining --> if raining == False
# #                        False  == False ==> True ==> Beach // expr1
# # output:
# # Let's go to the
 
 


#  ternary if contoh 2
#Ternary if #2
age = 12
s = 'teen' if age < 21 else 'adult'
# if age < 21:
#     s = 'teen'
# else:
#     s = 'adult'
print(s)
 
 



# # #Ternary if #3
'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'
 
# if ('qux' in ['foo', 'bar', 'baz']):
#     print('yes')
# else:
#     print('no')


# # #Ternary if #4
# m = a if a > b else b
 
# m = b
# if a > b :
#     m = a
 
# m = 0
# if a > b:
#     m = a
# else:
#     m = b


# While
n = 5
while n > 0: #5 4 3 2 1 0xxxx
    n -= 1 # n = n - 1  # 4 3 2 1 0
    print(n)    #4 3 2 1 0

# While 2
i = 1
while i < 6: # 1 2 3 4 5 6xxxx
  print(i)   # 1 2 3 4 5
  i += 1     # 2 3 4 5 6


# Break
#break
i = -1
while i < 6:
    print(i)
    if i == 2:
        break
    i += 1
 
print('print yang di luar loop')


#  while with continue
# continue
n = 5
while n > 0:       # 5 4 3 2 1 0
    n -= 1         # 4 3 2 1 0
    if n == 2:     # x x 2 x x
        continue   #     2
    print(n)       # 4 3 x 1 0
print('Loop ended.')

#  while else
# while else
n = 5
while n > 0:       # 5 4 3 2 1 0xxx
    n -= 1         # 4 3 2 1 0
    print(n)       # 4 3 2 1 0
else:              #                [v] executed
    print('Loop done.')


#  while, else, with break
#while else met with break
n = 5
while n > 0:        # 5 4 3
    n -= 1          # 4 3 2
    print(n)        # 4 3 2
    if n == 2:      # x x 2
        break       #     2terminates a loop entirely
else:               
    print('Loop done.')


# dictionary x loop
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d: # equals to d.keys()
    print(k)


#  [added]
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:     # 'foo'      'bar'      'baz'
    print(d[k]) # d['foo']   d['bar']   d['baz']
                #    1          2          3


# no context d.items()
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in d.items():  # -->  (value1, value2)
                        #       'foo', 1
                        #       'bar', 2
                        #       'baz', 3
    print(k, ":", v)

# another no context
for k, v in d.items():
    for kunci, nilai in d.items():
        print(d)
    break


# [updated]
# x = range(5)       # --> 0 1 2 3 4
# x = range(1,5)     # --> 1 2 3 4
# x = range(2,20)    # --> 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
x = range(0,10, 4) # in java, php, c++ // for ( i=0, i<10; i+=4)
                   # --> 0 4 8
for n in x :
    print(n)

# for x break
#for break
for i in ['foo', 'bar', 'baz', 'qux']:  # 'foo'     'bar'
    if 'b' in i:                        # x         'bar'
        break                           #            breakk // terminated
    print(i)                            # 'foo'


# for x continue
#for continue
for i in ['foo', 'bar', 'baz', 'qux']:  # 'foo' 'bar'       'baz'       'qux'
    if 'b' in i:                        # x     'bar'       'baz'       x
        continue                        #       continue    continue    
    print(i)                            # 'foo'                         'qux'


# for else met break
# for else met break
for i in ['foo', 'bar', 'baz', 'qux']:  # 'foo'  'bar'
  if i == 'bar':                        # x      'bar'
    break                               #         breakk // terminated a loop entirely
  print(i)                              # 'foo'
else:                                   #          skipped/ignored too
  print('Done.')
