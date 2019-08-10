Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:\Users\usha kiran\Desktop\Trail\S\Serial.py ===========
enter 1 to ON and 0 to OFF:1
enter 1 to ON and 0 to OFF:0
enter 1 to ON and 0 to OFF:1
enter 1 to ON and 0 to OFF:0
enter 1 to ON and 0 to OFF:1
enter 1 to ON and 0 to OFF:0
enter 1 to ON and 0 to OFF:1
enter 1 to ON and 0 to OFF:0
enter 1 to ON and 0 to OFF:1
enter 1 to ON and 0 to OFF:0
enter 1 to ON and 0 to OFF:
Traceback (most recent call last):
  File "C:\Users\usha kiran\Desktop\Trail\S\Serial.py", line 18, in <module>
    on_off()
  File "C:\Users\usha kiran\Desktop\Trail\S\Serial.py", line 7, in on_off
    on_off()
  File "C:\Users\usha kiran\Desktop\Trail\S\Serial.py", line 10, in on_off
    on_off()
  File "C:\Users\usha kiran\Desktop\Trail\S\Serial.py", line 7, in on_off
    on_off()
  File "C:\Users\usha kiran\Desktop\Trail\S\Serial.py", line 10, in on_off
    on_off()
  File "C:\Users\usha kiran\Desktop\Trail\S\Serial.py", line 7, in on_off
    on_off()
  File "C:\Users\usha kiran\Desktop\Trail\S\Serial.py", line 10, in on_off
    on_off()
  File "C:\Users\usha kiran\Desktop\Trail\S\Serial.py", line 7, in on_off
    on_off()
  File "C:\Users\usha kiran\Desktop\Trail\S\Serial.py", line 10, in on_off
    on_off()
  File "C:\Users\usha kiran\Desktop\Trail\S\Serial.py", line 7, in on_off
    on_off()
  File "C:\Users\usha kiran\Desktop\Trail\S\Serial.py", line 10, in on_off
    on_off()
  File "C:\Users\usha kiran\Desktop\Trail\S\Serial.py", line 15, in on_off
    a.write(b'0')
  File "C:\Python\Python37\lib\site-packages\serial\serialwin32.py", line 315, in write
    raise SerialException("WriteFile failed ({!r})".format(ctypes.WinError()))
serial.serialutil.SerialException: WriteFile failed (PermissionError(13, 'The device does not recognize the command.', None, 22))

>>> import Nino
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import Nino
ModuleNotFoundError: No module named 'Nino'
>>> 
======= RESTART: C:/Users/usha kiran/Desktop/python_practice2/Nino.py =======
>>> import Nino
>>> Nino.Sirena('usha','bangalore')
nino name place
>>> import importlib
>>> importlib.reload(Nino)
<module 'Nino' from 'C:/Users/usha kiran/Desktop/python_practice2\\Nino.py'>
>>> Nino.Sirena('usha','bangalore')
Nino name place
>>> import importlib
>>> importlib.reload(Nino)
<module 'Nino' from 'C:/Users/usha kiran/Desktop/python_practice2\\Nino.py'>
>>> Nino.Sirena('usha','bangalore','ban')
Nino name place address
>>> tap=(1,2,3,4,[7,8],'a')
>>> print(tap[4])
[7, 8]
>>> tapa[4][1]=5
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tapa[4][1]=5
NameError: name 'tapa' is not defined
>>> tap[4][1]=5
>>> tap[4]
[7, 5]
>>> tap[0]=3
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tap[0]=3
TypeError: 'tuple' object does not support item assignment
>>> tap[0:2]
(1, 2)
>>> tap=(1,3,5,7,9,11)
>>> t=list(tap)
>>> t
[1, 3, 5, 7, 9, 11]
>>> t[0]='s'
>>> t[1]='i'
>>> t[2]='r'
>>> t[3]='e'
>>> t[4]='n'
>>> t[5]='a'
>>> tap=('s','i','r','e','n','a')
>>> tap
('s', 'i', 'r', 'e', 'n', 'a')
>>> t1=(1,2,3)
>>> t2=(4,5,6)
>>> t1+t2
(1, 2, 3, 4, 5, 6)
>>> del(t1)
>>> t1
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    t1
NameError: name 't1' is not defined
>>> del[0:2]
SyntaxError: invalid syntax
>>> t1=(1,2,3,4)
>>> l1=list(t1)
>>> l1
[1, 2, 3, 4]
>>> tap=('v','i','v','a','r','t','t','a','n','a')
>>> print(count.tap('a'))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(count.tap('a'))
NameError: name 'count' is not defined
>>> print(tap.count('a'))
3
>>> 'q' in tap
False
>>> 'a' in tap
True
>>> 'a' not in tap
False
>>> tup=('a','b','c')
>>> t=str(tup)
>>> t
"('a', 'b', 'c')"
>>> for name in ('a','b','c'):
	print("hai",name)

	
hai a
hai b
hai c
>>> 
