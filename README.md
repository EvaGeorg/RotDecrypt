# RotDecrypt
RotDecrypt is a tool for decrypting text encrypted with basic rotation algorithms

<h2>Usage</h2> 

Using RotDecrypt is very simple since all you need to do is pass the file that you want to decrypt as a first parameter
and then the tool generates 26 files, tries all the possible rotations, since whatever the number of rotation is the tool
calculates %26.

```
$ python rotdecrypt.py file.txt
```

<h2>Requirements</h2> 

To be able to use RotDecrypt you need to have python3.8 installed on your system. For more information on **python** installation
and usage you can find [here](https://www.python.org/)

