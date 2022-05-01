## SPEAKER POINT AVERAGING

This is a tool intended to automatically calculate the average speaker points a judge gives at national circuit POLICY tournaments. 

![image](https://user-images.githubusercontent.com/62866081/166127141-74ba8fec-68fd-426f-9d75-318754a49452.png)

The script is relatively simple:
* **INPUT #1** - Requires the TABROOM link to a tournament for ROUND ONE
* **INPUT #2** - Takes the total number of preliminary rounds for the tournament
* **INPUT #3** - Speaker point distinction - [Y/N]

Tournaments generally offer two ways of showing data in the results table. 

# FIRST DATA FRAME

Auto-generated speaker points shown in a table for each debater.

![image](https://user-images.githubusercontent.com/62866081/166127184-e1795aab-4183-4447-9588-04e5ec733dbe.png)

# SECOND DATA FRAME

The next way is a slight modification - where it shows the numerical position for each debater 1-4 

![image](https://user-images.githubusercontent.com/62866081/166127195-2ae41576-c7e9-4000-abf4-089b7f5e3908.png)

# INPUT DIFFERENTIATION

The final piece of input will ask the user to input whether the tournament uses the first or second method of speaker point display.

Put 'y' (case sensitive) if the data frame matches the first image.
Put 'n' (case sensitive) if the data frame matches the second image. 

# REQUIREMENTS

To run this program locally on your computer, you will need a few programs installed on your computer
* Python 3.8+
* Microsoft Excel v10+
* Dependencies: BeautifulSoup, lxml, openpyxl

For each library, you must open the terminal and use the ```pip install``` command (this could change depending on your system) in order to successfuly import each dependency. 

## REQUIRED MODIFICATION TO CODE!

If you wish to run this code locally, you will have to edit the code. Go to main.py and change the following code - 

```wb = load_workbook('INSERT PATH')``` 
```wb.save('INSERT PATH')```

You will have to edit the path file to the destination you want to save the spreadsheet

![image](https://user-images.githubusercontent.com/62866081/166127358-d5d4cc49-f644-495f-8d34-8208fb5a2101.png)

# FINAL OUTPUT

If all input is entered correctly, the program will automatically generate a spreadsheet that contains the average number of speaker points organized by judge per tournament. Modifications to automatically average the final table **HAVE NOT** been added as of now - can be done fairly easily in excel however. 

We hope to use this as a general heuristic to see the types of speaker points that judges give on the national circuit. 

Cheers!


