install:
  python3 setup.py install
  
build:
  python3 setup.py bdist_wheel sdist
  echo dont forget to rename -py3 to -py2.py3
