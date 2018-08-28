import pygame
import time
from time import sleep  
import random
#import eztext
#import example
from Tkinter import *
import tkMessageBox as messagebox
import sys
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,30)
pygame.init()
#global player
#player=""

def tkfunc():
    top=Tk()
    top.attributes("-topmost",True)

    def func():
        global player
        player=ment.get()
        top.destroy()
        return

    ment=StringVar()
    top.geometry("250x250+200+200")
    top.title('Player Details')
    l1=Label(top,text='Player Name:').grid(row=0,column=0,sticky=W)
    but=Button(top,text='OK',command=func).grid(row=2,column=1)
    ent=Entry(top,textvariable=ment).grid(row=1,column=0)
    top.mainloop()

   
class MenuItem(pygame.font.Font):
    def __init__(self,text,font="images/digital.ttf",font_size=35,font_colour=(255,255,0),(pos_x,pos_y)=(0,0)):  
        pygame.font.Font.__init__(self,font,font_size)
        self.text = text
        self.font_size = font_size
        self.font_colour = font_colour
        self.label = self.render(self.text, 1, self.font_colour)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y

    def set_position(self,x,y):
        self.position=(x,y)
        self.pos_x=x
        self.pos_y=y

    def set_font_colour(self,rgb):
        self.font_colour=rgb
        self.label=self.render(self.text,1,self.font_colour)

    def is_mouse_selection(self,(posx,posy)):
        if(posx>=self.pos_x and posx<=self.pos_x+self.width)and(posy>=self.pos_y and posy<=self.pos_y+self.height): #check this for mouse highlighting
            return True
        return False

class Menu():
    def __init__(self,window,items,funcs,font="images/digital.ttf",font_size=35,font_colour=(255,255,255)):
        self.window=window
        self.funcs=funcs
        self.bg=pygame.image.load("images/menu.png")
        self.bg=pygame.transform.scale(self.bg,(800,700))
        self.window_width=self.window.get_rect().width
        self.window_height=self.window.get_rect().height
        self.clock=pygame.time.Clock()
        self.items=[]
        for item in items:
            if item=="Sound":
                menu_item=MenuItem(item,font,28,(120,134,107))
            else:
                menu_item=MenuItem(item,font,font_size,font_colour)
            if item=="Sound":
                pos_x=3
                pos_y=280
            elif item=="Start":                
                pos_x=22
                pos_y=454
            elif item=="Gameplay":
                pos_x=170
                pos_y=555
            elif item=="Player Records":
                pos_x=420
                pos_y=555
            else:
                pos_x=708
                pos_y=454
            menu_item.set_position(pos_x,pos_y)
            self.items.append(menu_item)
        self.mouse_is_visible=True
        self.cur_item=None
 
    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)
 
    def set_mouse_selection(self, item, mpos):
        if item.is_mouse_selection(mpos):
            if(item.text=="Sound"):return
            item.set_font_colour((0,255,0))
            item.set_italic(True)
        else:
            if(item.text=="Sound"):return
            item.set_font_colour((230,72,32))
            item.set_italic(False)

    def run(self):
        mainloop=True
        gamelabel=pygame.font.Font("images/digital.ttf",80)
        gamelabel.set_italic(True)
        g_label = gamelabel.render("GAMENAME", 1,(232,0,13))
        while mainloop:
            window.blit(gm.bg,(0,-100))
            self.clock.tick(50)
            mpos=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    mainloop=False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    for item in self.items:
                        if item.is_mouse_selection(mpos):
                            if item.text=="Sound":
                                if item.font_colour==(120,134,107):
                                    item.set_font_colour((230,72,32))
                                else:
                                    item.set_font_colour((120,134,107))
                            self.funcs[item.text]()
 
            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_is_visible = True
                self.cur_item = None
 
            self.set_mouse_visibility()
            #self.window.fill(self.bg)
            
            
            for item in self.items:
                if self.mouse_is_visible:
                    self.set_mouse_selection(item, mpos)
                self.window.blit(item.label, item.position)
            window.blit(g_label,(245,28))
            pygame.display.flip()
