#_01_데이타타입 # ***********************
# -- 데이터타입 6
# ***********************
''' 
Python has five standard data types −

#데이터와 자료구조로 나누어야한다. 데이터는 단수이고, 자료구조는 복수이다. 아래 다섯 문자를 타입이라고 한다.
Numbers : int, float, complex # 단수형이다.
String #string은 문자열이고, 열은 복수형이다. 복수형이다. 
List # 복수형이다.
Tuple # 복수형이다.
Dictionary #복수형이다.
'''
# Python Strings 
hello = 'Hello World!'

print (hello)          # Hello World!
print (hello[0])       # H
print (hello[2:5])     # llo
print (hello[2:])      # llo World!
print (hello * 2)      # Hello World!Hello World!
print (hello + "TEST") # Hello World!TEST

# Python Lists 
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # ['abcd', 786, 2.23, 'john', 70.200000000000003]
print (list[0])       # abcd
print (list[1:3])     # [786, 2.23]
print (list[2:])      # [2.23, 'john', 70.200000000000003]
print (tinylist * 2)  # [123, 'john', 123, 'john']
print (list + tinylist) # ['abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john']

# Python Tuples
''' Tuples can be thought of as read-only lists '''
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # ('abcd', 786, 2.23, 'john', 70.200000000000003)
print (tuple[0])        # abcd
print (tuple[1:3])      # (786, 2.23)
print (tuple[2:])       # (2.23, 'john', 70.200000000000003)
print (tinytuple * 2)   # (123, 'john', 123, 'john')
print (tuple + tinytuple) # ('abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john')

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list

# Python Dictionary
''' Python's dictionaries are kind of hash-table type '''
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # This is one
print (dict[2])           # This is two
print (tinydict)          # {'name': 'john', 'dept': 'sales', 'code': 6734}
print (tinydict.keys())   # dict_keys(['name', 'dept', 'code'])
print (tinydict.values()) # dict_values(['john', 'sales', 6734])

# Python Sets