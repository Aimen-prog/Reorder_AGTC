import sys
import time
from tkinter import *
from tkinter import ttk
from tkinter import WORD
import tkinter.font as tkFont
import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
from timeit import default_timer

#sequence cible (arrangée avec les sites de restriction)
cible = "ATGCCCAAGCAGGTGGAAGTACGAATGCACGACAGCCATCTCAGCTCATATGCAGAGGAGCCGAAGCACCGACATCTAGGCCTGCGTCTGTGTGACAAGCTGGGGAAGAACCTCCTGCTCACATTGACTGTGTTCGGTGTCATCCTGGGGGCAGTATGTGGAGGGCTTCTTCGCTTGGCATCTCCTCTCCACCCCGATGTGGTCATGTTGATAGCCTTCCCAGGGGATATACTCATGAGGATCCGGATGCTAAAAATGCTCATTCTCCCTCTCATCATCTCCAGCTTAATCACAGGGTTGTCGGGCCTGGATGCTAAAGCCAGTGGGCGCTTAGGCACAAGAGCCATGGTGTATTACATGTCCACAACCATAATTGCCGTCGGTGTTGGGGGTCATCCTGGTCTTGGCTATCCACCCAGGGAACCCCAAACTCAAGAAGCAGCTGGGACCTGGGAAGAAGAATGATGAAGTGTCCAGCCTGGAGGCCTTCCTGGATCTTATTCGAAATCTCTTTCCTGAAAACCTGGTCCAAGCCTGTTTTCAACAGATTCAAACGGTGACCAAGAAAGTCCTGGTGGCTCCTCCATCAGATGAGGACAGCAATGCCACCAATGCTGTCATCTCCTTATTGAACGAGACTGTGACGGAGGCCCCTGAAGAAGTGAAGGTGGTTATCAAGAAGGGCAAGCTTCTGGAGTTCAAGGATGGCATGAATGTCTTAGGTCTGATAGGGTTTTTCATTGCTTTTGGCATCGCCATGGGGAAGATGGGAGAGCAGGCCAAGCTGATGGTGGAGTTCTTCAACATTTTGAATGAGATTGTAATGAAGTTCTAGATAGTGATCATGATCATGTGGTACTCTCCCCTGGGTATTGCCTGCCTAATTTGTGGAAAGATCATTGCAATCAAGGACTTAGAAGTGGTTGCTAGGCAACTGGGGATGTACATGATCACGGTGATTGTGGGCCTCATCATCCATGGGGGCATCTTTCTCCCCTTGATTTACTTTCTAGTCACCAGGAAAAACCCTTTCTCCTTTTTCGCTGGCATTTTCCAAGCTGGATCACTGCCCTGGGTACCGCTTCCAGTGCCGGAACTTTGCCTGTCACTTTCCGTTGCCTGGAAGAAAATCTGGGGATTGATAAGCGCGTGACCAGATTTGTCCTCCCAGTGGGAGCAACCATCAGGACCACATGGACGGCACAGCCCTTTATGAAGCAGTGGCCGCCATCTTTATTGCCCAAATGAACGGTGTTATCCTGGACGGAGGCCAGATTGTGACTGTGAGCCTCACGGCCACGCTGGCGAGCGTCGGTGCGGCCAGTATCCCCAGCGCAGGCCTCGTCACACATGCTCCTCATCCTGACGGCTGTGGGCCTGCCAACGGAGGACATCAGCCTGCTGGTGGCTGTGGACTGGCTGCTGGACAGGATGAGAACTTCAGTCAATGTGGTGGGGGACTCATTTGGGGCTGGGATTGTCTCCCGGGATCACCTCTCCAAGTCTGAGCTGGATACTATTGACTCCCAGCATCGAGTGCATGAAGATATTGAAATGACCAAGACTCAGTCCATTTATGATGTGAAGAACCTTAGGGAAAGCAACTCTAATCAATGTGTCTATGCCGCACACAACTCTGTCATAGTAGATGAGTGCAAGGTAACTCTGGCAGCCAACGGAAAGTCAGCCGACTGTGGTGTTGAAGAAGAACCTTGGAAACGTGAAAAATAA"

