Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> open
<built-in function open>
>>> open ('prueba')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'prueba'
>>> open ('prueba')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'prueba'
>>> open ('prueba')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'prueba'
>>> f=open('prueba')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'prueba'
>>> f=open('prueba.Python')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'prueba.Python'
>>> open ('prueba.py')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'prueba.py'
>>> open ('prueba.py')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'prueba.py'
>>> directory
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'directory' is not defined
>>> dir


<built-in function dir>
>>> >>> >>> dir
<built-in function dir>
>>> 
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> ls

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ls' is not defined
>>> >>> f=open('prueba.Python')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'prueba.Python'
>>> f=open('prueba.Python')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'prueba.Python'
>>> f=open('prueba.py')
>>> f
<_io.TextIOWrapper name='prueba.py' mode='r' encoding='cp1252'>
>>> f.tell()
0
>>> f.readlines()
["print('hola')"]
>>> f.readlines()
[]
>>> f.readlines()
[]
>>> f.readlines()
[]
>>> f.readlines()
[]
>>> f.readlines()
[]
>>> f=open('prueba.py','rb')
>>> f
<_io.BufferedReader name='prueba.py'>
>>> dir(f)
['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_dealloc_warn', '_finalizing', 'close', 'closed', 'detach', 'fileno', 'flush', 'isatty', 'mode', 'name', 'peek', 'raw', 'read', 'read1', 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
>>> s=open('prueba.py')
>>> s
<_io.TextIOWrapper name='prueba.py' mode='r' encoding='cp1252'>
>>> type(f)
<class '_io.BufferedReader'>
>>> type(s)
<class '_io.TextIOWrapper'>
>>> f=open('prueba.py',B)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'B' is not defined
>>> f=open('prueba.py','b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Must have exactly one of create/read/write/append mode and at most one plus
>>> f.read(5)
b'print'
>>> type(f)
<class '_io.BufferedReader'>
>>> f=open('prueba.py','b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Must have exactly one of create/read/write/append mode and at most one plus
>>> f=open('prueba.py','B')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid mode: 'B'
>>> f=open('prueba.py','l')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid mode: 'l'
>>> f=open('prueba.py','')