soundval=0
sound=0
playername=""

if __name__=="__main__":
    def Game():
        #get_name()
        tkfunc()
        #global player
        #player=""
        pygame.mixer.music.stop()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,30)
        global sound
        global soundval


        '''def mquit():
            top=Tk()
            top.geometry("0x0+0+0")
            mexit=messagebox.askokcancel(title="Quit",message="Are you Sure")
                
            if mexit>0:
                top.destroy()
                return False
            else:
                top.destroy()
                return True
            '''
        global player

        
        pygame.init()

        window=pygame.display.set_mode((800,600))
        pygame.display.set_caption("Window")


        clock=pygame.time.Clock()

        black=(0,0,0)
        white=(255,255,255)



        red=pygame.image.load("images/trafficred.png")
        yel=pygame.image.load("images/trafficyel.png")
        gre=pygame.image.load("images/trafficgre.png")
        #image=pygame.transform.scale(image,(80,80))
                 



        def traffic():
            count=0
            
            while(True):
                
                if count==0:
                    count=1
                    window.blit(red,(0,0))
                    sleep(1)
                elif count==1:
                    count=2
                    window.blit(yel,(0,0))
                    sleep(1)
                    
                elif count==2:
                    count=3
                    
                    window.blit(gre,(0,0))
                    sleep(1)
                    
                elif count==3:
                    sleep(1)
                    return False
                    
                pygame.display.flip()
                clock.tick(10)

        class car:
            def __init__(self,x,y):
                self.x=x
                self.y=y
                self.i=pygame.image.load("images/Toyota_TopVIew.png")
                self.i=pygame.transform.scale(self.i,(95,200))
                self.timetarget=10
                self.timenum=0
                self.lane=1
            def render(self,ln):
                if(self.lane==1 and ln==2):
                    window.blit(self.i,(self.x+95,self.y))
                    self.lane=2
                elif(self.lane==2 and ln==1):
                    self.lane=1
                    window.blit(self.i,(self.x,self.y))

                elif(self.lane==1):
                    
                    window.blit(self.i,(self.x,self.y))
                else:
                    window.blit(self.i,(self.x+95,self.y))
                    

        class obs:
            def __init__(self,num):
                
                self.x=300
                self.y=3
                self.y-=200
                self.p=0
                loc="images/"+str(num)+".png"
                self.i=pygame.image.load(loc)
                self.i=pygame.transform.scale(self.i,(95,190))

            def render(self):
                if self.p==0:
                    num=random.choice([1,2,3,4])
                    loc="images/"+str(num)+".png"
                    self.i=pygame.image.load(loc)
                    self.i=pygame.transform.scale(self.i,(95,190))
                    self.p=1
                    self.x=random.choice([300,395,300,395])
                
                    
                window.blit(self.i,(self.x,self.y))

            
            
                    

        c=car(300,400)
        o=obs(1)
        o3=obs(3)
        #global gap
        #gap=[800,300]
        def movement(speed):
            global valid1
            global valid2
            if(valid1==1):
                o.render()      #FIRST
            
                    
            o.y+=speed

            if(o.y>=800):       #650
                valid1=1
                o.y=3-200
                o.p=0
            
            if(o.y>300):        #230
                if(valid2==1):
                    o3.render()
                
                o3.y+=speed
            
            if(o.y<=300 and o3.y>3):  # 230
                if(valid2==1):
                    o3.render()
                o3.y+=speed
            if(o3.y>700):          #650
               o3.y=3-200
               valid2=1
               o3.p=0




        def levelspeed(level):

            global nos
            global gap
            global prev
            global speed
            global prevspeed
            if(level==1):
                nos=10   
                speed=5
                print "speed is ",speed
                print "nos is ",nos
            elif(level==2):
                #gap=[650,230]
                speed=10
                nos=25
                print "speed is ",speed
                print "nos is ",nos                
            elif(level==3):
                #gap=[800,300]
                speed=10
                nos=35
                print "speed is ",speed
                print "nos is ",nos
            elif(level==4):
                #gap=[650,230]
                speed=15
                nos=40
                print "speed is ",speed
                print "nos is ",nos
            elif(level==5):
                #gap=[800,300]
                speed=20         #20,50
                nos=50
                print "speed is ",speed
                print "nos is ",nos
            else:
                return  
            prev=nos
            prevspeed=speed

        gameLoop=True
        count=0
        global valid1
        global valid2
        valid1=1
        valid2=1

        pos=0
        global tim
        tim=0
        window.fill(white)
        #traffic()
        global level
        level=1

        
        bglx=0
        bgrx=500
        bgry=-600
        bgly=-600
        roadx=300
        roady=-400
        global speed
        speed=5
        global nos
        nos=10
        global prev
        prev=nos
        global prevspeed
        prevspeed=speed
        global lives
        lives=5
        score=0                   #highscore
        l1=pygame.image.load("images/l1.png")
        l1=pygame.transform.scale(l1,(148,47))
        l2=pygame.image.load("images/l2.png")
        l2=pygame.transform.scale(l2,(148,47))
        l3=pygame.image.load("images/l3.png")
        l3=pygame.transform.scale(l3,(148,47))
        l4=pygame.image.load("images/l4.png")
        l4=pygame.transform.scale(l4,(148,47))
        l5=pygame.image.load("images/l5.png")
        l5=pygame.transform.scale(l5,(200,185))

        nostime=0                 #nos + score
        bege='5'           #ncomment this s dddddddddddddd
        begin=time.clock()
        
        while(time.clock()-begin<=5):
            bgl=pygame.image.load("images/bgl9.png")
            bgl=pygame.transform.scale(bgl,(300,1200))
            bgr=pygame.image.load("images/bgr9.png")
            bgr=pygame.transform.scale(bgr,(300,1200))
            road=pygame.image.load("images/road.png")
            road=pygame.transform.scale(road,(200,2200))
            window.blit(bgl,(bglx,bgly))
            window.blit(bgr,(bgrx,bgry))
            window.blit(road,(roadx,roady))
            c.render(c.lane)
            myfont = pygame.font.SysFont("monospace", 500,bold=True)
            label = myfont.render(bege, 1, (255,255,255))
            bege=str((int(bege))-1)
            
            window.blit(label, (250, 150))
            pygame.time.wait(1000)
            pygame.display.flip()


        if(soundval==1):             #soundrelaed change
            pygame.mixer.music.load("images/carsound.wav")
            pygame.mixer.music.play(15)

        gametime=time.clock()
        while gameLoop:
            window.fill(white)
            bgl=pygame.image.load("images/bgl9.png")
            bgl=pygame.transform.scale(bgl,(300,1200))
            bgr=pygame.image.load("images/bgr9.png")
            bgr=pygame.transform.scale(bgr,(300,1200))
            road=pygame.image.load("images/road.png")
            road=pygame.transform.scale(road,(200,2200))
            roady+=20
            bgly+=20
            bgry+=20
            if roady>=0 : roady=-600
            if bgly>=0 : bgly=-600

            if bgry>=0 : bgry=-600
            window.blit(bgl,(bglx,bgly))
            window.blit(bgr,(bgrx,bgry))
            window.blit(road,(roadx,roady))
            if(level==1):
                window.blit(l1,(540,500))
            if(level==2):
                window.blit(l2,(540,500))
            if(level==3):
                window.blit(l3,(540,500))
            if(level==4):
                window.blit(l4,(540,500))
            if(level==5):
                window.blit(l5,(510,285))
            myfont = pygame.font.SysFont("images/digital.ttf", 26,bold=True)
            sc="SCORE : "+str(score)                                 #score 
            label = myfont.render(sc, 1, (159,4,16))
            window.blit(label, (510, 550))    
            if((time.clock()- gametime > (10)*level ) and level<6):
                level+=1
                
                levelspeed(level)
                
                
                gametime=time.clock()
                #print level
                print "nos=:",nos
                print "speed=:",speed
            if(level==6):level=5
            #movement(speed)
            
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    pygame.mixer.music.stop()
                    if soundval==1 :
                        soundval=0
                        sound_onoff()
                    if sound==1:
                        sound=0
                        sound_onoff
                    return
                if(event.type==pygame.KEYUP ):
                    speed=prevspeed
                    nos=prev
                    #score+=int(level*(time.clock()-nostime))*20
                    nostime=0
                    #print "nos back to ",nos  
                if(event.type==pygame.KEYDOWN ):
                     
                    if(event.key==pygame.K_f):
                        window=pygame.display.set_mode((800,600),pygame.FULLSCREEN)                

                    elif(event.key==pygame.K_p):
                        while(1):
                            
                            pygame.mixer.music.stop()
                            event=pygame.event.wait()
                            if event.type==pygame.KEYDOWN and event.key==pygame.K_p:
                                if(soundval==1):
                                    pygame.mixer.music.load("images/carsound.wav")
                                    pygame.mixer.music.play()
                                break
                            
                                
                    elif(event.key==pygame.K_ESCAPE):
                        window=pygame.display.set_mode((800,600))

                    elif(event.key==pygame.K_SPACE ):

                        nostime=time.clock()
                        nos+=25
                        speed+=10
                        #print "nos changed to ",nos

                    elif(event.key==pygame.K_RIGHT and c.lane!=2 ):
                        im=pygame.transform.rotate(c.i,300)
                        window.blit(im,(295,400))
                        #pygame.display.flip()
                        pos=1
                        
                        '''
                        if(sound==1):
                            pygame.mixer.stop()
                            pygame.mixer.Sound("racing.wav").play(-1)
                            #pygame.time.wait(1000)
                            skid=pygame.mixer.Sound("CarSkidding.wav")
                            skid.play(0,2000,0)
                        '''
                        tim=time.clock()
                    elif (event.key==pygame.K_LEFT and c.lane!=1):
                        im=pygame.transform.rotate(c.i,60)
                        window.blit(im,(295,400))
                        #pygame.display.flip()
                        '''
                        if (sound==1):
                            pygame.mixer.stop()
                            pygame.mixer.Sound("racing.wav").play(-1)
                            skid=pygame.mixer.Sound("CarSkidding.wav")
                            skid.play(0,2000,0)
                        '''
                        pos=2
                        tim=time.clock()
            else:
                if(pos==1 and time.clock()-tim > 0.2):
                    c.render(2)
                    #pygame.display.flip()
                    pos=0
                    tim=0
                elif(pos==2 and time.clock()-tim > 0.2):
                    c.render(1)
                    #pygame.display.flip()
                    pos=0
                    tim=0
                elif(pos==1):
                    
                    
                    im=pygame.transform.rotate(c.i,300)
                    window.blit(im,(295,400))
                    #pygame.display.flip()
                elif(pos==2):
                    
                    im=pygame.transform.rotate(c.i,60)
                    window.blit(im,(295,400))
                    #pygame.display.flip()
                else:
                    #if sound==1:
                    #    pygame.mixer.Sound("racing.wav").play(-1)
                    c.render(c.lane)
            
            if(c.lane==1):             
                if((o.x==300 and (o.y+190-c.y>0 and o.y<600) and valid1==1 ) or (o3.x==300 and (o3.y+190-c.y>0 and o3.y<600) and valid2==1)):
                    if (o.x==300 and (o.y+190-c.y>0 and o.y<600) and valid1==1 ):
                        valid1=0
                    else:
                        valid2=0
                    #pygame.mixer.stop()
                    #pygame.mixer.Sound("crash.wav").play(0,2000,0)
                    lives-=1    
                    tm=time.clock()
                    print c.lane
                    if(tim!=0):
                        while(time.clock()-tm < 3):

                            window.blit(road,(roadx,roady))
                            pygame.display.flip()
                            pygame.time.wait(500)
                            o.render()
                            o3.render()
                            im=pygame.transform.rotate(c.i,300)
                            window.blit(im,(295,400))
                            #c.render(c.lane)
                            pygame.display.flip()
                            pygame.time.wait(500)
                    while(time.clock()-tm < 3):
                        window.blit(road,(roadx,roady))
                        pygame.display.flip()
                        pygame.time.wait(500)
                        o.render()
                        o3.render()
                        c.render(c.lane)
                        pygame.display.flip()
                        pygame.time.wait(500)
                        
                
            elif(c.lane==2):
                if((o.x==395 and (o.y+190-c.y>0 and o.y<600) and valid1==1) or (o3.x==395 and (o3.y+190-c.y>0 and o3.y<600 ) and valid2==1)):
                    if(o.x==395 and (o.y+190-c.y>0 and o.y<600) and valid1==1):
                        valid1=0
                    else:
                        valid2=0
                    tm=time.clock()
                    #pygame.mixer.stop()
                    #pygame.mixer.Sound("crash.wav").play(0,2000,)
                    #pygame.time.wait(5000)
                    lives-=1
                    print c.lane
                    if(tim!=0):
                        while(time.clock()-tm < 3):

                            window.blit(road,(roadx,roady))
                            pygame.display.flip()
                            pygame.time.wait(500)
                            o.render()
                            o3.render()
                            im=pygame.transform.rotate(c.i,60)
                            window.blit(im,(295,400))
                            #c.render(c.lane)
                            pygame.display.flip()
                            pygame.time.wait(500)
                    
                        
                    while(time.clock()-tm < 3):
                        window.blit(road,(roadx,roady))
                        pygame.display.flip()
                        pygame.time.wait(500)
                        o.render()
                        o3.render()
                        c.render(c.lane)
                        pygame.display.flip()
                        pygame.time.wait(500)
                    
            if(lives==0):
                
                fo=open("highscore.txt","r+")
                line=fo.readline()
                if(line):
                    l=line.split(',')
                    if(int(l[1])<score):
                        print "NEW HIGH SCORE "                # DISPLAY ON SCREEN
                        fa=open("auxillary.txt","wb")
                        rec=player+','+str(score)+'\n'
                        fa.write(rec)
                        fa.write(line)
                        for ln in fo:
                            fa.write(ln)
                        fo.close()
                        os.remove('highscore.txt')
                        fa.close()
                        os.rename('auxillary.txt','highscore.txt')
                    else:
                        print "not high score"
                        fo.close()
                else:
                    fo.close()
                    fo=open('highscore.txt','wb')
                    rec=player+','+str(score)+'\n'
                    fo.write(rec)
                    fo.close()
                
                    
                            
                            
                cl=time.clock()
                while(time.clock()-cl < 5 ):
                    
                    window.fill(black)
                    myfont = pygame.font.SysFont("monospace", 100,bold=True)
                    label = myfont.render("GAME OVER !", 1, (255,255,255))
                    window.blit(label, (100, 200))
                    myfont2 = pygame.font.SysFont("monospace", 50,bold=True)
                    s="Score is : "+str(score)
                    label2 = myfont2.render(s, 1, (255,255,255))
                    window.blit(label2, (150, 300))
                    pygame.display.flip()        # if button pressed
                    '''pygame.time.wait(1000)
                    window.blit(bgl,(bglx,bgly))
                    window.blit(bgr,(bgrx,bgry))
                    window.blit(road,(roadx,roady))
                    c.render(c.lane)
                    pygame.display.flip()
                    pygame.time.wait(500)'''
                pygame.mixer.music.stop()
                if soundval==1 :
                    soundval=0
                    sound_onoff()
                if sound==1 :
                    sound=0
                return
                    
                    
                
                gameLoop=False                            #CHANGE THIS    
            #if tim==0:
            if(lives!=0):
                movement(speed)
            #else:
                #movement(1)
            #pygame.draw.line(window,black,(300,o.y+200),(200,o.y+200))
            #pygame.draw.line(window,black,(300,o.y),(200,o.y))
            #pygame.draw.line(window,black,(300,o3.y+200),(200,o3.y+200))
            #pygame.draw.line(window,black,(300,o3.y),(200,o3.y))
            pygame.draw.line(window,black,(300,400),(300,400+200))
            pygame.draw.line(window,black,(295,0),(295,600))
            pygame.draw.line(window,black,(305+2*95,0),(305+2*95,600))
            pygame.display.flip() # update
            score+=(level*2)
            
            clock.tick(nos)  # frames per second
            

        pygame.quit()


            
    
    def Gamequit():
        pygame.quit()
        sys.exit()



    def sound_onoff():
        global soundval
        global sound
        pygame.mixer.init()
        pygame.mixer.music.load("images/drive.wav")
        if soundval==1:
            pygame.mixer.music.pause()
            soundval=0
        elif soundval==0:
            soundval=1
            pygame.mixer.music.play()            
        if sound==1:
            sound=0
        elif sound==0:
            sound=1
        return
    def instructions_display():
        window = pygame.display.set_mode((800,600), 0, 32)
        bg=pygame.image.load("images/instr.png")
        bg=pygame.transform.scale(bg,(800,600))
        window.blit(bg,(0,0))
        pygame.display.flip()
        loop=True
        nlabel=pygame.font.Font("images/digital.ttf",28)
        n_label = nlabel.render("The Car will start to move after the 5 second countdown.", 1,(0,255,0))
        alabel=pygame.font.Font("images/digital.ttf",28)
        a_label = alabel.render("You will have 5 lives.", 1,(0,255,0))
        clabel=pygame.font.Font("images/digital.ttf",28)
        c_label =clabel.render(" If you turn into car,you end up with a crash.", 1,(0,255,0))
        slabel=pygame.font.Font("images/digital.ttf",28)
        s_label = slabel.render("Player Controls:<- Left,-> Right,Space=NOS,f=Full Screen,ESC=Normal", 1,(0,255,0))
        balabel=pygame.font.Font("images/digital.ttf",25)
        ba_label = balabel.render("Back to Menu", 1,(255,128,0))
        bpos_x=b_label.get_rect().width
        bpos_y=+b_label.get_rect().height
        blabel=pygame.font.Font("images/digital.ttf",25)
        b_label = blabel.render("Turn within time to avoid a crash.", 1,(0,255,0))
        '''bpos_x=b_label.get_rect().width
        bpos_y=+b_label.get_rect().height'''
        while loop:
            for event in pygame.event.get():
                print event
                if event.type==pygame.QUIT:
                    pygame.quit()
                    mainloop=False
            mpos=pygame.mouse.get_pos()
            (posx,posy)=mpos
            window.blit(bg,(0,0))
            window.blit(n_label,(15,71))
            window.blit(s_label,(15,145))
            window.blit(b_label,(15,219))
            window.blit(a_label,(15,280))
            window.blit(c_label,(15,340))
            window.blit(ba_label,(623,574))
            if event.type==pygame.MOUSEBUTTONDOWN:
                if(posx>=623 and posx<=623+bpos_x)and(posy>=574 and posy<=574+bpos_y):
                    return
            pygame.display.flip()

    def highscore_display():
        window = pygame.display.set_mode((800,600), 0, 32)
        bg=pygame.image.load("images/highscore.png")
        bg=pygame.transform.scale(bg,(800,600))
        window.blit(bg,(0,0))
        pygame.display.flip()
        loop=True
        i=0
        l=[]
        fo=open("highscore.txt","r+")
        for line in fo:
            i+=1
            l.append(line.split(','))
        if(i>=1):
            n0=pygame.font.Font("images/digital.ttf",28)
            #l[0][1]=str(int(l[0][1])/10)
            
            n_0=n0.render(l[0][0], 1,(95,158,160))
            s0=pygame.font.Font("images/digital.ttf",26)
            s_0=s0.render(l[0][1][:-1], 1,(95,158,160))
        if(i>=2):
            n1=pygame.font.Font("images/digital.ttf",28)
            n_1=n1.render(l[1][0], 1,(95,158,160))
            s1=pygame.font.Font("images/digital.ttf",26)
            s_1=s1.render(l[1][1][:-1], 1,(95,158,160))
        if(i>=3):
            n2=pygame.font.Font("images/digital.ttf",28)
            n_2=n2.render(l[2][0], 1,(95,158,160))
            s2=pygame.font.Font("images/digital.ttf",26)
            s_2=s2.render(l[2][1][:-1], 1,(95,158,160))
        if(i>=4):
            n3=pygame.font.Font("images/digital.ttf",28)
            n_3=n3.render(l[3][0], 1,(95,158,160))
            s3=pygame.font.Font("images/digital.ttf",26)
            s_3=n3.render(l[3][1][:-1], 1,(95,158,160))
        if(i>=5):
            n4=pygame.font.Font("images/digital.ttf",28)
            n_4=n4.render(l[4][0], 1,(95,158,160))
            s4=pygame.font.Font("images/digital.ttf",26)
            s_4=s4.render(l[4][1][:-1], 1,(95,158,160))
        if(i>=6):
            n5=pygame.font.Font("images/digital.ttf",28)
            n_5=n5.render(l[5][0], 1,(95,158,160))
            s5=pygame.font.Font("images/digital.ttf",26)
            s_5=s5.render(l[5][1][:-1], 1,(95,158,160))
        if(i==7):
            n6=pygame.font.Font("images/digital.ttf",28)
            n_6=n6.render(l[6][0], 1,(95,158,160))
            s6=pygame.font.Font("images/digital.ttf",26)
            s_6=s6.render(l[6][1][:-1], 1,(95,158,160))
        fo.close()
        nlabel=pygame.font.Font("images/digital.ttf",28)
        n_label = nlabel.render("Name", 1,(95,158,160))
        slabel=pygame.font.Font("images/digital.ttf",28)
        s_label = slabel.render("Score", 1,(95,158,160))
        blabel=pygame.font.Font("images/digital.ttf",25)
        b_label = blabel.render("Back to Menu", 1,(255,128,0))
        bpos_x=b_label.get_rect().width
        bpos_y=+b_label.get_rect().height
        while loop:
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    pygame.quit()
                    mainloop=False
            mpos=pygame.mouse.get_pos()
            (posx,posy)=mpos
            if(posx>=652 and posx<=652+bpos_x)and(posy>=574 and posy<=574+bpos_y):
                b_label=blabel.render("<<< Back to Menu",1,(255,8,0))
            else:
                b_label=blabel.render("<<< Back to Menu",1,(255,128,0))
            window.blit(bg,(0,0))
            window.blit(n_label,(544,11.9))
            window.blit(s_label,(724,13.5))
            window.blit(b_label,(623,574))
            if(i>=1):
                window.blit(n_0,(455,45))
                window.blit(s_0,(722,45))
            if(i>=2):
                window.blit(n_1,(455,73))
                window.blit(s_1,(722,73))
            if(i>=3):
                window.blit(n_2,(455,103))
                window.blit(s_2,(722,103))
            if(i>=4): 
                window.blit(n_3,(455,133))
                window.blit(s_3,(722,133))
            if(i>=5):
                window.blit(n_4,(455,163))
                window.blit(s_4,(722,163))
            if(i>=6):
                window.blit(n_5,(455,193))
                window.blit(s_5,(722,193))
            if(i>=7):
                window.blit(n_6,(455,223))
                window.blit(s_6,(722,223))
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if(posx>=623 and posx<=623+bpos_x)and(posy>=574 and posy<=574+bpos_y):
                    return
            pygame.display.flip()
    '''def get_name():
        pygame.init()
        global playername
        window=pygame.display.set_mode((800,600))
        bg=pygame.image.load("images/highscore.png")
        events=pygame.event.get()
        txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='Player Name: ')
        clock=pygame.time.Clock()
        while True:
            clock.tick(30)
            for event in events:
                if event.type==pygame.QUIT:
                    return
                window.blit(bg,(0,0))
                txtbx.update(events)
                txtbx.draw(window)
                pygame.display.flip()
    '''            


    window = pygame.display.set_mode((800,600), 0, 32)
     
    menu_items = ('Start', 'Quit')
    funcs = {'Start': Game,
             'Quit': Gamequit,
             'Sound': sound_onoff,
             'Player Records': highscore_display,
             'Gameplay':instructions_display}
 
    pygame.display.set_caption('Game Menu')
    gm = Menu(window, funcs.keys(), funcs)
    gm.run()