#tableau des sites de restriction
motif = ["GGATCC","CATATG","AAGCTT","CCCGGG","TCTAGA","GGTACC"]

#fragments d'ADN coupés aux bons endroit
seq1 = "ATGCCCAAGCAGGTGGAAGTACGAATGCACGACAGCCATCTCAGCTCA"

seq2 = "CGCTTCCAGTGCCGGAACTTTGCCTGTCACTTTCCGTTGCCTGGAAGAAAATCTGGGGATTGATAAGCGCGTGACCAGATTTGTCCTCCCAGTGGGAGCAACCATCAGGACCACATGGACGGCACAGCCCTTTATGAAGCAGTGGCCGCCATCTTTATTGCCCAAATGAACGGTGTTATCCTGGACGGAGGCCAGATTGTGACTGTGAGCCTCACGGCCACGCTGGCGAGCGTCGGTGCGGCCAGTATCCCCAGCGCAGGCCTCGTCACACATGCTCCTCATCCTGACGGCTGTGGGCCTGCCAACGGAGGACATCAGCCTGCTGGTGGCTGTGGACTGGCTGCTGGACAGGATGAGAACTTCAGTCAATGTGGTGGGGGACTCATTTGGGGCTGGGATTGTCTCCC"

seq3 = "TATGCAGAGGAGCCGAAGCACCGACATCTAGGCCTGCGTCTGTGTGACAAGCTGGGGAAGAACCTCCTGCTCACATTGACTGTGTTCGGTGTCATCCTGGGGGCAGTATGTGGAGGGCTTCTTCGCTTGGCATCTCCTCTCCACCCCGATGTGGTCATGTTGATAGCCTTCCCAGGGGATATACTCATGAG"

seq4 = "AGCTTCTGGAGTTCAAGGATGGCATGAATGTCTTAGGTCTGATAGGGTTTTTCATTGCTTTTGGCATCGCCATGGGGAAGATGGGAGAGCAGGCCAAGCTGATGGTGGAGTTCTTCAACATTTTGAATGAGATTGTAATGAAGTT"

seq5 = "GGGATCACCTCTCCAAGTCTGAGCTGGATACTATTGACTCCCAGCATCGAGTGCATGAAGATATTGAAATGACCAAGACTCAGTCCATTTATGATGTGAAGAACCTTAGGGAAAGCAACTCTAATCAATGTGTCTATGCCGCACACAACTCTGTCATAGTAGATGAGTGCAAGGTAACTCTGGCAGCCAACGGAAAGTCAGCCGACTGTGGTGTTGAAGAAGAACCTTGGAAACGTGAAAAATAA"

seq6 = "CTAGATAGTGATCATGATCATGTGGTACTCTCCCCTGGGTATTGCCTGCCTAATTTGTGGAAAGATCATTGCAATCAAGGACTTAGAAGTGGTTGCTAGGCAACTGGGGATGTACATGATCACGGTGATTGTGGGCCTCATCATCCATGGGGGCATCTTTCTCCCCTTGATTTACTTTCTAGTCACCAGGAAAAACCCTTTCTCCTTTTTCGCTGGCATTTTCCAAGCTGGATCACTGCCCTGGGTAC"

seq7 = "GATCCGGATGCTAAAAATGCTCATTCTCCCTCTCATCATCTCCAGCTTAATCACAGGGTTGTCGGGCCTGGATGCTAAAGCCAGTGGGCGCTTAGGCACAAGAGCCATGGTGTATTACATGTCCACAACCATAATTGCCGTCGGTGTTGGGGGTCATCCTGGTCTTGGCTATCCACCCAGGGAACCCCAAACTCAAGAAGCAGCTGGGACCTGGGAAGAAGAATGATGAAGTGTCCAGCCTGGAGGCCTTCCTGGATCTTATTCGAAATCTCTTTCCTGAAAACCTGGTCCAAGCCTGTTTTCAACAGATTCAAACGGTGACCAAGAAAGTCCTGGTGGCTCCTCCATCAGATGAGGACAGCAATGCCACCAATGCTGTCATCTCCTTATTGAACGAGACTGTGACGGAGGCCCCTGAAGAAGTGAAGGTGGTTATCAAGAAGGGCA"

