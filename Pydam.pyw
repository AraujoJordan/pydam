#!/usr/bin/env python5
# -*- coding: utf-8 -*-

import time
import platform
import sys
if sys.version_info[0] == 3:
    from tkinter import *
    from tkinter import messagebox
    from tkinter import filedialog
else:
    from Tkinter import *
    import tkMessageBox as messagebox
    import tkFileDialog as filedialog

pecas=['V', 'V', 'V', 'P', 'V', 'V', 'V', 'V',
        'V', 'V', 'V', 'V', 'V', 'V', 'B', 'V',
        'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V',
        'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V',
        'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V',
        'V', 'V', 'V', 'V', 'P', 'V' , 'V', 'V',
        'V', 'V', 'V', 'V', 'V', 'V', 'V', 'P',
        'B', 'V', 'B', 'V', 'B', 'V' , 'B', 'V']

contb=12
contp=12
situacao=1
#sit1 =  esperando usuario clicar em alguma peça
#sit2 = esperando escolher a posivel situaçao da peca

peca_inicial=1
peca_final=1
peca_inimiga=100
apague_menu = True


#-------------------------------------------------------------------------------------------------------------------------------------------------------------   
# INÍCIO DA HEURÍSTICA
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


def heuristica():
    pos1=[None]*200
    pos2=[None]*200
    porc=[0]*200
    posdm=[None]*200

    ver=True
    i=0
    p1=0
    p2=0
    pdm=0
    prc=0

#-------------------------------------------------------------------------------------------------------------------------------------------------------------   
# POSSIBILIDADE DE FAZER DAMA:
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# p1 é a posição inicial, p2 é a posição final
# verificando se tem possibilidade de dama:
    if(pecas[49] == 'P'):
        if(pecas[56] == 'V'):
            ver=False
            p1 = 49
            p2 = 56
            pdm = 100
        if(pecas[58] == 'V'):
            ver=False
            p1 = 49
            p2 = 58
            pdm = 100

    if(pecas[51] == 'P'):
        if(pecas[58] == 'V'):
            ver=False
            p1 = 51
            p2 = 58
            pdm = 100
        if(pecas[60] == 'V'):
            ver=False
            p1 = 51
            p2 = 60
            pdm = 100

    if(pecas[53] == 'P'):
        if(pecas[60] == 'V'):
            ver=False
            p1 = 53
            p2 = 60
            pdm = 100
        if(pecas[62] == 'V'):
            ver=False
            p1 = 53
            p2 = 62
            pdm = 100

    if(pecas[55] == 'P'):
        if(pecas[62] == 'V'):
            ver=False
            p1 = 55
            p2 = 62
            pdm = 100
   
    
