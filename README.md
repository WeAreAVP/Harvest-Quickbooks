# Harvest Quickbooks Transformer

The Harvest Quickbooks Transformer is a program that converts data exported from Harvest into a compatible format for Quickbooks. This script can manipulate .iif files in certain ways that will make it much more efficient to create invoices.


## Installation

Python installation on your local machine is required to run this script. To check if your system has Python, open the terminal window and enter the command below:

```bash
python3 --version
```


If your terminal returns a version of Python, then you can proceed to the next steps. If Python is not installed, then download it from the official website by clicking [download](https://www.python.org/downloads/mac-osx/).

After download, find the file in your Downloads folder and double click to begin the installation process.



## Directions

1) Download transformer script from Github to your local machine.






2) If not already, open your terminal window. Navigate to the directory that contains the tranformer script by using the cd command. For instance if the script is in the Downloads folder:

```bash
cd Downloads
```



3) Run script in the terminal using the below command:


```bash
python quickbooks.py
```


4) Locate the .iif file you want to modify. You will be prompted to enter the file path of the file. Drag the file into terminal to enter the file path.




5) Enter the desired file name of the output file without including the .iif extension or _qb addition.




6) Choose the following options. Possible combinations are (a, b, c), (a, b), (a, c), (b, c), (a), (b), and (c):

    a) Copy ITEM values to NOTE values.

    b) Consolidate data by Item and Day.
    
    c) Rename all Item values to a single value.
    
    
    
    
7) A new .iif file is created with the added modifications. If no option was selected, the output file will be the same as the input. The new file should be in the same directory as the original file.




8) To convert another file, enter "y". Otherwise, enter "n", to exit program.
