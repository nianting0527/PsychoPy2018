from psychopy import visual, core,event
win = visual.Window(size = (1000,600), color = (1,1,1), fullscr = False )
text_1 = visual.TextStim(win, text = u'',
                               height = 0.1,
                               pos = (0.0,-0.1),
                               color = 'violet',
                               bold = True,
                               italic = False)
text_1.text = 'Welcome to our experiment。'

#时钟
timer = core.Clock()

text_1.draw()
win.flip()
core.wait(0)
timer.reset()           #重置时间0
k_1 = event.waitKeys()
timeUse = timer.getTime()       #获取时间
print (k_1, timeUse)

pic = visual.ImageStim(win, image = '027_2_1.jpg',size = 0.8)
pic2 = visual.ImageStim(win, image = '028_2_1.jpg',size = 0.8)
pics= ('027_2_1.jpg','027_1_1.jpg')
pics2= ('028_2_1.jpg','028_1_1.jpg')
trials =(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
#image = ('027_2_1.jpg')
for i in range(len(trials)):
    fixation = visual.TextStim(win, text = '+',
                               height = 0.2,
                               pos = (0.0,0.0),
                               color = 'black',
                               bold = True,
                               italic = False)
    fixation.draw()
    win.flip()
    core.wait(2)
    pic.image = pics[i]
    pic.draw()
    win.flip()
    core.wait(2)
    
    pic2.image = pics2[i]
    pic2.draw()
    win.flip()
    core.wait(2)


core.wait(1)
#pic2 = visual.ImageStim(win, image = 'picvoice7.jpg',size = 0.8)

k_2 = event.waitKeys(keyList = ['c','m'])

if k_2[0]=='c':
    text_1.text = u'左'
    text_1.draw()
    win.flip()
    core.wait(1)
else:
    text_1.text = u'右'
    text_1.draw()
    win.flip()
    core.wait(1)


win.close()
core.quit()