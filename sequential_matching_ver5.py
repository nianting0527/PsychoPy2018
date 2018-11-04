# 2018/10/25 圖片呈現
# 2018/10/27 使用list迴圈
# 2018/10/31 phase設定、反應鍵、指導語
# 2018/11/3  random_list_ver1 finally is done!!!!!!!!!!!!!!!!! have tried at least 30+ methods.....(feel tired like a dog)
# 2018/11/4  subject infornmation gui, keyboard record



#import module
from psychopy import visual, core,event,gui
from sys import exit
import csv, random
import pandas as pd


#print subj info
info = {'name':'', 'age':'', 'num':'2', 'task':['1','2','3','4']}
infoDlg = gui.DlgFromDict(dictionary = info, title = u'基本信息', order = ['name','age','num','task'])
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
#phase=[practice,test1,test2]


#實驗一共會有三個回合：1. 練習  2.測驗一  3.測驗二
for phase in range(1,4):

 if phase == 1:
  trials=5
  testfiles= "test3.csv"
  text_1.text = 'Practice phase, press any key to continue...'
  text_1.draw()
  win.flip()
  event.waitKeys()
 elif phase ==2:
  trials=5
  testfiles= "test3.csv"
  text_1.text = 'Test-1 phase, press any key to continue...'
  text_1.draw()
  win.flip()
  event.waitKeys()
 elif phase ==3:
  trials=5
  testfiles= "test3.csv"
  text_1.text = 'Test-2 phase, press any key to continue...'
  text_1.draw()
  win.flip()
  event.waitKeys()
  

 #刺激呈現
 reader = csv.DictReader(open("test3.csv", "r"))  
 tt=list(reader)
 random.shuffle(tt)
 dataFile.write('filename, filename2, species, species2,pressedKeys,accuracy\n')
 for i in range(0,trials):
      #testparameter
      trials=i+1
      print('trial = %d'%trials)
      print('*******************')
      print('phase = %d'%phase)
      print('*******************')
      print(tt[i]['filename'])
      print('*******************')
      print(tt[i]['filename2'])
      print('*******************')
      print(tt[i]['species'])
      print('*******************')
      print(tt[i]['species2'])
      print('-----------------')
      
      #圖片一
      pic = visual.ImageStim(win, size=[0.5,0.5], image=tt[i]['filename'])
      #圖片二
      pic2 = visual.ImageStim(win, size=[0.5,0.5], image=tt[i]['filename2'])
      #刺激呈現(fixation)
      fixation = visual.TextStim(win, text = '+',height = 0.2,pos = (0.0,0.0),color = 'black',bold = True,italic = False)
      fixation.draw()
      win.flip()
      core.wait(0.5)
      #刺激呈現(bird1)
      pic.draw()
      win.flip()
      core.wait(0.5)
      #刺激呈現(mask)
      mask.draw()
      win.flip()
      core.wait(0.5)
      #刺激呈現(bird2)
      pic2.draw()
      win.flip()
      core.wait(0.5)
      #反應鍵
      response.draw()
      win.flip()
      keys=event.waitKeys(4.000, ["c","m"])
      accuracy=[0]
      for key in keys:        if (key == "c"):          accuracy=[1]
      print(accuracy)
      
       
     
      
      
      dataFile.write(tt[i]['filename']+', '+tt[i]['filename2']+', '+tt[i]['species']+', '+tt[i]['species2']+','+str(keys)+','+str(accuracy)+'\n')

text_1.text = 'This is the end of the experiment,thank you!'
text_1.draw()
win.flip()
event.waitKeys()
win.close()
core.quit()