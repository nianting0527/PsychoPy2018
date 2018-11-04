# 2018/10/25 圖片呈現
# 2018/10/27 使用list迴圈
# 2018/10/31 phase設定、反應鍵、指導語
# 2018/11/3  random_list_ver1 finally is done!!!!!!!!!!!!!!!!! have tried at least 30+ methods.....(feel tired like a dog)

from psychopy import visual, core,event
from sys import exit
import csv, random 
import pandas as pd
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
for phase in range(1,3):

 if phase == 1:
  testfiles= "test3.csv"
  text_1.text = 'Practice phase, press any key to continue...'
  text_1.draw()
  win.flip()
  event.waitKeys()
 elif phase ==2:
  testfiles= "test3.csv"
  text_1.text = 'Test-1 phase, press any key to continue...'
  text_1.draw()
  win.flip()
  event.waitKeys()
 elif phase ==3:
  testfiles= "test3.csv"
  text_1.text = 'Test-2 phase, press any key to continue...'
  text_1.draw()
  win.flip()
  event.waitKeys()
  

 #刺激呈現
 
 for i in range(0,5): 
      reader = pd.read_csv("test3.csv")
      tt= reader.sample(frac=1)
      print(tt['filename'][0])
      print(tt['filename'][1])
      print(tt['filename'][2])
      print(tt['filename'][3])
      print(tt['filename'][4])
      
      print(len(tt['filename']))
      #圖片一
      pic = visual.ImageStim(win, size=[0.5,0.5], image=tt['filename'][i])
      #圖片二
      pic2 = visual.ImageStim(win, size=[0.5,0.5], image=tt['filename2'][i])
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
      event.waitKeys(4.000, ["c","m"])
       
 
win.close()
core.quit()