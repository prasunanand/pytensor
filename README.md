# pytensor
Buiding a tensor library in Python (C extension) for practice

## Install extension

```python
python setup.py install

# To remove
python setup.py clean
```

To test

```python
prasun@prasun-xps:~/dev/pytensor$ python
Python 3.7.3 (default, Mar 27 2019, 22:11:17) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import ctensor
>>> ctensor.hello()
Hello World!
>>> ctensor.system("ls -l")
total 24
drwxr-xr-x 4 prasun prasun 4096 Jul 18 19:20 build
-rw-r--r-- 1 prasun prasun 1520 Jul 18 16:00 LICENSE
-rw-r--r-- 1 prasun prasun  200 Jul 18 19:31 README.md
-rw-r--r-- 1 prasun prasun  435 Jul 18 19:20 setup.py
drwxr-xr-x 4 prasun prasun 4096 Jul 18 17:11 tensor
drwxr-xr-x 3 prasun prasun 4096 Jul 18 16:57 test
0
>>> exit()
```


## Tests
python -m unittest
