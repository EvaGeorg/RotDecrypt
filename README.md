# RotDecrypt
RotDecrypt is a tool for decrypting text encrypted with basic rotation algorithms

<h2>Usage</h2> 

Using RotDecrypt is very simple since all you need to do is pass the file that you want to decrypt as a first parameter
and then the tool generates 26 files, tries all the possible rotations, since whatever the number of rotations is it
calculates mod 26.

```
$ python rotdecrypt.py file.txt
```


<h2>Example</h2>

The standard alphabet is abcdefghijklmnopqrstuvwxyz, rotating it by 1 it would mean that a is replaced with b, b with c and so on, rotating it by 3 would mean that a is replaced by d, b by e and so on, rotating it by 36, it would mean a=(position_of_a+36)%26.


<h2>Requirements</h2> 

To be able to use RotDecrypt you need to have python3.8 installed on your system. For more information on **python** installation
and usage you can find [here](https://www.python.org/)


<h2>Install</h2> 

To install the tool you can use the **wget** and type the following command in terminal
```
$ wget https://github.com/EvaGeorg/RotDecrypt/blob/master/rotdecrypt.py
```

<h2>License</h2> 

Copyright 2020 - Eva Georgieva

This tool is available for anyone to use it free of charge.