tab = [seq1,seq2,seq3,seq4,seq5,seq6,seq7]

#seq qui remet les fragments dans le bon ordre pour reconstituer "cible"
cible2 = seq1 + seq3+ seq7+ seq4 + seq6 +seq2+ seq5

#vérifie la présence d'un motif dans une seq (on considère que chaque motif est présent qu'une fois donc return true à la première rencontre)
def verifMotif(seq,motif):
    present = False
    for i in range(len(seq)-len(motif)):
        codon = seq[i:i+len(motif)]
        if codon == motif:
            return True
    return False

#ici on considère qu'on ne connaît pas la séquence finale
#si le tableau de motif est vide à la fin alors c'est bon, on a reconstitué la séquence

seqFin = []


def parcours(tab,res):
    if(len(tab)==1 and len(res)==0):
        return True
    for i in range(len(tab)):
        for j in range(len(tab)):
            eq = False
            if(j==i):
                eq=True
            if(eq==False):
                inter = []
                inside = False
                chaine = tab[i] + tab[j]
                for r in res:
                    if(verifMotif(chaine,r)):
                        inside = True
                        res.remove(r)
                if(inside):
                    inter.append(chaine)
                    for k in range(len(tab)):
                        if(k != i and k !=j):
                            inter.append(tab[k])
                    if(parcours(inter,res)):
                        seqFin.append(inter)
                        return(True)
                    else:
                        inter.remove(chaine)
                else:
                    j=j+1
    return(False)

def compareSeq(seqA,seqB):
    inf = min(len(seqA),len(seqB))
    sup = max(len(seqA),len(seqB))
    same = 0
    score = 0
    for i in range (0,inf-2,3):
        if(seqA[i]==seqB[i]):
            same +=1
        if(seqA[i+1]==seqB[i+1]):
            same +=1
        if(seqA[i+2]==seqB[i+2]):
            same +=1
    score = (same/sup)*100
    return score
        
        

def rechercheBdd(seq,base):
    score = -1
    scoreMax = -1
    ind = -1
    for i in base:
        score = (compareSeq(seq,i[1]))
        if(score > scoreMax):
            scoreMax = score
            ind = i
    return i

def CPU():
    time1 = time.time()
    parcours(tab,motif)
    time2 = round(time.time()-time1,7)
    return time2

#cpu = CPU()

def main():
    
    if(parcours(tab,motif)):
        print("La séquence: ", seqFin[0][0])
        #print("Tester si la séquence reconstituée = à la séquence de départ via programme", seqFin[0][0]==cible)
        #print("Tester séquence de départ = seq reconstituée à la main", cible==cible2)
    else:
        print("ERROR")


main()


