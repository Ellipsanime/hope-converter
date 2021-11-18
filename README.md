# hope-converter

All hope abandon ye who use python v2.7! Keep calm and switch to python 3.10 at least! On account of this project you will be able to:

 1. Convert any of your python 2 code to a decent python version at the measure of possible(please refer to [2to3](https://docs.python.org/3/library/2to3.html))
 2. Convert any of your python 3 code to the version 2 using coconut compilation. 

The only purpose of this project is to help people to avoid any manual contact with python 2. If somehow you have to maintain python 2 and 3 compatibility this project can be helpful.   

### Usage

First convert your python 2 code to python 3

```bash
python app.py from2to3 $SOURCE $DEST --verbose
```

Then convert your python 3 version to the python 2 when needed

```bash
python app.py coconify $SOURCE $DEST --version $PYTHON_VERSION --verbose
```
