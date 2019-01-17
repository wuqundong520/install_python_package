

## environment
ubuntu 16.04 x64
anaconda3.5.2.0
python3.6

### prepare
pip install pyinstaller

### pack single file
```angular2html
LD_LIBRARY_PATH=/home/leo/.pyenv/versions/anaconda3-5.2.0/lib/ pyinstaller single.py
```
> LD_LIBRARY_PATH should contain libpython.so.xxxxx

### pack multi file
```angular2html
LD_LIBRARY_PATH=/home/leo/.pyenv/versions/anaconda3-5.2.0/lib/ pyinstaller main.py -p ./model1.py -p ./dir1/model2.py -p ./dir2/model3.py
```