base = [("Homo Sapiens","GAATTCTTCAGGTAGCTTCCTAGGGTTTCCAAGGCAATACAAGAAGAATTTTGATAGGCAGGAAAATGCATGCTACATACACATATTATTATTCTCTGATTTCCTTTCACATGTAAAAATTGAAAATTGCAAATCTGGTCTTTCAATTAGCAAAAGATTTAT"),
        ("Escherichia coli","AGCTTTTCATTCTGACTGCAATGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTCTCTGACAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAAAAATTACAGAGTACACAACATCCATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGACGCGTACAGGAAACACAGAAAAAAGCCCGCACCTGACAGTGCGGGCTTTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGTACATCAGTGGCAAATGCAGAACGTTTTCTGCGGGTTGCCGATATTCTGGAAAGCAATGCCAGGCAGGGGCAGGTGGCCACCGTCCTCTCTGCCCCCGCCAAAATCACCAACCACCTGGTGGCGATGATTGAAAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAACGTATTTTTGCCGAACTTTTGACGGGACTCGCCGCCGCCCAGCCGGGATTCCCGCTGGCGCAATTGAAAACTTTCGTCGACCAGGAATTTGCCCAAATAAAACATGTCCTGCATGGCATTAGTTTGTTAGGGCAGTGCCCGGATAGCATTAACGCTGCGCTGATTTGCCGTGGCGAGAAAATGTCGATCGCCATTATGGCCGGCGTGTTAGAAGCGCGTGGTCACAACGTTACCGTTATCGATCCGGTCGAAAAACTACTGGCAGTGGGGCATTACCTCGAATCTACCGTCGATATTGCTGAGTCCACCCGCCGTATTGCGGCAAGTCGTATTCCGGCTGATCACATGGTGCTGATGGCAGGCTTCACCGCCGGTAATGAAAAAGGCGAACTGGTGGTACTTGGACGCAACGGTTCCGACTACTCCGCGGCGGTGCTGGCTGCCTGTTTACGCGCCGATTGTTGCGAGATTTGGACGGACGTTGACGGGGTCTATACCTGCGACCCGCGTCAGGTGCCCGATGCGAGGTTGTTGAAGTCGATGTCCTACCAGGAAGCGATGGAGCTTTCCTACTTCGGCGCTAAAGTTCTTCACCCCCGCACCATTACCCCCATCGCCCAGTTCCAGATCCCTTGCCTGATTAAAAATACCGGAAATCCTCAAGCACCAGGTACGCTCATTGGTGCCAGTCGTGATGAAGACGAATTACCGGTCAAGGGCATTTCCAATCTGAATAACATGGCAATGTTCAGCGTTTCCGGCCCGGGGATGAAAGGAATGGTCGGCATGGCGGCGCGCGTCTTTGCCGCGATGTCACGCGCCCGTATTTCCGTGGTGCTGATTACGCAATCATCTTCCGAATACAGTATCAGTTTCTGCGTTCCGCAAAGCGACTGTGTGCGGGCTGAACGGGCAATGCAGGAAGAGTTCTACCTGGAACTGAAAGAAGGCTTACTGGAGCCGCTGGCGGTGACGGAACGGCTGGCCATTATCTCGGTGGTAGGTGATGGTATGCGTACCTTGCGTGGGATCTCGGCGAAATTCTTTGCCGCGCTGGCCCGCGCCAATATCAACATTGTCGCTATTGCTCAGGGATCTTCTGAACGCTCAATCTCTGTCGTGGTAAATAACGATGATGCGACCACTGGCGTGCGCGTTACTCATCAGATGCTGTTCAATACCGATCAGGTTATCGAAGTGTTTGTGATTGGCGTCGGTGGCGTTGGCGGTGCGCTGCTGGAGCAACTGAAGCGTCAACAAAGCTGGCTGAAGAATAAACATATCGACTTACGTGTCTGCGGTGTTGCCAACTCGAAGGCACTGCTCACCAATGTGCATGGCCTAAATCTGGAAAACTGGCAGGAAGAACTGGCGCAAGCCAAAGAGCCGTTTAATCTCGGGCGCTTAATTCGCCTCGTGAAAGAATATCATCTGCTGAACCCGGTCATTGTTGACTGCACCTCCAGCCAGGCAGTGGCGGATCAATATGCCGACTTCCTGCGCGAAGGTTTCCACGTTGTCACGCCGAACAAAAAGGCCAACACCTCGTCGATGGATTACTACCATCTGTTGCGTCATGCGGCGGAAAAATCGCGGCGGAAATTCCTCTATGACACCAACGTTGGGGCTGGATTACCGGTTATTGAAAACCTGCAAAATCTGCTCAATGCTGGTGATGAATTGATGAAGTTCTCCGGCATTCTTTCAGGATCGCTTTCTTATATCTTCGGCAAGTTAGACGAAGGCATGAGTTTCTCCGAGGCGACCACGCTGGCACGGGAAATGGGTTATACCGAACCGGATCCGCGAGATGATCTTTCTGGTATGGATGTGGCGCGTA"),
        ("Canis","ATGCCCAAGCAGGTGGAAGTACGAATGCACGACAGCCATCTCAGCTCAGAGGAGCCGAAGCACCGACATCTAGGCCTGCGTCTGTGTGACAAGCTGGGGAAGAACCTCCTGCTCACATTGACTGTGTTCGGTGTCATCCTGGGGGCAGTATGTGGAGGGCTTCTTCGCTTGGCATCTCCTCTCCACCCCGATGTGGTCATGTTGATAGCCTTCCCAGGGGATATACTCATGAGGATGCTAAAAATGCTCATTCTCCCTCTCATCATCTCCAGCTTAATCACAGGGTTGTCGGGCCTGGATGCTAAAGCCAGTGGGCGCTTAGGCACAAGAGCCATGGTGTATTACATGTCCACAACCATAATTGCCGCGGTGTTGGGGGTCATCCTGGTCTTGGCTATCCACCCAGGGAACCCCAAACTCAAGAAGCAGCTGGGACCTGGGAAGAAGAATGATGAAGTGTCCAGCCTGGAYGCCTTCCTGGATCTTATTCGAAATCTCTTTCCTGAAAACCTGGTCCAAGCCTGTTTTCAACAGATTCAAACGGTGACCAAGAAAGTCCTGGTGGCTCCTCCATCAGATGAGGACAGCAATGCCACCAATGCTGTCATCTCCTTATTGAACGAGACTGTGACGGAGGCCCCTGAAGAAGTGAAGGTGGTTATCAAGAAGGGCCTGGAGTTCAAGGATGGCATGAATGTCTTAGGTCTGATAGGGTTTTTCATTGCTTTTGGCATCGCCATGGGGAAGATGGGAGAGCAGGCCAAGCTGATGGTGGAGTTCTTCAACATTTTGAATGAGATTGTAATGAAGTTAGTGATCATGATCATGTGGTACTCTCCCCTGGGTATTGCCTGCCTAATTTGTGGAAAGATCATTGCAATCAAGGACTTAGAAGTGGTTGCTAGGCAACTGGGGATGTACATGATCACGGTGATTGTGGGCCTCATCATCCATGGGGGCATCTTTCTCCCCTTGATTTACTTTCTAGTCACCAGGAAAAACCCTTTCTCCTTTTTCGCTGGCATTTTCCAAGCTTGGATCACTGCCCTGGGTACCGCTTCCAGTGCCGGAACTTTGCCTGTCACTTTCCGTTGCCTGGAAGAAAATCTGGGGATTGATAAGCGCGTGACCAGATTTGTCCTCCCAGTGGGAGCAACCATCAACATGGACGGCACAGCCCTTTATGAAGCAGTGGCCGCCATCTTTATTGCCCAAATGAACGGTGTTATCCTGGACGGAGGCCAGATTGTGACTGTGAGCCTCACGGCCACGCTGGCGAGCGTCGGTGCGGCCAGTATCCCCAGCGCAGGCCTCGTCACCATGCTCCTCATCCTGACGGCTGTGGGCCTGCCAACGGAGGACATCAGCCTGCTGGTGGCTGTGGACTGGCTGCTGGACAGGATGAGAACTTCAGTCAATGTGGTGGGGGACTCATTTGGGGCTGGGATTGTCTATCACCTCTCCAAGTCTGAGCTGGATACTATTGACTCCCAGCATCGAGTGCATGAAGATATTGAAATGACCAAGACTCAGTCCATTTATGATGTGAAGAACCTTAGGGAAAGCAACTCTAATCAATGTGTCTATGCCGCACACAACTCTGTCATAGTAGATGAGTGCAAGGTAACTCTGGCAGCCAACGGAAAGTCAGCCGACTGTGGTGTTGAAGAAGAACCTTGGAAACGTGAAAAATAA")
        ]


