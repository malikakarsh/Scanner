import os
import sys
import imutils
import shutil
import numpy as np
import cv2
import PIL
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk


if not os.path.isdir('SAVED'):
    os.mkdir('SAVED')
else:
    shutil.rmtree('SAVED')
    os.mkdir('SAVED')
    


    
root = Tk()


img_frame = LabelFrame(root, text="Developed by Akarsh", width = 700, height = 900)
img_frame.grid(row=0,column=0,rowspan=2,padx=2,pady=2)


label_frame_top = Frame(root, height = 350)
label_frame_top.grid(row=0,column=1,padx=2,pady=2)

label_frame_bottom = Frame(root, height = 350)
label_frame_bottom.grid(row=1,column=1,padx=2,pady=2)

img_label = Label(img_frame)
img_label.grid(row=0,column=0)





shift = 0
scan_shift = 0
file = 0
rotation = 0
img = 0
width=0
height =0
TL,TR,BR,BL = [0,0],[0,0],[0,0],[0,0]
TL_w,TR_w,BR_w,BL_w = 0,0,0,0
TL_h,TR_h,BR_h,BL_h = 0,0,0,0
img_save = 0
i = 0
val = 0
convert = 0
text = 0


TL_hscale, TL_wscale, TR_hscale, TR_wscale, BR_hscale,BR_wscale,BL_hscale,BL_wscale = 0,0,0,0,0,0,0,0

def reset():
    global TL_hscale, TL_wscale, TR_hscale, TR_wscale, BR_hscale,BR_wscale,BL_hscale,BL_wscale,TL_w,TR_w,BR_w,BL_w,TL_h,TR_h,BR_h,BL_h
    
    TL_hscale, TL_wscale, TR_hscale, TR_wscale, BR_hscale,BR_wscale,BL_hscale,BL_wscale = 0,0,0,0,0,0,0,0
    TL_w,TR_w,BR_w,BL_w = 0,0,0,0
    TL_h,TR_h,BR_h,BL_h = 0,0,0,0
    buttons()
    
    

def update(w1=0,h1=0,w2=0,h2=0,w3=0,h3=0,w4=0,h4=0):
    global TL_w,TR_w,BR_w,BL_w,TL_h,TR_h,BR_h,BL_h, TL_hscale, TL_wscale, TR_hscale, TR_wscale, BR_hscale,BR_wscale,BL_hscale,BL_wscale
    TL_h = TL_hscale.get()
    TL_w = TL_wscale.get()
    TR_h = TR_hscale.get()
    TR_w = TR_wscale.get()
    BL_h = BL_hscale.get()
    BL_w = BL_wscale.get()
    BR_h = BR_hscale.get()
    BR_w = BR_wscale.get()
    buttons()
    


def rot():
    global rotation
    if rotation == 360:
        rotation = 0
    else:
        rotation += 90

def open_file():
    global file, scan_shift,shift
    root.filename = filedialog.askopenfilename(initialdir="/", title= "Select an Image", filetypes=((".png extension","*.png"),(".jpg extension","*.jpg"),(".jpeg extension","*.JPEG")))
    
    file = root.filename
    if file:
        scan_shift = 1
        shift = 1
        scanner()
        buttons()
    
def discard():
    global shift, scan_shift, rotation, text
    
    shift = 0
    scan_shift = 0
    rotation = 0
    text = 0
    buttons()
    #scanner()

def save():
    global img_save, shift
    img_save = 1
    shift = 0
    buttons()
    
def view():
    global i, shift, scan_shift
    if i > 0:
        shift = 2
        scan_shift = 2
    buttons()
    scanner()
        
def add():
    global val
    
    if val >= 0 and val < (len(os.listdir('SAVED')) - 1):
        val += 1
    
    elif val == (len(os.listdir('SAVED')) - 1):
        val = 0
    
    buttons()
        
def sub():
    global val
    
    if val > 0 and val <= (len(os.listdir('SAVED')) - 1):
        val -= 1
    
    elif val == 0:
        val = (len(os.listdir('SAVED')) - 1)

    buttons()
        
def save_as():
    global convert
    convert = 1

def extract():
    global text
    text = 1
    
    
    
    