# 11 ifs até aqui
#-------------------------------------------------------------------------------------------------------------------------------------------------------------   
# SE CONSEGUIR FAZER DAMA, POSSIBILIDADES DE DAMA COMER AS PEÇAS:
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


    if(ver):
        ind=0
        while(ind < 64):
            if(pecas[ind] == 'DP'):
                if((ind == 1)or(ind == 8)):
                    if(((pecas[ind + 9] == 'B')or(pecas[ind + 9] == 'DB'))and(pecas[ind + 18] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind + 18
                        porc[i] = 100
                        posdm[i]= ind + 9
                        i += 1
                        ind += 1
                        

                        
                if((ind == 3)or(ind == 5)or(ind == 10)or(ind == 12)):
                    if(((pecas[ind + 7] == 'B')or(pecas[ind + 7] == 'DB'))and(pecas[ind + 14] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind + 14
                        porc[i] = 100
                        posdm[i]= ind + 7
                        i += 1
                        ind += 1
                        
                    if(((pecas[ind + 9] == 'B')or(pecas[ind + 9] == 'DB'))and(pecas[ind + 18] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind + 18
                        porc[i] = 100
                        posdm[i]= ind + 8
                        i += 1
                        ind += 1
                        

                        
                if((ind == 7) or (ind == 14)):
                    if(((pecas[ind + 7] == 'B')or(pecas[ind + 7] == 'DB'))and(pecas[ind + 14] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind + 14
                        porc[i] = 100
                        posdm[i]= ind + 7
                        i += 1
                        ind += 1
                        

                        
                if((ind==17)or(ind==19)or(ind==21)or(ind==24)or(ind==26)or(ind==28)or(ind==33)or(ind==35)or(ind==37)or(ind==40)or(ind==42)or(ind==44)):
                    if(((pecas[ind - 7] == 'B')or(pecas[ind - 7] == 'DB'))and(pecas[ind - 14] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind - 14
                        porc[i] = 100
                        posdm[i]= ind - 7
                        i += 1
                        ind += 1
                        
                    if(((pecas[ind + 9] == 'B')or(pecas[ind + 9] == 'DB'))and(pecas[ind + 18] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind + 18
                        porc[i] = 100
                        posdm[i]= ind + 9
                        i += 1
                        ind += 1
                        

                       
                if((ind==23)or(ind==19)or(ind==21)or(ind==26)or(ind==28)or(ind==30)or(ind==35)or(ind==37)or(ind==39)or(ind==42)or(ind==44)or(ind==46)):
                    if(((pecas[ind - 9] == 'B')or(pecas[ind - 9] == 'DB'))and(pecas[ind - 18] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind - 18
                        porc[i] = 100
                        posdm[i]= ind - 9
                        i += 1
                        ind += 1
                        
                    if(((pecas[ind + 7] == 'B')or(pecas[ind + 7] == 'DB'))and(pecas[ind + 14] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind + 14
                        porc[i] = 100
                        posdm[i]= ind + 7
                        i += 1
                        ind += 1
                        
                       

                if((ind == 49)or(ind == 56)):
                    if(((pecas[ind - 7] == 'B')or(pecas[ind - 7] == 'DB'))and(pecas[ind - 14] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind - 14
                        porc[i] = 100
                        posdm[i]= ind - 7
                        i += 1
                        ind += 1
                        

                       
                if((ind == 62)or(ind == 55)):
                    if(((pecas[ind - 9] == 'B')or(pecas[ind - 9] == 'DB'))and(pecas[ind - 18] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind - 18
                        porc[i] = 100
                        posdm[i]= ind - 9
                        i += 1
                        ind += 1
                        


                if((ind == 58)or(ind == 51)or(ind == 60)or(ind == 53)):
                   if(((pecas[ind - 7] == 'B')or(pecas[ind - 7] == 'DB'))and(pecas[ind - 14] == 'B')):
                        pos1[i] = ind
                        pos2[i] = ind - 14
                        porc[i] = 100
                        posdm[i]= ind - 7
                        i += 1
                        ind += 1
                        
                   if(((pecas[ind - 9] == 'B')or(pecas[ind - 9] == 'DB'))and(pecas[ind - 18] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind - 18
                        porc[i] = 100
                        posdm[i]= ind - 9
                        i += 1
                        ind += 1
                        


# 33 ifs até aqui
#-------------------------------------------------------------------------------------------------------------------------------------------------------------   
# POSSIBILIDADE DE PEÇAS PRETAS SEM SER DAMA COMER AS OUTRAS PEÇAS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



            if(pecas[ind] =='P'):
                if((ind==1)or(ind==3)or(ind==5)or(ind==8)or(ind==10)or(ind==12)or(ind==17)or(ind==19)or(ind==21)or(ind==24)or(ind==26)or(ind==28)or(ind==33)or(ind==35)or(ind==37)or(ind==40)or(ind==42)or(ind==44)):
                    if(((pecas[ind + 9] == 'B')or(pecas[ind + 9] == 'DB'))and(pecas[ind - 18] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind + 18
                        porc[i] = 100
                        posdm[i]= ind + 9
                        i += 1
                        ind += 1
                        
                   
                if((ind==7)or(ind==3)or(ind==5)or(ind==14)or(ind==10)or(ind==12)or(ind==23)or(ind==19)or(ind==21)or(ind==30)or(ind==26)or(ind==28)or(ind==39)or(ind==35)or(ind==37)or(ind==46)or(ind==42)or(ind==44)):
                    if(((pecas[ind + 7] == 'B')or(pecas[ind + 7] == 'DB'))and(pecas[ind + 14] == 'V')):
                        pos1[i] = ind
                        pos2[i] = ind + 14
                        porc[i] = 100
                        posdm[i]= ind + 7
                        i += 1
                        ind += 1
            ind +=1        
            
# 37 ifs até aqui
#-------------------------------------------------------------------------------------------------------------------------------------------------------------   
# MOVIMENTO DAS DAMAS PRETAS (SEM COMER NADA)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


        ind = 0
                       
        while(ind < 64):
            if(pecas[ind] == 'DP'):
                    if(ind == 7):
                        if(pecas[ind + 7] == 'V'):
                            pos1[i] = ind
                            pos2[i] = ind + 7
                            porc[i] = 80
                            posdm[i]= 100
                            i += 1
                            ind += 1

                       
                    if(ind == 56):
                        if(pecas[ind - 7] == 'V'):
                            pos1[i] = ind
                            pos2[i] = ind - 7
                            porc[i] = 80
                            posdm[i]= 100
                            i += 1
                            ind += 1

                       
                    if((ind == 1)or(ind == 3)or(ind == 5)):
                       if(pecas[ind + 7] == 'V'):
                            pos1[i] = ind
                            pos2[i] = ind + 7
                            porc[i] = 80
                            posdm[i]= 100
                            i += 1
                            ind += 1
                       if(pecas[ind + 9] == 'V'):
                            pos1[i] = ind
                            pos2[i] = ind + 9
                            porc[i] = 80
                            posdm[i]= 100
                            i += 1
                            ind += 1

                       
                    if((ind==8)or(ind==10)or(ind==12)or(ind==14)or(ind==17)or(ind==19)or(ind==21)or(ind==24)or(ind==26)or(ind==28)or(ind==30)or(ind==33)or(ind==35)or(ind==37)or(ind==40)or(ind==42)or(ind==44)or(ind==46)or(ind==49)or(ind==51)or(ind==53)):
                       if(pecas[ind - 7] == 'V'):
                            pos1[i] = ind
                            pos2[i] = ind - 7
                            porc[i] = 80
                            posdm[i]= 100
                            i += 1
                            ind += 1
                       if(pecas[ind + 9] == 'V'):
                            pos1[i] = ind
                            pos2[i] = ind + 9
                            porc[i] = 80
                            posdm[i]= 100
                            i += 1
                            ind += 1

                       
                    if((ind==23)or(ind==10)or(ind==12)or(ind==14)or(ind==17)or(ind==19)or(ind==21)or(ind==39)or(ind==26)or(ind==28)or(ind==30)or(ind==33)or(ind==35)or(ind==37)or(ind==55)or(ind==42)or(ind==44)or(ind==46)or(ind==49)or(ind == 51)or(ind==53)):
                       if(pecas[ind + 7] == 'V'):
                            pos1[i] = ind
                            pos2[i] = ind + 7
                            porc[i] = 80
                            posdm[i]= 100
                            i += 1
                            ind += 1
                       if(pecas[ind - 9] == 'V'):
                            pos1[i] = ind
                            pos2[i] = ind - 9
                            porc[i] = 80
                            posdm[i]= 100
                            i += 1
                            ind += 1

                       
                    if((ind == 58)or(ind == 60)or(ind == 62)):
                       if(pecas[ind - 7] == 'V'):
                            pos1[i] = ind
                            pos2[i] = ind - 7
                            porc[i] = 90
                            posdm[i]= 100
                            i += 1
                            ind += 1
                       if(pecas[ind - 9] == 'V'):
                            pos1[i] = ind
                            pos2[i] = ind - 9
                            porc[i] = 90
                            posdm[i]= 100
                            i += 1
                            ind += 1



# 54 ifs até aqui
#-------------------------------------------------------------------------------------------------------------------------------------------------------------   
# MOVIMENTO DAS PEÇAS PRETAS (SEM COMER NADA)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


            if(pecas[ind] =='P'):
                if((ind == 7) or (ind == 1) or (ind == 3) or (ind == 5) or (ind == 10) or (ind == 12) or (ind == 14) or (ind == 23) or (ind == 17) or (ind == 19) or (ind == 21) or (ind == 39) or (ind == 26) or (ind == 28) or (ind == 30) or (ind == 33) or (ind == 35) or (ind == 37) or (ind == 42) or (ind == 44) or (ind == 46)):
                        if(pecas[ind + 7] == 'V'):
                                pos1[i] = ind
                                pos2[i] = ind + 7
                                porc[i] = 80
                                posdm[i]= 100
                                i += 1
                                ind += 1

                       
                if((ind == 8) or (ind == 1) or (ind == 3) or (ind == 5) or (ind == 10) or (ind == 12) or (ind == 14) or (ind == 24) or (ind == 17) or (ind == 19) or (ind == 21) or (ind == 26) or (ind == 28) or (ind == 30) or (ind == 40) or (ind == 33) or (ind == 35) or (ind == 37) or (ind == 42) or (ind == 44) or (ind == 46)):
                        if(pecas[ind + 9] == 'V'):
                                pos1[i] = ind
                                pos2[i] = ind + 9
                                porc[i] = 80
                                posdm[i]= 100
                                i += 1
                                ind += 1
            ind +=1

# 58 ifs até aqui
#-------------------------------------------------------------------------------------------------------------------------------------------------------------   
# FILTRO DE JOGADAS
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



        if(pos1[0] == None):

            contp = 0
            ind = 0

        while(ind<200):
            if(pos1[ind] != None):
                if((pos2[ind]==1)or(pos2[ind]==3)or(pos2[ind]==5)or(pos2[ind]==7)or(pos2[ind]==23)or(pos2[ind]==39)or(pos2[ind]==55)or(pos2[ind]==56)or(pos2[ind]==58)or(pos2[ind]==60)or(pos2[ind]==62)or(pos2[ind]==8)or(pos2[ind]==24)or(pos2[ind]== 40)):
                    ind += 1
                else:
                    porc[ind] = porc[ind] - 10
                    ind += 1
            else:
                break
                       
        ind = 0
                       
        while(ind<200):
            if(pos1[ind] != None):
                if((ind == 1)or(ind == 3)or(ind == 5)or(ind == 7)):
                    if(pos1[ind] == 'P'):
                        porc[ind] = proc[ind] - 20
                        ind += 1
                    else:
                        ind += 1
                else:
                    ind += 1
            else:
                break

        ind = 0

        while(ind<200):
            pt = pos1[ind]
            ps = pos2[ind]
            if(pt != None):
                if(((pecas[pt] == 'P') or (pecas[pt] == 'DP')) and (pecas[ps] == 'V')):
                    if(porc[ind] != 0):
                        if(porc[ind] > prc):
                            p1 = pos1[ind]
                            p2 = pos2[ind]
                            pdm = posdm[ind]
                            prc = porc[ind]
                            ind += 1
                    else:
                        break
            ind += 1
    if(pdm == 100):
        movepec(p1,p2)
    else:
        comepec(p1,pdm, p2)
    return

#-------------------------------------------------------------------------------------------------------------------------------------------------------------   
# FIM HEURÍSTICA 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



def verificaprox():
    if(peca_final-peca_inicial==(7)):
       return True
    if(peca_final-peca_inicial==(9)):
       return True
    if(peca_final-peca_inicial==(-7)):
       return True
    if(peca_final-peca_inicial==(-9)):
       return True
    else:
       return False
def verbloq(indice,x):
    global pecas
    if ((pecas[indice+x]=='B')or(pecas[indice+x]=='DB')):
        return True;
    if (((pecas[indice+x]=='P')or(pecas[indice+x]=='DP'))and(pecas[indice+x+x]!='V')):
        return True;
    else:
        return False;
def vermov(indice,x):
    if(pecas[indice+x]=='V'):
        return True;
    else:
        return False;
def vercom(indice,x):
    if (((pecas[indice+x]=='P') or (pecas[indice+x]=='DP'))and(pecas[indice+x+x]=='V')):
        return True;
    else:
        return False;             
def movepec (casa_inicial, casa_final):
    global pecas
    global peca_inicial, peca_final
    pecas[casa_final] = pecas[casa_inicial]
    pecas[casa_inicial]='V'
    peca_inicial=100
    peca_final=100
    if (((casa_final==1) or (casa_final==3) or (casa_final==5) or (casa_final==7))and (pecas[casa_final]=='B')):
        pecas[casa_final]='DB'
    if (((casa_final==56) or (casa_final==58) or (casa_final==60) or (casa_final==62))and (pecas[casa_final]=='P')):
        pecas[casa_final]='DP'
    return
        
def comepec(casa_inicial, casa_inimiga, casa_final):
    global pecas
    global contb, contp, peca_inicial, peca_final, peca_inimiga
    if ((pecas[casa_inimiga]=='P')or(pecas[casa_inimiga]=='DP')):
        contp=contp-1
    else:
        contb=contb-1
    pecas[casa_final]=pecas[casa_inicial]
    pecas[casa_inicial]='V'  
    pecas[casa_inimiga]='V'
    peca_inicial=100
    peca_final=100
    peca_inimiga=100
    if (((casa_final==1) or (casa_final==3) or (casa_final==5) or (casa_final==7))and (pecas[casa_final]=='B')):
        pecas[casa_final]='DB'
    if (((casa_final==56) or (casa_final==58) or (casa_final==60) or (casa_final==62))and (pecas[casa_final]=='P')):
        pecas[casa_final]='DP'
    return
#---------------------------------------------
# JANELA PRINCIPAL
#--------------------------------------------
class JanelaPrincipal:
    def __init__(self, toplevel):

        self.app=toplevel
        
        self.app.title("Pydam 0.5 BETA")
        if platform.system() == "Linux":
            self.app.iconbitmap('@imagens/pydam.xbm')
        else:
            self.app.iconbitmap('imagens/pydam.ico')

        self.menu = Menu(app)
        self.app.config(menu = self.menu)

        self.arqmenu = Menu(app)
        self.menu.add_cascade(label="Arquivo", menu=self.arqmenu)
        self.arqmenu.add_command(label="Novo Jogo", command=self.restart)
        self.arqmenu.add_separator()
        self.arqmenu.add_command(label="Sair para o Menu", command=self.menu_principal)
        self.arqmenu.add_command(label="Sair do Pydam", command=self.fechar)

        self.helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="Ajuda", menu=self.helpmenu)
        self.helpmenu.add_command(label="Créditos", command=self.creditos)

        self.app.protocol("WM_DELETE_WINDOW", self.fechar)

        self.primprint=1
        global contb
        global contp
        global situacao
        
        self.menu_principal()

        #--------------------------------------------------------------------------------------
        #           MENU
        #--------------------------------------------------------------------------------------
    def menu_principal(self):
        global apague_menu
        if (self.primprint!=1):
            if messagebox.askokcancel(title = 'Sair do jogo', message = 'Você tem certeza que quer sair? Seu jogo será perdido.'):
                self.apaga_casas()

        photo = PhotoImage(file='imagens/Pydamlogo.gif')
        self.printi = Label(image=photo)
        self.printi.photo = photo
        self.printi.pack()
                
        self.iniciandogame = Frame(pady=5)
        self.iniciandogame.pack()
        self.novo_jogo_b=Button(self.iniciandogame,width=20,bg='white', font=('Verdana','12','bold'), text="Novo jogo", command=self.restart)
        self.novo_jogo_b.pack()

        self.creditosf = Frame(pady=5)
        self.creditosf.pack()
        self.creditos_b=Button(self.creditosf,width=20,font=('Verdana','12','bold'),  bg='white',text="Creditos", command=self.creditos)
        self.creditos_b.pack()

        self.sairf=Frame(pady=5)
        self.sairf.pack()
        self.sair_b=Button(self.sairf,width=20,font=('Verdana','12','bold'), bg='white', text="Sair",command=self.fechar)
        self.sair_b.pack()

        self.abaixo_info=Label(text="Jogo desenvolvido para trabalho acadêmico. Proibido seu uso comercial.")
        self.abaixo_info.pack()
        self.menu_ok=True
    def sair_de_menu(self):
                self.iniciandogame.destroy()
                self.novo_jogo_b.destroy()
                self.creditosf.destroy()
                self.creditos_b.destroy()
                self.sairf.destroy()
                self.sair_b.destroy()
                self.printi.destroy()
                self.abaixo_info.destroy()
            
        #--------------------------------------------------------------------------------------
        #AQUI COMEÇA AS POSSIBILIDADES POR CASA DO USUARIO
        #--------------------------------------------------------------------------------------
    def normal2(self,indice):
        global situacao, peca_inicial, peca_final, peca_inimiga
        global pecas
        if(vermov(indice,-9)):
           peca_inicial=indice
           pecas[indice-9]='S'
           situacao=2
        if(vermov(indice,-7)):
           pecas[indice-7]='S'
           peca_inicial=indice
           situacao=2
        if(indice-9-9>0):
           if(vercom(indice,-9)):
               pecas[indice-18]='S'
               peca_inicial=indice
               situacao=2
        if(indice-7-7>0):
           if(vercom(indice,-7)):
               pecas[indice-14]='S'
               peca_inicial=indice
               situacao=2
        return self.refresh()
    def lateral_esq_normal(self,indice):
        global situacao, peca_inicial, peca_final, peca_inimiga
        global pecas
        if(vermov(indice,-7)):
           pecas[indice-7]='S'
           peca_inicial=indice
           situacao=2
        if(indice-7-7>0):
           if(vercom(indice,-7)):
               pecas[indice-14]='S'
               peca_inicial=indice
               situacao=2
        return self.refresh()
    def lateral_dir_normal(self,indice):
        global situacao, peca_inicial, peca_final, peca_inimiga
        global pecas
        if(vermov(indice,-9)):
           peca_inicial=indice
           pecas[indice-9]='S'
           situacao=2
        if(indice-9-9>0):
           if(vercom(indice,-9)):
               pecas[indice-18]='S'
               peca_inicial=indice
               situacao=2
        return self.refresh()
    def acima_dama(self,indice):
        global situacao, peca_inicial, peca_final, peca_inimiga
        global pecas
        if(vermov(indice,7)):
           pecas[indice+7]='S'
           peca_inicial=indice
           situacao=2
        if(vermov(indice,9)):
           pecas[indice+9]='S'
           peca_inicial=indice
           situacao=2
        if(indice+9+9<64):
            if(vercom(indice,9)):
               situacao=2
               peca_inicial=indice
               pecas[indice+18]='S'
        if(indice+7+7<64):
            if(vercom(indice,7)):
               situacao=2
               peca_inicial=indice
               pecas[indice+14]='S'
        return self.refresh()
    def dama_lateral_esq(self,indice):
        global situacao, peca_inicial, peca_final, peca_inimiga
        global pecas
        if(vermov(indice,9)):
           pecas[indice+9]='S'
           peca_inicial=indice
           situacao=2
        if(vermov(indice,-7)):
           pecas[indice-7]='S'
           peca_inicial=indice
           situacao=2
        if(indice+9+9<64):
            if(vercom(indice,9)):
               situacao=2
               peca_inicial=indice
               pecas[indice+18]='S'
        if(indice-7-7>0):
           if(vercom(indice,-7)):
               pecas[indice-14]='S'
               peca_inicial=indice
               situacao=2
        return self.refresh()   
    def dama_lateral_dir(self,indice):
        global situacao, peca_inicial, peca_final, peca_inimiga
        global pecas
        if(vermov(indice,-9)):
           peca_inicial=indice
           pecas[indice-9]='S'
           situacao=2
        if(vermov(indice,7)):
           pecas[indice+7]='S'
           peca_inicial=indice
           situacao=2
        if(indice-9-9>0):
           if(vercom(indice,-9)):
               pecas[indice-18]='S'
               peca_inicial=indice
               situacao=2
        if(indice+7+7<64):
            if(vercom(indice,7)):
               situacao=2
               peca_inicial=indice
               pecas[indice+14]='S'  
        return self.refresh()   
    def dama_normal4(self, indice):
        global situacao, peca_inicial, peca_final, peca_inimiga
        global pecas
        if(vermov(indice,-9)):
           peca_inicial=indice
           pecas[indice-9]='S'
           situacao=2
        if(vermov(indice,-7)):
           pecas[indice-7]='S'
           peca_inicial=indice
           situacao=2
        if(vermov(indice,7)):
           pecas[indice+7]='S'
           peca_inicial=indice
           situacao=2
        if(vermov(indice,9)):
           pecas[indice+9]='S'
           peca_inicial=indice
           situacao=2
        if(indice-9-9>0):
           if(vercom(indice,-9)):
               pecas[indice-18]='S'
               peca_inicial=indice
               situacao=2
        if(indice-7-7>0):
           if(vercom(indice,-7)):
               pecas[indice-14]='S'
               peca_inicial=indice
               situacao=2
        if(indice+9+9<64):
            if(vercom(indice,9)):
               situacao=2
               peca_inicial=indice
               pecas[indice+18]='S'
        if(indice+7+7<64):
            if(vercom(indice,7)):
               situacao=2
               peca_inicial=indice
               pecas[indice+14]='S'
        return self.refresh()
       
    #-------------------------------------------------------------------------------------
    # AQUI TERMINA AS POSSIBILIDADES POR CASA DO USUARIO
    # ---------------------------------------------------------------------------------------
    def restart(self):
        global contb
        global contp
        global pecas
        if messagebox.askokcancel(title='Você tem certeza?', message='Você tem certeza que quer começar um novo jogo?'):        
                pecas=['V', 'P', 'V', 'P', 'V', 'P', 'V', 'P',
                       'P', 'V', 'P', 'V', 'P', 'V', 'P', 'V',
                       'V', 'P', 'V', 'P', 'V', 'P', 'V', 'P',
                       'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V',
                       'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V',
                       'B', 'V', 'B', 'V', 'B', 'V' , 'B', 'V',
                       'V', 'B', 'V', 'B', 'V', 'B', 'V', 'B',
                       'B', 'V', 'B', 'V', 'B', 'V' , 'B', 'V']              
                contb=12
                contp=12
                if(self.menu_ok==True):
                    self.sair_de_menu()
                    self.menu_ok=False
                self.refresh()
    def creditos(self):
            messagebox.showinfo( "Créditos", "Jogo feito por alunos da Universidade Federal \n"
                                                       "da Paraíba para trabalho acadêmico da cadeira de Lógica Aplicada \n"
                                                       "a Computação. Caso alteração, notifique aos autores."
                                                       "\nContato:   jordan@di.ufpb.br \n irsa@di.ufpb.br ")
    def fechar(self):
            if messagebox.askokcancel(title = 'Sair', message = 'Você tem certeza que quer sair?'):
                app.destroy()
    def casasescuras(self, indice ):
            if (pecas[indice]=='V'):
                return self.vazio
            if (pecas[indice]=='B'):
                return self.pecb
            if (pecas[indice]=='P'):
                return self.pecp
            if (pecas[indice]=='DP'):
                return self.damp
            if (pecas[indice]=='DB'):
                return self.damb
            if (pecas[indice]=='S'):
                return self.brilha
    def apaga_casas(self):
        self.taba.destroy()
        self.tabb.destroy()
        self.tabc.destroy()
        self.tabd.destroy()
        self.tabf.destroy()
        self.tabe.destroy()
        self.tabg.destroy()
        self.tabh.destroy()
        self.c00.destroy()
        self.c01.destroy()
        self.c02.destroy()
        self.c03.destroy()
        self.c04.destroy()
        self.c05.destroy()
        self.c06.destroy()
        self.c07.destroy()
        self.c08.destroy()
        self.c09.destroy()
        self.c10.destroy()
        self.c11.destroy()
        self.c12.destroy()
        self.c13.destroy()
        self.c14.destroy()
        self.c15.destroy()
        self.c16.destroy()
        self.c17.destroy()
        self.c18.destroy()
        self.c19.destroy()
        self.c20.destroy()
        self.c21.destroy()
        self.c22.destroy()
        self.c23.destroy()
        self.c24.destroy()
        self.c25.destroy()
        self.c26.destroy()
        self.c27.destroy()
        self.c28.destroy()
        self.c29.destroy()
        self.c30.destroy()
        self.c31.destroy()
        self.c32.destroy()
        self.c33.destroy()
        self.c34.destroy()
        self.c35.destroy()
        self.c36.destroy()
        self.c37.destroy()
        self.c38.destroy()
        self.c39.destroy()
        self.c40.destroy()
        self.c41.destroy()
        self.c42.destroy()
        self.c43.destroy()
        self.c44.destroy()
        self.c45.destroy()
        self.c46.destroy()
        self.c47.destroy()
        self.c48.destroy()
        self.c49.destroy()
        self.c50.destroy()
        self.c51.destroy()
        self.c52.destroy()
        self.c53.destroy()
        self.c54.destroy()
        self.c55.destroy()
        self.c56.destroy()
        self.c57.destroy()
        self.c58.destroy()
        self.c59.destroy()
        self.c60.destroy()
        self.c61.destroy()
        self.c62.destroy()
        self.c63.destroy()
        
    def refresh(self):
            if (self.primprint == 0):
                self.apaga_casas()
            
            casab = PhotoImage(file='imagens/branca.gif')
            self.vazio = PhotoImage(file='imagens/preta.gif')
            self.pecb = PhotoImage(file='imagens/pecabranca.gif')
            self.pecp = PhotoImage(file='imagens/pecapreta.gif')
            self.damb = PhotoImage(file='imagens/damabranca.gif')
            self.damp = PhotoImage(file='imagens/damapreta.gif')
            self.brilha = PhotoImage(file='imagens/brilha.gif')

            self.primprint = 0
            
            self.tabh = Frame()
            self.tabh.pack()

            self.c00 = Button(self.tabh, width=50, height=50, image=casab)
            self.c00.image = casab
            self.c00.pack(side=LEFT)

            casa1= self.casasescuras(1)
            self.c01=Button(self.tabh, width=50, height=50, image=casa1,command=lambda :self.acao(1))
            self.c01.image=casa1
            self.c01.pack(side=LEFT)
            
            self.c02 = Button(self.tabh, width=50, height=50, image=casab)
            self.c02.image=casab
            self.c02.pack(side=LEFT)

            casa3= self.casasescuras(3)
            self.c03=Button(self.tabh, width=50, height=50, image=casa3,command=lambda :self.acao(3))
            self.c03.image=casa3
            self.c03.pack(side=LEFT)

            self.c04 = Button(self.tabh, width=50, height=50, image=casab)
            self.c04.image=casab
            self.c04.pack(side=LEFT)

            casa5= self.casasescuras(5)
            self.c05=Button(self.tabh, width=50, height=50, image=casa5,command=lambda :self.acao(5))
            self.c05.image=casa5
            self.c05.pack(side=LEFT)

            self.c06 = Button(self.tabh, width=50, height=50, image=casab)
            self.c06.image=casab
            self.c06.pack(side=LEFT)

            casa7= self.casasescuras(7)
            self.c07=Button(self.tabh, width=50, height=50, image=casa7,command=lambda :self.acao(7))
            self.c07.image=casa7
            self.c07.pack(side=LEFT)

            self.tabg = Frame()
            self.tabg.pack()

            casa8= self.casasescuras(8)
            self.c08=Button(self.tabg, width=50, height=50, image=casa8,command=lambda :self.acao(8))
            self.c08.image=casa8
            self.c08.pack(side=LEFT)

            self.c09= Button(self.tabg, width=50, height=50, image=casab)
            self.c09.image=casab
            self.c09.pack(side=LEFT)

            casa10= self.casasescuras(10)
            self.c10=Button(self.tabg, width=50, height=50, image=casa10,command=lambda :self.acao(10))
            self.c10.image=casa10
            self.c10.pack(side=LEFT)

            self.c11= Button(self.tabg, width=50, height=50, image=casab)
            self.c11.image=casab
            self.c11.pack(side=LEFT)

            casa12= self.casasescuras(12)
            self.c12=Button(self.tabg, width=50, height=50, image=casa12,command=lambda :self.acao(12))
            self.c12.image=casa12
            self.c12.pack(side=LEFT)

     
            self.c13= Button(self.tabg, width=50, height=50, image=casab)
            self.c13.image=casab
            self.c13.pack(side=LEFT)

            casa14= self.casasescuras(14)
            self.c14=Button(self.tabg, width=50, height=50, image=casa14,command=lambda :self.acao(14))
            self.c14.image=casa14
            self.c14.pack(side=LEFT)


            self.c15= Button(self.tabg, width=50, height=50, image=casab)
            self.c15.image=casab
            self.c15.pack(side=LEFT)

            self.tabf = Frame()
            self.tabf.pack()

            self.c16= Button(self.tabf, width=50, height=50, image=casab)
            self.c16.image=casab
            self.c16.pack(side=LEFT)

            casa17= self.casasescuras(17)
            self.c17=Button(self.tabf, width=50, height=50, image=casa17,command=lambda :self.acao(17))
            self.c17.image=casa17
            self.c17.pack(side=LEFT)


            self.c18= Button(self.tabf, width=50, height=50, image=casab)
            self.c18.image = casab
            self.c18.pack(side=LEFT)

            casa19= self.casasescuras(19)
            self.c19=Button(self.tabf, width=50, height=50, image=casa19,command=lambda :self.acao(19))
            self.c19.image=casa19
            self.c19.pack(side=LEFT)

            self.c20= Button(self.tabf, width=50, height=50, image=casab)
            self.c20.image = casab
            self.c20.pack(side=LEFT)

            casa21= self.casasescuras(21)
            self.c21=Button(self.tabf, width=50, height=50, image=casa21,command=lambda :self.acao(21))
            self.c21.image=casa21
            self.c21.pack(side=LEFT)

            self.c22= Button(self.tabf, width=50, height=50, image=casab)
            self.c22.image = casab
            self.c22.pack(side=LEFT)

            casa23= self.casasescuras(23)
            self.c23=Button(self.tabf, width=50, height=50, image=casa23,command=lambda :self.acao(23))
            self.c23.image=casa23
            self.c23.pack(side=LEFT)
            
            self.tabe = Frame()
            self.tabe.pack()

            casa24= self.casasescuras(24)
            self.c24=Button(self.tabe, width=50, height=50, image=casa24,command=lambda :self.acao(24))
            self.c24.image=casa24
            self.c24.pack(side=LEFT)

            self.c25= Button(self.tabe, width=50, height=50, image=casab)
            self.c25.image = casab
            self.c25.pack(side=LEFT)

            casa26= self.casasescuras(26)
            self.c26=Button(self.tabe, width=50, height=50, image=casa26,command=lambda :self.acao(26))
            self.c26.image=casa26
            self.c26.pack(side=LEFT)

            self.c27= Button(self.tabe, width=50, height=50, image=casab)
            self.c27.image = casab
            self.c27.pack(side=LEFT)

            casa28= self.casasescuras(28)
            self.c28=Button(self.tabe, width=50, height=50, image=casa28,command=lambda :self.acao(28))
            self.c28.image=casa28
            self.c28.pack(side=LEFT)

            self.c29= Button(self.tabe, width=50, height=50, image=casab)
            self.c29.image = casab
            self.c29.pack(side=LEFT)

            casa30= self.casasescuras(30)
            self.c30=Button(self.tabe, width=50, height=50, image=casa30,command=lambda :self.acao(30))
            self.c30.image=casa30
            self.c30.pack(side=LEFT)

            self.c31= Button(self.tabe, width=50, height=50, image=casab)
            self.c31.image = casab
            self.c31.pack(side=LEFT)
            
            self.tabd = Frame()
            self.tabd.pack()

            self.c32= Button(self.tabd, width=50, height=50, image=casab)
            self.c32.image = casab
            self.c32.pack(side=LEFT)

            casa33= self.casasescuras(33)
            self.c33=Button(self.tabd, width=50, height=50, image=casa33,command=lambda :self.acao(33))
            self.c33.image=casa33
            self.c33.pack(side=LEFT)

            self.c34= Button(self.tabd, width=50, height=50, image=casab)
            self.c34.image = casab
            self.c34.pack(side=LEFT)

            casa35= self.casasescuras(35)
            self.c35=Button(self.tabd, width=50, height=50, image=casa35,command=lambda :self.acao(35))
            self.c35.image=casa35
            self.c35.pack(side=LEFT)

            self.c36= Button(self.tabd, width=50, height=50, image=casab)
            self.c36.image = casab
            self.c36.pack(side=LEFT)

            casa37= self.casasescuras(37)
            self.c37=Button(self.tabd, width=50, height=50, image=casa37,command=lambda :self.acao(37))
            self.c37.image=casa37
            self.c37.pack(side=LEFT)

            self.c38= Button(self.tabd, width=50, height=50, image=casab)
            self.c38.image = casab
            self.c38.pack(side=LEFT)

            casa39= self.casasescuras(39)
            self.c39=Button(self.tabd, width=50, height=50, image=casa39,command=lambda :self.acao(39))
            self.c39.image=casa39
            self.c39.pack(side=LEFT)

            self.tabc = Frame()
            self.tabc.pack()

            casa40= self.casasescuras(40)
            self.c40=Button(self.tabc, width=50, height=50, image=casa40,command=lambda :self.acao(40))
            self.c40.image=casa40
            self.c40.pack(side=LEFT)

            self.c41= Button(self.tabc, width=50, height=50, image=casab)
            self.c41.image = casab
            self.c41.pack(side=LEFT)

            casa42= self.casasescuras(42)
            self.c42=Button(self.tabc, width=50, height=50, image=casa42, command=lambda :self.acao(42))
            self.c42.image=casa42
            self.c42.pack(side=LEFT)

            self.c43= Button(self.tabc, width=50, height=50, image=casab)
            self.c43.image = casab
            self.c43.pack(side=LEFT)

            casa44= self.casasescuras(44)
            self.c44=Button(self.tabc, width=50, height=50, image=casa44,command=lambda :self.acao(44))
            self.c44.image=casa44
            self.c44.pack(side=LEFT)

            self.c45= Button(self.tabc, width=50, height=50, image=casab)
            self.c45.image = casab
            self.c45.pack(side=LEFT)

            casa46= self.casasescuras(46)
            self.c46=Button(self.tabc, width=50, height=50, image=casa46,command=lambda :self.acao(46))
            self.c46.image=casa46
            self.c46.pack(side=LEFT)

            self.c47= Button(self.tabc, width=50, height=50, image=casab)
            self.c47.image = casab
            self.c47.pack(side=LEFT)

            self.tabb = Frame()
            self.tabb.pack()

            self.c48= Button(self.tabb, width=50, height=50, image=casab,command=lambda :self.acao(48))
            self.c48.image = casab
            self.c48.pack(side=LEFT)

            casa49= self.casasescuras(49)
            self.c49=Button(self.tabb, width=50, height=50, image=casa49,command=lambda :self.acao(49))
            self.c49.image=casa49
            self.c49.pack(side=LEFT)

            self.c50= Button(self.tabb, width=50, height=50, image=casab)
            self.c50.image = casab
            self.c50.pack(side=LEFT)

            casa51= self.casasescuras(51)
            self.c51=Button(self.tabb, width=50, height=50, image=casa51,command=lambda :self.acao(51))
            self.c51.image=casa51
            self.c51.pack(side=LEFT)

            self.c52= Button(self.tabb, width=50, height=50, image=casab)
            self.c52.image = casab
            self.c52.pack(side=LEFT)

            casa53= self.casasescuras(53)
            self.c53=Button(self.tabb, width=50, height=50, image=casa53,command=lambda :self.acao(53))
            self.c53.image=casa53
            self.c53.pack(side=LEFT)

            self.c54= Button(self.tabb, width=50, height=50, image=casab)
            self.c54.image = casab
            self.c54.pack(side=LEFT)

            casa55= self.casasescuras(55)
            self.c55=Button(self.tabb, width=50, height=50, image=casa55,command=lambda :self.acao(55))
            self.c55.image=casa55
            self.c55.pack(side=LEFT)

            self.taba = Frame()
            self.taba.pack()

            casa56= self.casasescuras(56)
            self.c56=Button(self.taba, width=50, height=50, image=casa56, command=lambda :self.acao(56))
            self.c56.image=casa56
            self.c56.pack(side=LEFT)

            self.c57= Button(self.taba, width=50, height=50, image=casab)
            self.c57.image = casab
            self.c57.pack(side=LEFT)

            casa58= self.casasescuras(58)
            self.c58=Button(self.taba, width=50, height=50, image=casa58,command=lambda :self.acao(58))
            self.c58.image=casa58
            self.c58.pack(side=LEFT)

            self.c59= Button(self.taba, width=50, height=50, image=casab)
            self.c59.image = casab
            self.c59.pack(side=LEFT)

            casa60= self.casasescuras(60)
            self.c60=Button(self.taba, width=50, height=50, image=casa60,command=lambda :self.acao(60))
            self.c60.image=casa60
            self.c60.pack(side=LEFT)

            self.c61= Button(self.taba, width=50, height=50, image=casab)
            self.c61.image = casab
            self.c61.pack(side=LEFT)

            casa62= self.casasescuras(62)
            self.c62=Button(self.taba, width=50, height=50, image=casa62,command=lambda :self.acao(62))
            self.c62.image=casa62
            self.c62.pack(side=LEFT)

            self.c63= Button(self.taba, width=50, height=50, image=casab)
            self.c63.image = casab
            self.c63.pack(side=LEFT)
            return
    def tira_s(self):
        global pecas
        contador=0
        while(contador<64):
            if (pecas[contador]=='S'):
                pecas[contador]='V'
            contador=contador+1
    def verifica_fim(self):
        global contp, contb
        if (contp==0):
            self.apaga_casas()
            uwi = PhotoImage(file='imagens/u_win.gif')
            self.printiw = Label(image=uwi)
            self.printiw.uwi = uwi
            self.printiw.pack()
        if (contb==0):
            self.apaga_casas()
            ulo = PhotoImage(file='imagens/game_over.gif')
            self.printil = Label(image=ulo)
            self.printil.ulo = ulo
            self.printil.pack()
    def acao(self, indice):
            global heuristica
            global situacao, peca_inicial, peca_final, peca_inimiga
            global pecas
            if (situacao==1):
                if (pecas[indice] == 'B'): #SITUACAO1 SEM DAMAS!
                    if (indice==8):
                        self.lateral_esq_normal(indice)
                        return
                    if (indice==24):
                        self.lateral_esq_normal(indice)
                        return
                    if (indice==40):
                        self.lateral_esq_normal(indice)
                        return
                    if (indice==56):
                        self.lateral_esq_normal(indice)
                        return
                    if (indice==58):
                        self.normal2(indice)
                        return
                    if(indice==60):
                        self.normal2(indice)
                        return
                    if(indice==49):
                        self.normal2(indice)
                        return
                    if(indice==62):
                        self.normal2(indice)
                        return
                    if(indice==51):
                        self.normal2(indice)
                        return
                    if(indice==53):
                        self.normal2(indice)
                        return
                    if(indice==42):
                        self.normal2(indice)
                        return
                    if(indice==44):
                        self.normal2(indice)
                        return
                    if(indice==46):
                        self.normal2(indice)
                        return
                    if(indice==33):
                        self.normal2(indice)
                        return
                    if(indice==35):
                        self.normal2(indice)
                        return
                    if(indice==37):
                        self.normal2(indice)
                        return
                    if(indice==39):
                        self.normal2(indice)
                        return
                    if(indice==26):
                        self.normal2(indice)
                        return
                    if(indice==28):
                        self.normal2(indice)
                        return
                    if(indice==30):
                        self.normal2(indice)
                        return
                    if(indice==17):
                        self.normal2(indice)
                        return
                    if(indice==19):
                        self.normal2(indice)
                        return
                    if(indice==21):
                        self.normal2(indice)
                        return
                    if(indice==14):
                        self.normal2(indice)
                        return
                    if(indice==12):
                        self.normal2(indice)
                        return
                    if(indice==10):
                        self.normal2(indice)
                        return
                    if(indice==55):
                        self.lateral_dir_normal(indice)
                        return
                    if(indice==39):
                        self.lateral_dir_normal(indice)
                        return
                    if(indice==23):
                        self.lateral_dir_normal(indice)
                        return
                if(pecas[indice]=='DB'): #SITUACAO1 COM DAMAS!
                    if (indice==56):
                        self.lateral_esq_normal(indice)
                        return
                    if (indice==58):
                        self.normal2(indice)
                        return
                    if(indice==60):
                        self.normal2(indice)
                        return
                    if(indice==62):
                        self.normal2(indice)
                        return
                    if (indice==7): #caso especial
                        if (vercom(7,7)):
                            peca_inicial=indice
                            peca_final=indice+14
                            peca_inimiga=1
                            situacao=2
                            pecas[indice+14]='S'
                            return self.refresh()
                        if(vermov(7,7)):
                            peca_inicial=indice
                            peca_final=indice+7
                            pecas[indice+7]='S'
                            situacao=2
                            return self.refresh()
                        else:
                            return
                    if(indice==5):
                        self.acima_dama(indice)
                        return
                    if(indice==3):
                        self.acima_dama(indice)
                        return
                    if(indice==1):
                        self.acima_dama(indice)
                        return
                    if(indice==40):
                        self.dama_lateral_esq(indice)
                        return
                    if(indice==24):
                        self.dama_lateral_esq(indice)
                        return
                    if(indice==8):
                        self.dama_lateral_esq(indice)
                        return
                    if(indice==55):
                        self.dama_lateral_dir(indice)
                        return
                    if(indice==39):
                        self.dama_lateral_dir(indice)
                        return
                    if(indice==23):
                        self.dama_lateral_dir(indice)
                        return
                    if(indice==49):
                        self.dama_normal4(indice)
                        return
                    if(indice==51):
                        self.dama_normal4(indice)
                        return
                    if(indice==53):
                        self.dama_normal4(indice)
                        return
                    if(indice==46):
                        self.dama_normal4(indice)
                        return
                    if(indice==44):
                        self.dama_normal4(indice)
                        return
                    if(indice==42):
                        self.dama_normal4(indice)
                        return
                    if(indice==33):
                        self.dama_normal4(indice)
                        return
                    if(indice==35):
                        self.dama_normal4(indice)
                        return
                    if(indice==37):
                        self.dama_normal4(indice)
                        return
                    if(indice==30):
                        self.dama_normal4(indice)
                        return
                    if(indice==28):
                        self.dama_normal4(indice)
                        return
                    if(indice==26):
                        self.dama_normal4(indice)
                        return
                    if(indice==17):
                        self.dama_normal4(indice)
                        return
                    if(indice==19):
                        self.dama_normal4(indice)
                        return
                    if(indice==21):
                        self.dama_normal4(indice)
                        return
                    if(indice==14):
                        self.dama_normal4(indice)
                        return
                    if(indice==12):
                        self.dama_normal4(indice)
                        return
                    if(indice==10):
                        self.dama_normal4(indice)
                        return
            if (situacao==2):
                peca_final=indice
                if (pecas[indice]=='S'):
                    if(verificaprox()):
                       peca_inimiga=100
                    else:
                       peca_inimiga=1
                    if (peca_inimiga==100):
                        movepec(peca_inicial, peca_final)

                        self.verifica_fim()
                        heuristica()                     
                        self.verifica_fim()
                        
                        situacao=1
                        self.tira_s()
                        return self.refresh()
                    if (peca_inimiga!=100):
                        if(peca_final-peca_inicial==14):
                            peca_inimiga=(indice-7)
                        if(peca_final-peca_inicial==18):
                            peca_inimiga=(indice-9)
                        if(peca_final-peca_inicial==-14):
                            peca_inimiga=(indice+7)
                        if(peca_final-peca_inicial==-18):
                            peca_inimiga=(indice+9)
                        comepec(peca_inicial, peca_inimiga, peca_final)
                        
                        self.verifica_fim()
                        heuristica()
                        self.verifica_fim()
                        
                        situacao=1
                        peca_inimiga=100
                        contador=0
                        self.tira_s()
                        return self.refresh()
                if(pecas[indice]!='S'):
                    self.tira_s()
                    situacao=1
                    self.refresh()
                    return self.acao(indice)
       
app = Tk()
JanelaPrincipal(app)
app.mainloop()

