#luiscarloscollazo
#dec1

#our first graphical user interface (GUI) app

#import TKinter libraries
from tkinter import *

#create a window using the Tk class
window = Tk()


#give a title to our window
window.title('My First GUI Python App')

#set size of window
window.geometry("500x500")


#first label

#change the label 
mylabel = Label(window,
                 text = "Hello CSI Users!",
                 font = ("Didot", 20),
                 justify = 'left'
)

#second label 

mylabel2 = Label(window,
                 text = "My Personal Program - GUI App",
                 font = ("Didot", 25),
                 foreground = "white",
                 background = "#0099ff",
                 justify = 'left'
)

#text 
text1 = '''
========================================================
== NAME: Luis Carlos Collazo Carrión                  ==
== GRADE: 8th Grade                                   ==
== HOBBIES: Basketball, Volleyball, Running, and Math ==
========================================================
'''
#third label

mylabel3  = Label(window,
                  text = text1,
                  font = "Courier 8",
                  justify = 'left',
                  foreground = 'black'
)


#drawing

text2 ='''
             /\            
            /  \           
     _ _ _ /    \ _ _ _    
      \              /     
      /              \     
     /_ _ _      _ _ _\    
           \    /          
            \  /           
             \/            
'''
#fourth label

mylabel4 = Label(window,
                 text = text2
)


mylabel.pack()
mylabel2.pack()
mylabel3.pack()
mylabel4.pack()









#run our GUI app
window.mainloop()
