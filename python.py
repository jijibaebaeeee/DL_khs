리스트 형으로 저장 => .split(), .keys(), .values()
튜플 형으로 저장 => .items()
a = 10
b = 11.4
print(a,h) -> 10 11.4
print(a, 100, 200, b) -> 10 100 200 11.4
print(a, 100, 200, b, sep=',', end='...')
-> 10, 100,200,11.4...
a,b -> (10, 11.4)
a -> 10
a
b -> 11.4

a = 10
b = 11.4
c = None
type(a), type(b), type(c)
->(int, float, NoneType)
type(b) -> float

c = a > b
print(c, type(c))
->False <class 'bool'>

#-----------여기서 부터 string에 대한 것 (string의 slicing은 생략함)---------------
#string

a = 'hello world'
b = a.upper()
print(a)-> hello world 
print(b)-> HELLO WORLD
a.replace('h','hhh')->'hhhello world'
b.replace('h','hhh')->'HELLO WORLD'

temp = 25.5
prob = 80.0
a = '오늘 기온 {}, 비올 확률{}'.format(temp,prob)
print(a) -> 오늘 기온 25.5, 비올 확률 80.8

b = 'hello world what a nice world'
b.split() -> ['hello', 'world', 'what', 'a', 'nice', 'world']
b.split('w') -> ['hello', 'orld', 'hat a nice', 'orld']

b = 'hello world'
c = b.split()
print(b) -> 'hello world'
print(C) -> ['hello', 'world']
type(b), type(c) -> (str, list)

# --------------여기서부터 list, tuple, dictionary------------(list의 slicing, append()은 생략)
# list
a = 'hello world'
b = list(a)
print(b) -> ['h','e','l','l','o', 'w','o','r','l','d']
c = (1, 2, 3)
d = list(c)
print(c) -> (1, 2, 3)
print(d) -> [1, 2, 3]
e = a.split()
print(e)
['hello', 'world']

a = 'hello world'
b = 'jello world'
c = 'j' + a[1:]
d = a.replace('h','j')
print(b)->jello world
print(c)->jello world
print(d)->jello world
print(a)->hello world

a = [1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b)
print(a)->[1,2,3,4,5,6,7,8,9,10]
a += b
print(a)->[1,2,3,4,5,6,7,8,9,10]

a = [1,2,3,4,5]
a.insert(1, 10)
print(a)->[1,10,2,3,4,5]

a = [1,2,20,4,5]
a.remove(20)
print(a)->[1,2,4,5]

a = [1,2,2,4,5]
a.remove(2)
print(a)->[1,2,4,5]

a = [1,2,3,4,5]
a.pop
print(a)->[1,2,3,4]

a = [1,2,3,4,5]
b = a.pop(1)
print(a)->[1,3,4,5] # 헷갈림
print(b)-> 2

a = [10, 20, 30, 30, 50]
a.index(30) -> 2

a = [0,2,8,3,5,9,-1]
a.sort()
print(a)->[-1,0,2,3,5,8,9]
a.sort(reverse=True)
print(a)->[9,8,5,3,2,0,-1]

a = [0,2,8,3,5,9,-1]
b = sorted(a)
print(a)->[0,2,8,3,5,9,-1]
print(b)->[-1,0,2,3,5,8,9]

#tuple
b = 1, 2, 3
print(type(b))-><class 'tuple'>

#dictonary
a = {'korea':'seoul', 'canada':'ottawa', 'usa':'washington'}
print(type(a))-><class 'dict'>
print(a['korea'])->seoul
print(a['usa'])->washington
a['japan'] = 'tokyo'
print(a)
->{'korea':'seoul', 'canada':'ottawa', 'usa':'washington', 'japan':'tokyo'}
a['korea'] = 'cheongju'
print(a)
->{'korea':'cheongju', 'canada':'ottawa', 'usa':'washington', 'japan':'tokyo'}