sequence = seqFin[0][0]
#print(rechercheBdd(sequence,base))

match_blast = rechercheBdd(sequence,base)

##création fenêtre principale

window = Tk() #création fenêtre
window.title("L'info c'est bio") #titre de la fenêtre
window.geometry("720x780")
window.minsize(720,780) 
window.maxsize(720,780)
window.configure(bg='lightblue')


##création zone affichage tableau exemple
URL = "https://i.ibb.co/pynqsyM/2.gif"
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
example = ImageTk.PhotoImage(im)

zone_example = Canvas(window, width=690, height=80, bg="lightblue")
zone_example.create_image(1,1,anchor=NW,image=example)
zone_example.place(x=15,y=130)


##création zone affichage tableau enzyme
URL = "https://i.ibb.co/x5xPMzP/3.gif"
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
enzyme = ImageTk.PhotoImage(im)

zone_enzyme = Canvas(window, width = 200, height = 250, bg="lightblue")
zone_enzyme.create_image(1,1,image=enzyme,anchor=NW)
zone_enzyme.place(x=15,y=310)

##création zone affichage tableau séquences
URL = "https://i.ibb.co/qB10sn3/1.gif"
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
tabSeq = ImageTk.PhotoImage(im)

zone_tabSeq = Canvas(window, width = 450, height = 250, bg="lightblue")
zone_tabSeq.create_image(1,1,image=tabSeq,anchor=NW)
zone_tabSeq.place(x=250,y=310)


