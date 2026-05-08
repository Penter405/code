# section .data
###### any variable set here is like ``int x=5;`` , set variable with pre data inside
## define a variable
```
name_of_variable  size_of_variable  the_data
```
## the table: size_of_variable
|key_word|
# section .bss
###### any variable set here is like ``int x;`` , set variable without pre data inside, so get data here before put data would be Cpp-UB
## define a variable

# section .text
###### assembly will run all thing here
###### we can just put code here, or put a entry label , the entry label reference to the code belong to entry label

# entry label
###### you can name a label as python variable, no int first , no space 
```
example_name:
    ;code here
```

## indentation and change row is useless in asm, so as c++