a = {'a':1,'b':2,'c':3}
b = {'a':2,'d':4,'e':5,'f':6}
a.updata(b)
print(a) -> {'a':2,'b':2,'c':3,'d':4,'e':5,'f':6}
del a['b']
print(a) -> {'a':2,'c':3,'d':4,'e':5,'f':6}
c = 'b' in a
print(c) -> False
a.clear()
print(a) -> {}
a = {'a':1, 'b':2, 'c':3}
print(a.get('d'))
print(a['d'])

a = {'a':1,'b':2,'c':3}
print(a) -> {'a':1,'b':2,'c':3}
print(a.keys()) -> dict_keys(['a','b','c'])
print(a.values()) -> dict_values([1,2,3])

a = {1,1,2,3,4,4,5,3,1}
print(a) -> {1,2,3,4,5}

a = [1,1,2,3,4,4,5,3,1]
print(a) -> [1,1,2,3,4,4,5,3,1]
b = set(a)
print(b) -> [1,2,3,4,5]



#-------------------2번째 python ppt----------------(기본 문법 생략)
a = {'korea':'seoul', 'canada':'ottawa', 'japan':'tokyo'}
b = list(a.items())
print(type(b)) -> <class 'list'>
print(b)->[('korea','seoul'), ('canada', 'ottawa'), ('japan','tokyo')]

a = [10,20,30,40]
for index, value in enumerate(a):
    print(index, value)
-> 0 10
   1 20
   3 30
   4 40

b = list(range(10))
c = list(range(10, 20))
d = list(range(10, 20, 2))
print(b)->[0,1,2,3,4,5,6,7,8,9]
print(c)->[10,11,12,13,14,15,16,17,18,19]
print(d)->[10,12,14,16,18]

#flexibel arguments
def test(*args):
    print(type(args))
    for item in args:
        print(item)
test() -> <class 'tuple'>
test(1)->
<class 'tuple'>
1
test(1,2,3)->
<class 'tuple'>
1
2
3

def test2(**x):
    print(type(x))
    for key in x:
        print(key, x[key])
    return

test2(a=1, b=2, c=3, d=4, name='kang')
<class 'dict'>
a 1
b 2 
c 3 
d 4
name kang

#function
square2 = lambda x:x**2
print(square2(5))->25
print(type(square2))
-> <class 'function'>

#lambda function
def str_len(s):
    return len(s)

strings = ['bob','charles','alexander','teddy','jane']
strings.sort(key=str_len) # = strings.sort(key=lambda s:len(s))
print(strings)
->['bob', 'jane','teddy','charles','alexander']

def even(n):
    return n%2==0

a = [10, 13, 2, 3, 8, 9,17]
b = list(filter(even,a)) # = list(filter(lambda n:n%2==0, a))
print(b) -> [10, 2, 8]

a = [10, 13, 2, 3, 8, 9,17]
b = list(map(lambda n:n%2==0, a))
print(b)
-> [True, False, True, False, True, False, False]
b = list(map(lambda n:n**2, a))
print(b)
-> [100, 169, 4, 9, 64, 81, 289]

import functools

a = [1, 2, 3, 4, 5]
b = functools.reduce(lambda x,y:x+y, a)
print(b)->15



#----------------여기서부터 3번째 ppt 자료------------------------
# class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Eat(self, food):
        print('{}는 {}를 먹는다.'.format(self.name, food))
    def Sleep(self, hour):
        print('{}는 {}동안 잔다.'.format(self.name, hour))
    def Work(self, hour):
        print('{}는 {}동안 일한다.'.format(self.name, hour))


class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Work(self, hour):
        #super().Work(hour) super사용시 부모, 자식 모두 츨력된다.
        print('{}는 {}동안 공부한다.'.format(self.name, hour))

class Employee(Person): # 여기에 Person을 적게되면 위의 클래스를 상속받음
    def __init__(self, name, age):
        self.name = name
        self.age = age



bob = Person('Bob',30)
bob.Eat('BBQ')
bob.Sleep(8)
bob.Work(10)

# __str__ , __add__, __sub__ 써보기
class Point2D:
    def __init__(self, x, y):
        






