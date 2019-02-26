import glob
from functools import reduce

#set ypurt mapping of which displays map to which output varibale names in your code
variable_names = {0:"LED0",1:"LED1",2:"LED2",3:"LED3",4:"LED4",5:"LED5"}

#set the directory of your project
path_name = "lab3/bcdclock/"



def get_loc(segnum, varname, invert = True):
    """
    Assigns a given vhdl logic vector (6 downto 0) to the appropriate pins of the seven segment display
    labled 5 downto 0 (from left to right on the DE0CV) 
    
    invert will assign the most significant std logic element to the least significant seven segment display input 
    this is just to match the format of JESUS' bcd -> 7 function so its default set to true
    Note: 
    """
    segs = [
                ["PIN_U21","PIN_V21","PIN_W22","PIN_W21","PIN_Y22","PIN_Y21","PIN_AA22"],
                ["PIN_AA20","PIN_AB20","PIN_AA19","PIN_AA18","PIN_AB18","PIN_AA17","PIN_U22"],
                ["PIN_Y19","PIN_AB17","PIN_AA10","PIN_Y14","PIN_V14","PIN_AB22","PIN_AB21"],
                ["PIN_Y16","PIN_W16","PIN_Y17","PIN_V16","PIN_U17","PIN_V18","PIN_V19"],
                ["PIN_U20","PIN_Y20","PIN_V20","PIN_U16","PIN_U15","PIN_Y15","PIN_P9"],
                ["PIN_N9","PIN_M8","PIN_T14","PIN_P14","PIN_C1","PIN_C2","PIN_W19"]
           ]
    return reduce(lambda x,y: x+y, ["set_location_assignment {} -to {}[{}]\n".format(segs[segnum][i],varname,int(6*invert-2*(invert-1/2)*i)) for i in range(7)])

with open(glob.glob(path_name+"*.qsf")[0], "a") as f: 
        f.write("\n")
        for i in variable_names: f.write(get_loc(i,variable_names[i]))
