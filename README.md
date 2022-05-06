# SEIR Model Stimulations
## Inroduction
This program create a main window which the user can simulate the pendemic based on SEIR model.  
on the window, the user can change the parameter: days, Tinc, Tinf, R0. A label will show the parameter 
information to tell the user what are the parameter now.  
then the user can choose what garph to show:   
- static line graph  
- animated line graph  
- animated pie chart  
- different model pictures  
## How to use  
This code should be run in Spyder. You should install matplotlib, tkiner, numpy.  
The main program file for this stimulation is __SEIR_model_simulation.py__. Open it in Spyder and run it, the main window will appear like the picture shown below:  
![image](https://user-images.githubusercontent.com/98830245/167046659-88e1c428-7c59-40e8-a0fe-d280709733e0.png)  
The left part inside the main window shows all the parameters needed for stimulation. And the default values are shown on the bottom left corner of the main window. You can change the variable values by typing numbers in the inputboxes and all the values are synchronised on the bottom left corner immediately.    
The right part inside the main window contains four different buttons. The top 3 buttons show the static line graph, annimated line graph and animated pie chart respectively, all of them can be changed by adjusting parameter values. The bottom button shows the data difference between different models (SI, SIR and SEIR), it is a static picture and will not be changed by adjusting parameter value.
 
    