##définition des polices de caractères utilisées

fontSubTitle = tkFont.Font(family="Segoe Script", size=20, weight="bold", slant="italic")
fontTitle = tkFont.Font(family="Segoe Script", size=30, weight="bold", slant="italic")
fontButton = tkFont.Font(family="Segoe Script", size=15, weight="bold", slant="italic")

##définition des titres
title1 = Label(window, text="Un scientifique maladroit", bg="#D10000",width=720,font=fontTitle)
title1.pack()

subtitle1 = Label(window, text="Une petite coupe ?", bg="#33CC00",width=15,font=fontSubTitle).place(x=15,y=80)
subtitle2 = Label(window, text="Votre mission: Associer les fragments deux à deux pour reformer aux jointures les motifs recherchés", wraplength=700, bg="#33CC00",font=fontSubTitle).place(x=15,y=210)
subtitle3 = Label(window, text="Ordre proposé", bg="#33CC00",width=15,font=fontSubTitle).place(x=15,y=580)

##initialisation des séquences proposées dans le menu déroulant

A = "TCAAGAAGGGCA"
B = "TGTAATGAAGTT"
C = "CATCTCAGCTCA"
D = "AGCTTCTGGAGT"
E = "TATACTCATGAG"
F = "TATGCAGAGGAG"
G = "GATCCGGATGCT"
H = "CTAGATAGTGAT"

#choix menu déroulant
listeSeq = [A,B,C,D,E,F,G,H]
listeChoix = ["A","B","C","D","E","F","G","H"]

#séquence objectif
#but = B+A+D+C+F+E
but = C+F+E+G+A+D+B+H

## fonction callback pour menu déroulant
def callbackMenu1(event):
    select1 = menu1.get()
    return select1

def callbackMenu2(event):
    select2 = menu2.get()
    return select2

def callbackMenu3(event):
    select3 = menu3.get()
    return select3

def callbackMenu4(event):
    select4 = menu4.get()
    return select4

def callbackMenu5(event):
    select5 = menu5.get()
    return select5

def callbackMenu6(event):
    select6 = menu6.get()
    return select6

##définition des menus
y_menu = 635
width_menu = 3

menu1 = ttk.Combobox(window,values = listeChoix,width=width_menu)
menu1.place(x=15, y=y_menu)
menu1.current(2)
menu1.config(state='readonly')
menu1.bind("<<ComboboxSelected>>",callbackMenu1)


menu2 = ttk.Combobox(window,values = listeChoix, width=width_menu)
menu2.place(x=95, y=y_menu)
menu2.current(5)
menu2.config(state='readonly')
menu2.bind("<<ComboboxSelected>>", callbackMenu2)

menu3 = ttk.Combobox(window,values = listeChoix, width=width_menu)
menu3.place(x=175, y=y_menu)
menu3.current(4)
menu3.config(state='readonly')
menu3.bind("<<ComboboxSelected>>", callbackMenu3)

menu4 = ttk.Combobox(window,values = listeChoix, width=width_menu)
menu4.place(x=255, y=y_menu)
menu4.current(6)
menu4.config(state='readonly')
menu4.bind("<<ComboboxSelected>>", callbackMenu4)

menu5 = ttk.Combobox(window,values = listeChoix, width=width_menu)
menu5.place(x=335, y=y_menu)
menu5.current(0)
menu5.config(state='readonly')
menu5.bind("<<ComboboxSelected>>", callbackMenu5)

menu6 = ttk.Combobox(window,values = listeChoix, width=width_menu)
menu6.place(x=415, y=y_menu)
menu6.current(3)
menu6.config(state='readonly')
menu6.bind("<<ComboboxSelected>>", callbackMenu6)

