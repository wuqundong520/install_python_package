

## environment
ubuntu 16.04 x64
anaconda3.5.2.0
python3.6

### prepare
pip install pyinstaller

### pack single file
```angular2html
LD_LIBRARY_PATH=/home/leo/.pyenv/versions/anaconda3-5.2.0/lib/ pyinstaller -F single.py 
LD_LIBRARY_PATH=/home/leo/.pyenv/versions/anaconda3-5.2.0/lib/ pyinstaller -F single.py  --hidden-import mysql --hidden-import other --exclude-module matplotlib  --exclude-module matplotlib.pyplot --exclude-module plt  --exclude-module pylab 
```
> LD_LIBRARY_PATH should contain libpython.so.xxxxx
> -F means single file generation
### pack multi file
```angular2html
LD_LIBRARY_PATH=/home/leo/.pyenv/versions/anaconda3-5.2.0/lib/ pyinstaller main.py -p ./model1.py -p ./dir1/model2.py -p ./dir2/model3.py
```


### 参考需要解决的问题
+ ImportError: No module named 'setuptools._vendor' .... .... .... AttributeError: 'str' object has no attribute 'items'
> pip install --upgrade setuptools
> pip install --upgrade urllib3



### READING
https://pythonhosted.org/PyInstaller/hooks.html
https://stackoverflow.com/questions/15229658/pyinstaller-what-are-hiddenimports-and-hooks
