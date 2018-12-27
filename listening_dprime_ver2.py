from psychopy import visual, core,event,gui,sound
from sys import exit
import csv, random

#print subj info
info = {'name':'', 'age':'', 'num':''}
infoDlg = gui.DlgFromDict(dictionary = info, title = u'基本信息', order = ['name','age','num'])
if infoDlg.OK == False:
    core.quit()
    
    
#open new files to record
dataFile = open("%s.csv"%(info['num']+'_'+info['name']), 'a')
dataFile.write(info['name']+','+info['age']+','+info['num']+'\n')


win = visual.Window(size = (1000,600), color = (1,1,1), fullscr = False )
#實驗準備
text_1 = visual.TextStim(win, text = u'',
                               height = 0.1,
                               pos = (0.0,-0.1),
                               color = 'violet',
                               bold = True,
                               italic = False)
text_1.text = 'Welcome to our experiment。'
mask = visual.ImageStim(win, image = "mask.jpg",size = 0.8)
intro = visual.ImageStim(win, image = "intro.png",size = 1.3)
response = visual.ImageStim(win, image = "response.png",size = 1.2)
timer = core.Clock()
intro.draw()
win.flip()
core.wait(0)
timer.reset()           
k_1 = event.waitKeys()
timeUse = timer.getTime()       
print (k_1, timeUse)

for phase in range(1,4):

 if phase == 1:
  trials=10
  testfiles= "listening_1.csv"
  text_1.text = 'Practice phase, press any key to continue...'
  text_1.draw()
  win.flip()
  event.waitKeys()
 elif phase ==2:
  trials=70
  testfiles= "listening_2.csv"
  text_1.text = 'Test-1 phase, press any key to continue...'
  text_1.draw()
  win.flip()
  event.waitKeys()
 elif phase ==3:
  trials=70
  testfiles= "listening_3.csv"
  text_1.text = 'Test-2 phase, press any key to continue...'
  text_1.draw()
  win.flip()
  event.waitKeys()
  

 #刺激呈現
 reader = csv.DictReader(open(testfiles, "r"))  
 tt=list(reader)
 random.shuffle(tt)
 dataFile.write('filename, filename2, species, species2,pressedKeys,accuracy\n')
 for i in range(0,trials):
  fixation = visual.TextStim(win, text = '+',height = 0.2,pos = (0.0,0.0),color = 'black',bold = True,italic = False)
  fixation.draw()
  win.flip()
  core.wait(0.5)
  pic = visual.ImageStim(win, size=[1.2,1.2], image=tt[i]['filename'])
  music = tt[i]['filename2']
  sounds = sound.Sound(music, loops=10)
  sounds.play()
  pic.draw() 
  win.flip()
  
  keys=event.waitKeys(7.00,["c","m"])
  accuracy=[0]
  sounds.stop()
  if keys != None:
    sounds.stop()
    for key in keys: 
     if (key == "c") and (tt[i]['species'])==(tt[i]['species2']): 
      accuracy=[1]
     elif (key == "m") and (tt[i]['species'])!=(tt[i]['species2']): 
      accuracy=[1]
 
      print(accuracy)
      dataFile.write(tt[i]['filename']+', '+tt[i]['filename2']+', '+tt[i]['species']+', '+tt[i]['species2']+','+str(keys)+','+str(accuracy)+'\n')

  
  