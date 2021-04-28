import os, pyautogui as pag

#prompt to get filepath 
filepath= pag.prompt(text= "Please input path of folder you would like to have images stored in.", title="Path for images",default= os.getcwd())
#move into filepath and create imgs folder
os.chdir(filepath)
os.mkdir("imgs")
os.chdir("imgs")

#instructions for users 
pag.alert(text= "Please make sure the application that you would like to screenshot and catalogue is set up correctly on the screen.\nYou will be prompted to get the coordinates for the steps in future message boxes.")

#get flippage coordinates
if pag.confirm(text="Please put the mouse where you would click to flip to the next page and click space bar to select OK", title="Flip Page Button Coordinates")== "OK":
    flip_page= pag.position()
    
#get number of pages user wants to save
numPage= pag.prompt(text= "How many pages would you like to screenshot and save?\n *Please hit enter to submit*")
numPage= int(numPage)

#go through and screengrab and save, first screen grab is delayed for one second so the numPage prompt isn't still on screen
i=0
for x in range(0,numPage):
   if i==0:
       pag.moveTo(flip_page, duration=1)
       pag.screenshot("img"+str(i)+".jpg")
       pag.click()
       i+=1
   else:
       pag.moveTo(flip_page)
       pag.screenshot("img"+str(i)+".jpg")
       pag.click()
       i+=1
#go back to OG filepath just in case user wants to  delete saves/imgs folder    
os.chdir(filepath)

pag.alert(text= "The process is complete. Thank you for using screengrab_and_save! Have a great day!")