def scanner():
    global scan_shift, file, rotation, img, width, height,TL,TR,BR,BL,TL_w,TR_w,BR_w,BL_w,TL_h,TR_h,BR_h,BL_h, img_save, i, val, convert,text
   
    if os.path.isfile('SAVED/.DS_Store'):
        os.remove('SAVED/.DS_Store')
    if os.path.isfile('SAVED/.DS_Store'):
        os.remove('SAVED/.DS_Store')
    if scan_shift == 0:
        try:
        
            img = np.ones([900,650,3],dtype=np.uint8)
            img[:,:] = [160,255,13]
            cv2.putText(img,"1) Select an image to scan.",(10,40),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img,"2) If auto edge detection fails,",(10,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img,"   manually select the edges.",(10,120),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img,"3) Save image after edge detection.",(10,160),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img,"4) Follow along for more images.",(10,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img,"5) Click on view once done.",(10,240),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img,"6) Click EXTRACT to extract text.",(10,280),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img,"7) Extracted text displays in terminal",(10,320),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img,"8) Click CONVERT to convert to pdf.",(10,360),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img,"9) The pdf will be saved as scanned.pdf,",(10,400),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img,"   in the Scanner directory.",(10,440),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            img = PIL.Image.fromarray(img)
            if img.size[0] > img.size[1]:
                width = 960
                wpercent = width/float(img.size[0])
                height = int((float(img.size[1]) * float(wpercent)))
            else:
                height= 700
                hpercent = height/float(img.size[1])
                width = int((float(img.size[0]) * float(hpercent)))

            img_tk = ImageTk.PhotoImage(img)
            img_label.imgtk = img_tk
            img_label.configure(image=img_tk)
            #img_label.after(10,scanner)

        except:
            
            print("Error while opening image")
            scanner()

    
    elif scan_shift == 1:
       
        img = PIL.Image.open(file)
        if img.size[0] > img.size[1]:
            width = 960
            wpercent = width/float(img.size[0])
            height = int((float(img.size[1]) * float(wpercent)))
        else:
            height= 700
            hpercent = height/float(img.size[1])
            width = int((float(img.size[0]) * float(hpercent)))
                
        img = img.resize((width,height), PIL.Image.ANTIALIAS)
        orig = img.copy()
        orig = cv2.cvtColor(np.float32(orig), cv2.COLOR_RGB2BGR)
        img = np.asarray(img)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)



        imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        imgBlurred = cv2.GaussianBlur(imgGray, (5,5),0)
        imgCanny = cv2.Canny(imgBlurred, 30,50)
        #cv2.imwrite("canny.png",imgCanny)

        contours,hierarchy = cv2.findContours(imgCanny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        contours =sorted(contours,key=cv2.contourArea,reverse=True)

        for c in contours:
            p = cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,0.02*p,True)

            if len(approx)==4:
                target = approx
                break

        def mapp(h):
            h = h.reshape((4,2))
            hnew = np.zeros((4,2), dtype = np.float32)

            add = h.sum(1)
            hnew[0] = h[np.argmin(add)]
            hnew[2] = h[np.argmax(add)]

            diff = np.diff(h,axis =1)
            hnew[1] = h[np.argmin(diff)]
            hnew[3] = h[np.argmax(diff)]

            return hnew

        approx = mapp(target)
        if abs(approx[0][1] - approx[2][1]) < (height*(1/4)):
            approx = np.array([[40+TL_w,40+TL_h],[width-20+TR_w,40+TR_h],[width-20+BR_w,height-20+BR_h],[40+BL_w,height-20+BL_h]],dtype=np.float32)

        else:
            approx = np.array([[approx[0][0]+TL_w,approx[0][1]+TL_h],[approx[1][0]+TR_w,approx[1][1]+TR_h],[approx[2][0]+BR_w,approx[2][1]+BR_h],[approx[3][0]+BL_w,approx[3][1]+BL_h]],dtype=np.float32)





        pts = np.float32([[0,0],[width,0],[width,height],[0,height]])

        TL = [approx[0][0]+TL_w,approx[0][1]+TL_h]
        TR = [approx[1][0]+TR_w,approx[1][1]+TR_h]
        BR = [approx[2][0]+BR_w,approx[2][1]+BR_h]
        BL = [approx[3][0]+BL_w,approx[3][1]+BL_h]

        points = np.array([TL,BL,BR,TR],np.int32)
        points = points.reshape((-1,1,2))
        cv2.polylines(img,[points],True,(13,255,160),2)
        cv2.circle(img,(int(approx[0][0]+TL_w),int(approx[0][1]+TL_h)),10,(13,255,160),-1)
        cv2.circle(img,(int(approx[1][0]+TR_w),int(approx[1][1]+TR_h)),10,(13,255,160),-1)
        cv2.circle(img,(int(approx[2][0]+BR_w),int(approx[2][1]+BR_h)),10,(13,255,160),-1)
        cv2.circle(img,(int(approx[3][0]+BL_w),int(approx[3][1]+BL_h)),10,(13,255,160),-1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


        if img_save == 1:

            op = cv2.getPerspectiveTransform(approx,pts)
            dst = cv2.warpPerspective(np.float32(orig),op,(width,height))
            dst = imutils.rotate_bound(dst, rotation)
            i += 1
            #dst = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY).astype('uint8')
            #dst = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) 
            cv2.imwrite(f"SAVED/{i}.png",dst)
            img_save = 0
            scan_shift = 0

        img = imutils.rotate_bound(img, rotation)
        img_tk = ImageTk.PhotoImage(PIL.Image.fromarray(img))
        img_label.imgtk = img_tk
        img_label.configure(image=img_tk)
        img_label.after(10,scanner)
        '''
        except:
            print("Error while opening")
            scanner()
        '''
        
    
    elif scan_shift == 2:
        try:
            
            img_list = []
            save_list = []
            for image in os.listdir('SAVED'):
                img_list.append([image,PIL.Image.open(f"SAVED/{image}")])
                
            img_list.sort()

            if convert == 1 and len(img_list) !=0:
                im1 = img_list[0][1]

                if len(img_list) >= 2:
                    for a in range(1,len(img_list)):
                        save_list.append(img_list[a][1].convert('RGB'))

                    im1 = img_list[0][1].convert('RGB')
                    im1.save('scanned.pdf',save_all = True, append_images = save_list)

                    shutil.rmtree('SAVED')
                    os.mkdir('SAVED')
                    i = 0
                    val = 0
                    convert = 0
                    rotation = 0
                    text = 0
                    discard()

                else:
                    im1 = img_list[0][1]
                    im1 = img_list[0][1].convert('RGB')
                    im1.save('scanned.pdf')
                    i = 0
                    val = 0
                    convert = 0
                    rotation = 0
                    text = 0
                    discard()
                    
            if text == 1:
                try:
                    os.system(f"tesseract SAVED/{img_list[val][0]} out")
                    f = open('out.txt','r')
                    print("\nEXTRACTED TEXT:\n")
                    print(f.read())
                    text = 0
                except:
                    f = open('out.txt',"r")
                    print("\nEXTRACTED TEXT:\n")
                    print(f.read())
                    text = 0
                    
                
                
                
                    
            img = np.asarray(img_list[val][1])
            img = PIL.Image.fromarray(img)

            img_tk = ImageTk.PhotoImage(img)
            img_label.imgtk = img_tk
            img_label.configure(image = img_tk)
            img_label.after(10,scanner)
    
        except:
            print("Error while loading")
            scanner()
                
        
        
        

def buttons():
    global shift,width,height,TL,TR,BL,BR,TL_w,TR_w,BR_w,BL_w,TL_h,TR_h,BR_h,BL_h ,TL_hscale, TL_wscale, TR_hscale, TR_wscale, BR_hscale,BR_wscale,BL_hscale,BL_wscale

    
    if shift == 0:
        #label_frame_top
        open_button = Button(label_frame_top, text="OPEN",command=open_file, height = 4, width = 20)
        open_button.grid(row=0,column=0,padx=5,pady=2)
        save_button = Button(label_frame_top, text= "SAVE", height = 4, width = 20,state = DISABLED)
        save_button.grid(row=1,column=0,padx=5,pady=2)
        discard_button = Button(label_frame_top, text= "DISCARD", height = 4, width = 20,state = DISABLED)
        discard_button.grid(row=2,column=0,padx=5,pady=2)
        rotate_button = Button(label_frame_top, text = "ROTATE", height = 4, width = 20, command = rot,state = DISABLED)
        rotate_button.grid(row=3,column=0,padx=5,pady=2)
        view_button = Button(label_frame_top, text = "VIEW", height = 4, width =20, command = view)
        view_button.grid(row=4,column=0,padx=5,pady=2)
        #save_as_button = Button(label_frame_top, text = "CONVERT", height =4, width = 20, command = save_as, state = DISABLED)
        #save_as_button.grid(row=5,column=0,padx=5,pady=2)
        
        TL_hscale1 = Scale(label_frame_bottom,from_ = int((0 - TL[1])/2), to = int(((BL[1]-TL[1]) - 20)/3), orient = HORIZONTAL, command =update, state = DISABLED)
        TL_hscale1.set(0)
            
        TL_hlabel1 = Label(label_frame_bottom, text = "Top Left Height")
            
        TL_hscale1.grid(row=0,column=0)
        TL_hlabel1.grid(row=1,column=0)
        
        TL_wscale1 = Scale(label_frame_bottom,from_ = int((0 - TL[0])/2), to = int(((TR[0]-TL[0]) - 20)/3), orient = HORIZONTAL, command =update, state = DISABLED)
        TL_wlabel1 = Label(label_frame_bottom, text = "Top Left Width")
        TL_wscale1.set(0)
            
        TL_wscale1.grid(row=0,column=1)
        TL_wlabel1.grid(row=1,column=1)
        
        TR_hscale1 = Scale(label_frame_bottom,from_ = int((0 - TR[1])/2), to = int(((BR[1]-TR[1]) - 20)/3), orient = HORIZONTAL, command =update, state = DISABLED)
        TR_hlabel1 = Label(label_frame_bottom, text = "Top Right Height")
        TR_hscale1.set(0)
            
        TR_hscale1.grid(row=2,column=0)
        TR_hlabel1.grid(row=3,column=0)
        
        TR_wscale1 = Scale(label_frame_bottom,from_ = int((0 - TR[0])/3), to = int(((width-TR[0]))/2), orient = HORIZONTAL, command =update, state = DISABLED)
        TR_wlabel1 = Label(label_frame_bottom, text = "Top Right Width")
        TR_wscale1.set(0)
            
        TR_wscale1.grid(row=2,column=1)
        TR_wlabel1.grid(row=3,column=1)
        
        BL_hscale1 = Scale(label_frame_bottom,from_ = int((0-BL[1])/3), to = int(((height-BL[1]))/3), orient = HORIZONTAL, command =update, state = DISABLED)
        BL_hlabel1 = Label(label_frame_bottom, text = "Bottom Left Height")
        BL_hscale1.set(0)
            
        BL_hscale1.grid(row=4,column=0)
        BL_hlabel1.grid(row=5,column=0)
        
        BL_wscale1 = Scale(label_frame_bottom,from_ = int((0-BL[0])/2), to = int(((BR[0]-BL[0]) - 20)/3), orient = HORIZONTAL, command =update, state = DISABLED)
        BL_wlabel1 = Label(label_frame_bottom, text = "Bottom Left Width")
        BL_wscale1.set(0)
            
        BL_wscale1.grid(row=4,column=1)
        BL_wlabel1.grid(row=5,column=1)
        
        BR_hscale1 = Scale(label_frame_bottom,from_ = int((0-BR[1])/3), to = int(((height-BR[1]))/3), orient = HORIZONTAL, command =update, state = DISABLED)
        BR_hlabel1 = Label(label_frame_bottom, text = "Bottom Right Height")
        BR_hscale1.set(0)
            
        BR_hscale1.grid(row=6,column=0)
        BR_hlabel1.grid(row=7,column=0)
        
        BR_wscale1 = Scale(label_frame_bottom,from_ = int((0-BR[0])/3), to = int(((width-BR[0]))/2), orient = HORIZONTAL, command =update, state= DISABLED)
        BR_wlabel1 = Label(label_frame_bottom, text = "Bottom Right Width")
        BR_wscale1.set(0)
            
        BR_wscale1.grid(row=6,column=1)
        BR_wlabel1.grid(row=7,column=1)
        
        reset_button = Button(label_frame_bottom, text="RESET", width=20, height =4, command = reset, state = DISABLED)
        reset_button.grid(row=16,column=0,columnspan=2,padx=5,pady=2)

    elif shift == 1:
        open_button = Button(label_frame_top, text="OPEN",command=open_file, height = 4, width = 20,state = DISABLED)
        open_button.grid(row=0,column=0,padx=5,pady=2)
        save_button = Button(label_frame_top, text= "SAVE", height = 4, width = 20, command = save)
        save_button.grid(row=1,column=0,padx=5,pady=2)
        discard_button = Button(label_frame_top, text= "DISCARD", height = 4, width = 20,command = discard)
        discard_button.grid(row=2,column=0,padx=5,pady=2)
        rotate_button = Button(label_frame_top, text = "ROTATE", height = 4, width = 20, command = rot)
        rotate_button.grid(row=3,column=0,padx=5,pady=2)
        view_button = Button(label_frame_top, text = "VIEW", height = 4, width =20, command = view)
        view_button.grid(row=4,column=0,padx=5,pady=2)
        #save_as_button = Button(label_frame_top, text = "CONVERT", height =4, width = 20, command = save_as, state = DISABLED)
        #save_as_button.grid(row=5,column=0,padx=5,pady=2)
        
        
        if TL_hscale == 0:
            TL_hscale = Scale(label_frame_bottom,from_ = int((0 - TL[1])/2), to = int(((BL[1]-TL[1]) - 20)/3), orient = HORIZONTAL, command =update)
            TL_hscale.set(0)
            
            TL_hlabel = Label(label_frame_bottom, text = "Top Left Height")
            
            TL_hscale.grid(row=0,column=0)
            TL_hlabel.grid(row=1,column=0)
        if TL_wscale == 0:
            TL_wscale = Scale(label_frame_bottom,from_ = int((0 - TL[0])/2), to = int(((TR[0]-TL[0]) - 20)/3), orient = HORIZONTAL, command =update)
            TL_wlabel = Label(label_frame_bottom, text = "Top Left Width")
            TL_wscale.set(0)
            
            TL_wscale.grid(row=0,column=1)
            TL_wlabel.grid(row=1,column=1)
        
        if TR_hscale == 0:
            TR_hscale = Scale(label_frame_bottom,from_ = int((0 - TR[1])/2), to = int(((BR[1]-TR[1]) - 20)/3), orient = HORIZONTAL, command =update)
            TR_hlabel = Label(label_frame_bottom, text = "Top Right Height")
            TR_hscale.set(0)
            
            TR_hscale.grid(row=2,column=0)
            TR_hlabel.grid(row=3,column=0)
        
        if TR_wscale == 0:
            TR_wscale = Scale(label_frame_bottom,from_ = int((0 - TR[0])/3), to = int(((width-TR[0]))/2), orient = HORIZONTAL, command =update)
            TR_wlabel = Label(label_frame_bottom, text = "Top Right Width")
            TR_wscale.set(0)
            
            TR_wscale.grid(row=2,column=1)
            TR_wlabel.grid(row=3,column=1)
        
        if BL_hscale == 0:
            BL_hscale = Scale(label_frame_bottom,from_ = int((0-BL[1])/3), to = int(((height-BL[1]))/3), orient = HORIZONTAL, command =update)
            BL_hlabel = Label(label_frame_bottom, text = "Bottom Left Height")
            BL_hscale.set(0)
            
            BL_hscale.grid(row=4,column=0)
            BL_hlabel.grid(row=5,column=0)
            
        if BL_wscale == 0:
            BL_wscale = Scale(label_frame_bottom,from_ = int((0-BL[0])/2), to = int(((BR[0]-BL[0]) - 20)/3), orient = HORIZONTAL, command =update)
            BL_wlabel = Label(label_frame_bottom, text = "Bottom Left Width")
            BL_wscale.set(0)
            
            BL_wscale.grid(row=4,column=1)
            BL_wlabel.grid(row=5,column=1)
            
        if BR_hscale == 0:
            BR_hscale = Scale(label_frame_bottom,from_ = int((0-BR[1])/3), to = int(((height-BR[1]))/3), orient = HORIZONTAL, command =update)
            BR_hlabel = Label(label_frame_bottom, text = "Bottom Right Height")
            BR_hscale.set(0)
            
            BR_hscale.grid(row=6,column=0)
            BR_hlabel.grid(row=7,column=0)
            
        if BR_wscale == 0:
            BR_wscale = Scale(label_frame_bottom,from_ = int((0-BR[0])/3), to = int(((width-BR[0]))/2), orient = HORIZONTAL, command =update)
            BR_wlabel = Label(label_frame_bottom, text = "Bottom Right Width")
            BR_wscale.set(0)
            
            BR_wscale.grid(row=6,column=1)
            BR_wlabel.grid(row=7,column=1)
            
        reset_button = Button(label_frame_bottom, text="RESET", width=20, height =4, command = reset)
        reset_button.grid(row=16,column=0,columnspan=2,padx=5,pady=2)
        
    elif shift == 2:
        return_button = Button(label_frame_top, text= "RETURN", height = 4, width = 20,command = discard)
        return_button.grid(row=0,column=0,padx=5,pady=2)
        next_button = Button(label_frame_top, text = "NEXT >>", height = 4, width = 20, command = add)
        next_button.grid(row=1,column=0,padx=5,pady=2)
        prev_button = Button(label_frame_top, text = "<< PREVIOUS", height = 4, width = 20, command = sub)
        prev_button.grid(row=2,column=0,padx=5,pady=2)
        extract_button = Button(label_frame_top, text = "EXTRACT TEXT", height =4 ,width = 20, command = extract)
        extract_button.grid(row=3,column=0,padx=5,pady=2)
        #rotate_button = Button(label_frame_top, text = "ROTATE", height = 4, width = 20, command = rot)
        #rotate_button.grid(row=4,column=0,padx=5,pady=2)
        save_as_button = Button(label_frame_top, text = "CONVERT", height =4, width = 20, command = save_as)
        save_as_button.grid(row=4,column=0,padx=5,pady=2)
        
        TL_hscale1 = Scale(label_frame_bottom,from_ = int((0 - TL[1])/2), to = int(((BL[1]-TL[1]) - 20)/3), orient = HORIZONTAL, command =update, state = DISABLED)
        TL_hscale1.set(0)
            
        TL_hlabel1 = Label(label_frame_bottom, text = "Top Left Height")
            
        TL_hscale1.grid(row=0,column=0)
        TL_hlabel1.grid(row=1,column=0)
        
        TL_wscale1 = Scale(label_frame_bottom,from_ = int((0 - TL[0])/2), to = int(((TR[0]-TL[0]) - 20)/3), orient = HORIZONTAL, command =update, state = DISABLED)
        TL_wlabel1 = Label(label_frame_bottom, text = "Top Left Width")
        TL_wscale1.set(0)
            
        TL_wscale1.grid(row=0,column=1)
        TL_wlabel1.grid(row=1,column=1)
        
        TR_hscale1 = Scale(label_frame_bottom,from_ = int((0 - TR[1])/2), to = int(((BR[1]-TR[1]) - 20)/3), orient = HORIZONTAL, command =update, state = DISABLED)
        TR_hlabel1 = Label(label_frame_bottom, text = "Top Right Height")
        TR_hscale1.set(0)
            
        TR_hscale1.grid(row=2,column=0)
        TR_hlabel1.grid(row=3,column=0)
        
        TR_wscale1 = Scale(label_frame_bottom,from_ = int((0 - TR[0])/3), to = int(((width-TR[0]))/2), orient = HORIZONTAL, command =update, state = DISABLED)
        TR_wlabel1 = Label(label_frame_bottom, text = "Top Right Width")
        TR_wscale1.set(0)
            
        TR_wscale1.grid(row=2,column=1)
        TR_wlabel1.grid(row=3,column=1)
        
        BL_hscale1 = Scale(label_frame_bottom,from_ = int((0-BL[1])/3), to = int(((height-BL[1]))/3), orient = HORIZONTAL, command =update, state = DISABLED)
        BL_hlabel1 = Label(label_frame_bottom, text = "Bottom Left Height")
        BL_hscale1.set(0)
            
        BL_hscale1.grid(row=4,column=0)
        BL_hlabel1.grid(row=5,column=0)
        
        BL_wscale1 = Scale(label_frame_bottom,from_ = int((0-BL[0])/2), to = int(((BR[0]-BL[0]) - 20)/3), orient = HORIZONTAL, command =update, state = DISABLED)
        BL_wlabel1 = Label(label_frame_bottom, text = "Bottom Left Width")
        BL_wscale1.set(0)
            
        BL_wscale1.grid(row=4,column=1)
        BL_wlabel1.grid(row=5,column=1)
        
        BR_hscale1 = Scale(label_frame_bottom,from_ = int((0-BR[1])/3), to = int(((height-BR[1]))/3), orient = HORIZONTAL, command =update, state = DISABLED)
        BR_hlabel1 = Label(label_frame_bottom, text = "Bottom Right Height")
        BR_hscale1.set(0)
            
        BR_hscale1.grid(row=6,column=0)
        BR_hlabel1.grid(row=7,column=0)
        
        BR_wscale1 = Scale(label_frame_bottom,from_ = int((0-BR[0])/3), to = int(((width-BR[0]))/2), orient = HORIZONTAL, command =update, state= DISABLED)
        BR_wlabel1 = Label(label_frame_bottom, text = "Bottom Right Width")
        BR_wscale1.set(0)
            
        BR_wscale1.grid(row=6,column=1)
        BR_wlabel1.grid(row=7,column=1)
        
        reset_button = Button(label_frame_bottom, text="RESET", width=20, height =4, command = reset, state = DISABLED)
        reset_button.grid(row=16,column=0,columnspan=2,padx=5,pady=2)
        
        
        
            
                 
scanner()
buttons()
        
    
root.mainloop()