menu7 = ttk.Combobox(window,values = listeChoix, width=width_menu)
menu7.place(x=500, y=y_menu)
menu7.current(1)
menu7.config(state='readonly')
menu7.bind("<<ComboboxSelected>>")

menu8 = ttk.Combobox(window,values = listeChoix, width=width_menu)
menu8.place(x=580, y=y_menu)
menu8.current(7)
menu8.config(state='readonly')
menu8.bind("<<ComboboxSelected>>")


def nextAction():
    
    fenNext = Tk()
    fenNext.title("Next")
    fenNext.geometry("500x600")
    fenNext.minsize(500,600)
    fenNext.maxsize(500,600)
    fenNext.configure(bg="lightblue")
    titleNext = Label(fenNext, text="Comparaison de la séquence à une base de données", bg="#D10000",width=500,font=fontTitle).pack()
    zone_molecule = Label(fenNext, text="Type de molécule", bg="lightgreen",font=fontSubTitle).place(x=15, y=30)
    
    menu_mol = ttk.Combobox(fenNext,values = ["ADN","ARN","Protéine"], width=5)
    menu_mol.place(x=15, y=60)
    menu_mol.current(0)
    menu_mol.config(state='readonly')
    
    zone_espece = Label(fenNext, text="Organismes", bg="lightgreen",font=fontSubTitle).place(x=15, y=150)

    menu_esp = ttk.Combobox(fenNext,values = ["Plantes","Mammifères","Tous"], width=10)
    menu_esp.place(x=15, y=180)
    menu_esp.current(0)
    menu_esp.config(state='readonly')
    def rechercheAction():
        
        choix_mol = menu_mol.get()
        choix_esp = menu_esp.get()
        
        if(choix_mol == "ADN" and choix_esp == "Tous"):
            titleRecherche = Label(fenNext, text="Un match a été trouvé", bg="yellow",font=fontTitle)
            titleRecherche.place(x=200,y=280)
            zone_org = Label(fenNext, text="Organisme: "+match_blast[0], bg="yellow").place(x=15,y=320)
            zone_mol = Label(fenNext, text="Type de molécule: "+ menu_mol.get(), bg="yellow").place(x=15,y=350)
            zone_size = Label(fenNext, text="Taille: "+str(len(match_blast[1]))+" pb", bg="yellow").place(x=15,y=380)
            
            
            message = "Bravo, vous avez réussi à reconstituer la séquence d'ADN et à trouver le coupable...enfin presque !\n La séquence obtenue n'est pas humaine.\nCe nouvel indice va-t-il vous aider à trouver le coupable ?\n"
            zone_msg = Label(fenNext, text=message, bg="pink", wraplength=350).place(x=100,y=440)
        
        else :
            fenRecherche = Tk()
            fenRecherche.title("Recherche")
            fenRecherche.geometry("200x200")
            fenRecherche.minsize(200,200)
            fenRecherche.maxsize(200,200)
            titleRecherche = Label(fenRecherche, text="Aucune base de données ne correspond aux paramètres entrés\nVeuillez réessayer", bg="pink",font=fontTitle, wraplength=150).pack()
    button_recherche = Button(fenNext, text="Lancer la recherche", font=fontButton, relief=RAISED,command=rechercheAction).place(x=200, y=250)


    

##fonctions bouton VERIFIER
def affichBravo():
    fen = Tk()
    fen.title("Bravo") #titre de la fenêtre
    
    fen.geometry("500x500")
    fen.minsize(500,500) #dimensions minimales 
    title = Label(fen, text="Bravo", bg="lightgreen",width=300,height=300,font=fontSubTitle)
    title.pack()
    



def affichFail():
    fen = Tk()
    fen.title("Dommage")
    fen.geometry("500x500")
    fen.configure(bg="#DE2916")
    fen.minsize(500,500)
    fen.maxsize(500,500)
    fontTitle = tkFont.Font(family="Segoe Script", size=30, weight="bold", slant="italic")
    def voirSol():
        sol = but
        zone_ordre = Label(fen, text="La bonne réponse est:\nC-F-E-G-A-D-B-H", bg="white",font=fontSubTitle).place(x=175,y=200)
        #zone_ordre.pack()
        zone_sol = Label(fen, text=sol, bg="white",font=fontSubTitle,wraplength=450).place(x=20,y=400)
    #encore_border = Frame(fen,background="white")
    title = Label(fen,bd=1,relief="solid",text="Essaie encore !",bg="#DE2916",font=fontSubTitle).place(x=200,y=100)
    button_sol = Button(fen, text="Voir Solution", width=10, font=fontButton, relief=RAISED,command=voirSol).place(x=200, y=300)
    #title.pack()

