# Seven Segment Display Pin Mapper for Quartus II

To use start by opening the script and changing the `variable_names` map to contain the names of the varibles in your Quartus 
program that you want to map to each sgement.
```
#i.e
variable_names = {0:"LED0",1:"LED1",2:"LED2",3:"LED3",4:"LED4",5:"LED5"}
```
Finally, set the path name for your project directory.
```
path_name = "~/QuartusProjects/lab2/"
```
The program should find the `.qsf` file in your directory and take care if the rest.
