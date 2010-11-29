#!/usr/bin/python
import os
import ImageFilter 
from Tkinter import *
import tkFileDialog
import Image
from tkMessageBox import *

class Convert:
    def imageConvert(self, image, format, file_name_out, size, graus , efects):
        try:   
            im = Image.open(image)
        except:
            return    
        nome = image.split('.')[0]
        nome = nome.split('/')[-1]
        im = im.rotate(graus)
        im = self.efects(im, efects)
        im.resize(size, Image.ANTIALIAS).save(file_name_out + '/' + nome + '.' + format.lower(), format.upper())

    def directoryConvert(self, file_name_in, format, file_name_out, size, graus, efects):
        for image in os.listdir(file_name_in):
            image = file_name_in + '/' + image
            self.imageConvert(image, format, file_name_out, size, graus, efects)
   
    def efects(self, im, list_efects):
        if(list_efects[0] == 1):
            im = im.convert('L')
        if(list_efects[1] == 1):
            im = im.convert('L').filter(ImageFilter.CONTOUR)
        if(list_efects[2] == 1):
            im = im.filter(ImageFilter.BLUR)
        if(list_efects[3] == 1):
            im = im.filter(ImageFilter.SMOOTH)
        return im                    
         
class PrincipalWindow:
    def __init__ (self, toplevel):
        self.frame0=Frame(toplevel,pady=10, bg = 'lightgreen', height = 10)  
        self.frame0.pack(fill=X, side = TOP)
        self.frame=Frame(toplevel,pady=10, bg = tk_rgb, height = 10)  
        self.frame.pack(fill=X, side = TOP)
        self.frame1=Frame(toplevel)
        self.frame1.pack()
        self.frame2=Frame(toplevel, pady=10, padx=5, bg = tk_rgb)
        self.frame2.pack(fill=X, expand=True)
        self.frame3=Frame(toplevel, pady=10, padx=5, bg = tk_rgb)
        self.frame3.pack(fill=X, expand=True)
        self.frame4=Frame(toplevel,pady=10, padx = 5, bg = tk_rgb)  
        self.frame4.pack(fill=X, expand=True)
        self.frame5=Frame(toplevel,pady=10, padx = 5, bg = tk_rgb)  
        self.frame5.pack(fill=X, expand=True)
        self.frame6=Frame(toplevel,pady=10, bg = tk_rgb)  
        self.frame6.pack()
        self.frame7=Frame(toplevel,pady=10, bg = 'lightgreen', height = 10)  
        self.frame7.pack(fill=X, side = BOTTOM)
        
        #****TITULO*****
        Label(self.frame1,text='Image Converter 1.0 Beta', fg='darkblue',
        font=('Verdana','14','bold'), height=1).pack()
        fonte1=('Verdana','10','bold')
        
        #****ENTRADA****
        Label(self.frame2,text='Input: ', font=fonte1,width=8).pack(side=LEFT)
        self.File_in=Entry(self.frame2,width=30, font=fonte1)
        self.File_in.focus_force() # Para o foco comecar neste campo
        self.File_in['bg'] = 'lightblue'
        self.File_in.pack(side=LEFT)
        self.search_file=Button(self.frame2, font=fonte1, text='Arquivo',
        bg='green', command=self.openDialogInFile)
        self.search_file.pack(side=RIGHT) 
        Label(self.frame2,text='', font=fonte1,width=1, bg=tk_rgb).pack(side=RIGHT)  
        self.search_directory=Button(self.frame2, font=fonte1, text='Diretorio',
        bg='green', command=self.openDialogInDirectory)
        self.search_directory.pack(side=RIGHT)
        
        #*****SAIDA*****
        Label(self.frame3,text='Output: ',
        font=fonte1,width=8).pack(side=LEFT)
        self.File_out=Entry(self.frame3,width=30,font=fonte1)
        self.File_out['bg'] = 'lightblue'
        self.File_out.pack(side=LEFT)
        self.search2=Button(self.frame3, font=fonte1, text='Abrir',
        bg='green', command=self.openDialogOut)
        self.search2.pack(side=LEFT)
        
        #****PROPRIEDADES******
        #----largura X altura----
        Label(self.frame4,text='Largura:',font=fonte1,width=8).pack(side=LEFT)
        self.Largura=Entry(self.frame4,width=6,font=fonte1)
        self.Largura['bg'] = 'lightblue'
        self.Largura.pack(side=LEFT)
        Label(self.frame4,text='Altura:',font=fonte1,width=8).pack(side=LEFT)
        self.Altura=Entry(self.frame4,width=6,font=fonte1)
        self.Altura['bg'] = 'lightblue'
        self.Altura.pack(side=LEFT) 
        #----formato de saida-----
        var = StringVar(self.frame4)
        var.set("jpeg") # initial value
        self.formato = OptionMenu(self.frame4, var, "jpeg", "gif", "bmp", "png",
        'tiff', 'pdf')
        self.formato.pack(side = RIGHT)
        Label(self.frame4,text='Formato:', font=fonte1,width=10).pack(side=RIGHT)
        #****ROTATE*****
        varRote = StringVar(self.frame5)
        varRote.set("0") # initial value
        self.Rote = OptionMenu(self.frame5, varRote, "0", "90", "180", "270")
        self.Rote.pack(side = RIGHT)
        Label(self.frame5,text='Girar:', font=fonte1,width=6).pack(side=RIGHT)

        
        #****BOTAO*****
        self.converte=Button(self.frame6, font=fonte1, text='Converter',
        bg='green', command=self.converter) 
        self.converte.pack()
       
        #****Check*****
        self.criaCheck()
        
        
    def converter(self):
        file_in = self.File_in.get()
        file_out = self.File_out.get()
        largura = self.Largura.get()
        altura =self.Altura.get()
        efects = [self.varA.get(), self.varB.get(), self.varC.get(), self.varD.get()]
        format = self.formato.cget('text')
        graus = int(self.Rote.cget('text'))
        erro = True
        if (file_in==''):
            showinfo('ERRO', 'Por favor preencha o campo input')
            self.File_in.focus_force()
        elif (file_out==''):
            showinfo('ERRO', 'Por favor preencha o campo output')
            self.File_out.focus_force()    
        elif (largura==''):
            showinfo('ERRO', 'Por favor preencha o campo largura')
            self.Largura.focus_force()
        elif (altura==''):
            showinfo('ERRO', 'Por favor preencha o campo altura')
            self.Altura.focus_force()                
        else:
            size = (int(largura), int(altura))
            if os.path.isfile(file_in) and os.path.isdir(file_out):
                erro = False
                convert.imageConvert(file_in, format, file_out, size, graus, efects)
            elif os.path.isdir(file_in) and os.path.isdir(file_out):
                erro = False         
                convert.directoryConvert(file_in, format, file_out, size, graus, efects)
            else:
                showinfo('ERRO', 'Alguns dos caminhos sao invalidos')
                self.File_in.focus_force()
            if not(erro):    
                self.clearEntrys()        
        
    def clearEntrys(self):
        self.File_in.delete(0, END)
        self.File_out.delete(0, END)
        self.File_in.focus_force()    
            
    def openDialogInFile(self):
        filename = tkFileDialog.askopenfilename().encode('utf8')
        self.File_in.delete(0, END)
        self.File_in.insert(0, filename)
        im = Image.open(filename)
        self.Altura.insert(0, im.size[1])
        self.Largura.insert(0, im.size[0])
        
    def openDialogInDirectory(self):
        filename = tkFileDialog.askdirectory().encode('utf8')
        self.File_in.delete(0, END)
        self.File_in.insert(0, filename)
                        

    def openDialogOut(self):
        filename = tkFileDialog.askdirectory().encode('utf8')
        self.File_out.delete(0, END)
        self.File_out.insert(0, filename)
        
    def criaCheck(self):
        self.varA = IntVar()
        self.varB = IntVar()
        self.varC = IntVar()
        self.varD = IntVar()
        self.a = Checkbutton(self.frame5, text = 'gray scale', width = 7,
        padx = 5, variable=self.varA)  
        self.b = Checkbutton(self.frame5, text = 'contour', width = 7,
        padx = 5, variable=self.varB)
        self.c = Checkbutton(self.frame5, text = 'blur', width = 7, 
        padx = 5, variable=self.varC)
        self.d = Checkbutton(self.frame5, text = 'smooth', width = 7,
        padx = 5, variable=self.varD)  
        self.a.pack(side = LEFT)
        self.b.pack(side = LEFT)
        self.c.pack(side = LEFT)
        self.d.pack(side = LEFT)
        
if __name__ == "__main__":
    convert = Convert()
    raiz=Tk()
    raiz.title('Image Converter')
    tk_rgb = "#%02x%02x%02x" % (100, 100, 100)
    raiz['bg'] = tk_rgb
    PrincipalWindow(raiz)
    raiz.mainloop()
 