##fonction bouton MORE    
def moreAction():
    fenMore = Tk()
    fenMore.title("More")
    fenMore.geometry("1100x730")
    fenMore.configure(bg="lightblue")
    fenMore.minsize(900,730)
    fenMore.maxsize(1000,730)
    zone_font = tkFont.Font(family="Segoe Script", size=30, weight="bold", slant="italic")
    chaine = "Voici tous les fragments que notre scientifique a obtenu...\nHeureusement que nous savons faire de l'informatique !\nAppuyez sur 'Reconstituer' pour obtenir la séquence"
    zone_txt = Label(fenMore, text=chaine, bg="#D10000",wraplength=550).place(x=85,y=12)
    zone_seq1 = Label(fenMore, text=seq1, borderwidth=1,relief="solid",bg="white",wraplength=550).place(x=65,y=75)
    zone_seq2 = Label(fenMore, text=seq2, borderwidth=1,relief="solid",bg="white",wraplength=550).place(x=15,y=105)
    zone_seq3 = Label(fenMore, text=seq3, borderwidth=1,relief="solid",bg="white",wraplength=550).place(x=15,y=230)
    zone_seq4 = Label(fenMore, text=seq4, borderwidth=1,relief="solid",bg="white",wraplength=550).place(x=15,y=308)
    zone_seq5 = Label(fenMore, text=seq5, borderwidth=1,relief="solid",bg="white",wraplength=550).place(x=15,y=370)
    zone_seq6 = Label(fenMore, text=seq6, borderwidth=1,relief="solid",bg="white",wraplength=550).place(x=15,y=462)
    zone_seq7 = Label(fenMore, text=seq7, borderwidth=1,relief="solid",bg="white",wraplength=550).place(x=15,y=552)
    def reconstituer():
        print("reconstituer")
        zone_reconstituer = Label(fenMore, text=seqFin[0][0], bg="white",wraplength=375).place(x=600,y=20)
        zone_time = Label(fenMore, text=(str(CPU()) + " sec") , bg="yellow").place(x=490,y=50)
    button_Reconstitution = Button(fenMore, text="Reconstituer", width=10, font=fontButton, relief=RAISED,command=reconstituer).place(x=470, y=15)

def SwitchFrag(arg):
    
        if(arg=="A"):
            return(A)
        if(arg=="B"):
            return(B)
        if(arg=="C"):
            return(C)
        if(arg=="D"):
            return(D)
        if(arg=="E"):
            return(E)
        if(arg=="F"):
            return(F)
        if(arg=="G"):
            return(G)
        if(arg=="H"):
            return(H)
      
def verifAction():
    print("VerifAction")
    consensus = ["","","","","","","",""]
    consensus[0] = SwitchFrag(menu1.get())
    consensus[1] = SwitchFrag(menu2.get())
    consensus[2] = SwitchFrag(menu3.get())
    consensus[3] = SwitchFrag(menu4.get())
    consensus[4] = SwitchFrag(menu5.get())
    consensus[5] = SwitchFrag(menu6.get())
    consensus[6] = SwitchFrag(menu7.get())
    consensus[7] = SwitchFrag(menu8.get())

    seqFusion = ""
    for i in consensus:
        seqFusion += i
    if (seqFusion == but):
        affichBravo()
    else:
        affichFail()
    #print(consensus)
    #print(seqFusion)
    

##initialisation des boutons 
button_verif = Button(window,text="Verify",font=fontButton, bd = 5,activebackground= "yellow",width=15,relief='raised',command=verifAction).place(x = 15, y=660)
button_next = Button(window,text="Next",width=10,font=fontButton,relief=RAISED,command=nextAction).place(x = 550, y=660)
button_more = Button(window, text="More", width=10, font=fontButton, relief=RAISED, command=moreAction).place(x=550, y=570)


window.mainloop()
