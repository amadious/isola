from upemtk import * 
from time import *


''' Il y a tout d'abord plusieurs fonctions basiques,
afin de créer le plateau, les pions et les cases noires,
puis les différents modes seront sous forme de programmes tout en bas
Un petit générique précedera le programme principal'''



#------------------------------------------------------------------------   
########################## FONCTIONS ####################################   

#------------------------------------------------------------------------


#création du plateau_______________
def plato():
   L = ['A','B','C','D','E','F']
   C = ['1','2','3','4','5','6']
   dicoPlato= {}
   dP = dicoPlato
    
   l = 0
   for i in range(100, 700, 100):#il y aura un espace vide autour du plateau 
      c= 0 
      for j in range(100, 700, 100) :
         dP[L[l]+C[c]] = rectangle(i, j, 100+i, 100+j,tag="")
         texte(50, 125+(c*100), L[c])
         texte(150+(c*100),50, C[c])
         c+=1 
      l+= 1
        
#etat de la case: vide, prise ou bloqué par un carré      
def etatCase():
   dicoPlato= {}
   dP = dicoPlato


    
   for i in range(100, 700, 100): #lignes
      for j in range(100, 700, 100): #colonnes
         dP[str(i+50)+str(j+50)] = 'Vide'
         # i correspond aux sommets de la case, et  +50 pour arriver au centre de la case
   return dP         
          
plateau = etatCase()       
# il suffira donc de concaténer les coordonnées afin de comparer l'état de la case       
       

       
       
#pion_______________
def dpion1(a, b, limita1, limita2, limitb1, limitb2):
    # les limites permettent de ne pas dépasser les 8 cases autour 
   while True:
       
      
      ev = donne_evenement()
      type_ev = type_evenement(ev)
    
    
      da = 0
      db = 0
      ok = 'pas ok'
      if type_ev == 'Touche':
         if touche(ev) == 'Left':
            da = max(-a+150, -dep,limita2-a ) 
         elif touche(ev) == 'Right':
            da = min(dep, 700-2*taille_p-a,limita1 - a)     
         elif touche(ev) == 'Up':
            db = max(-b+150, -dep, limitb2-b)   
         elif touche(ev) == 'Down':
            db = min(dep,700-2*taille_p-b, limitb1-b)
         
         elif touche(ev) == 'space':
            ok = 'ok'
             
            
        
         a += da
         b += db
         return [a, b,'tag',ok] # on renvoie les coordonnées, le tag et la validation du choix de la case
           
      mise_a_jour()  


      
#pion2______________________________      
def dpion2(j,k, limitj1, limitj2, limitk1, limitk2):
   
   while True:
       
      ev = donne_evenement()
      type_ev = type_evenement(ev)
    
    
      da = 0
      db = 0
      ok2 = 'pas ok'
      if type_ev == 'Touche':
         if touche(ev) == 'q':#z-q-s-d équivalent des flèches
            da = max(-j+150, -dep, limitj2-j) 
         elif touche(ev) == 'd':
            da = min(dep, 700-2*taille_p-j, limitj1-j)     
         elif touche(ev) == 'z':
            db = max(-k+150, -dep, limitk2-k)   
         elif touche(ev) == 's':
            db = min(dep,700-2*taille_p-k, limitk1-k)
         
         elif touche(ev) == 't':# équivalent d'espace
            ok2 = 'ok'
            
        
         j += da
         k += db
         return [j, k, 'tag2', ok2]  # on renvoie les coordonnées, le tag et la validation du choix de la case
           
      mise_a_jour()   
      

#pion3______________________________      
def dpion3(e,f, limite1, limite2, limitf1, limitf2):
   
   while True:
       
      ev = donne_evenement()
      type_ev = type_evenement(ev)
    
    
      de = 0
      df = 0
      ok3 = 'pas ok'
      if type_ev == 'Touche':
         if touche(ev) == 'j':#z-q-s-d équivalent des flèches
            de = max(-e+150, -dep, limite2-e) 
         elif touche(ev) == 'l':
            de = min(dep, 700-2*taille_p-e, limite1-e)     
         elif touche(ev) == 'i':
            df = max(-f+150, -dep, limitf2-f)   
         elif touche(ev) == 'k':
            df = min(dep,700-2*taille_p-f, limitf1-f)
         
         elif touche(ev) == 'p':# équivalent d'espace
            ok3 = 'ok'
            
        
         e += de
         f += df
         return [e, f, 'tag3', ok3]  # on renvoie les coordonnées, le tag et la validation du choix de la case
           
      mise_a_jour()   
      
      
      
      
      
      
      
      
      
      
      

#ordinateur Z_______________________
def dpionZ(c, d):
   #ordinateur respectant les règles 
   placeZ = verifPLace(c,d)
   s,w = placeZ[4], placeZ[5]
   return [s,w,'tagZ']    
   
      
##############################           
def dpion0(a,b):
    #ordinateur ne respectant pas les règles, il suit le joueur partout !
    place0 = verifPLace(a,b)
    f,g = place0[4], place0[5]
    return [f,g, 'tagZ']
          



# case noir_______________________  
def case_noir(etatCase):
   x, y, taille = 100, 300, 100
   dep = 100
   case_noir = None 
   #deplacement case_noir
   while True :
       if case_noir:
          efface(case_noir)
     
       case_noir = rectangle(x, y, x + taille, y + taille, remplissage='black')

       ev = donne_evenement()
       type_ev = type_evenement(ev)
 
       dx = 0
       dy = 0
       if type_ev == 'Touche':
          name_t = touche(ev) 
          if name_t == 'Left':
              dx = max(-dep, -x+100)# '+100' afin que la case ne dépasse pas le plateau
          elif name_t == 'Right':
              dx = min(dep, 800-x-taille*2) # même chose
          elif name_t == 'Up':
              dy = max(-dep, -y+100)
          elif name_t == 'Down':
              dy = min(dep, 800-y-taille*2)    
          x += dx
          y += dy
 
          if name_t == 'space':
              if etatCase[str(x+50) + str(y+50)] == 'Vide': 
                  # si la case n'est pas vide ça ne marche pas
                  return [x,y, taille] 
                  break 
       
          
          
          
    
       mise_a_jour()          

       
       

#case_grise________________________
def case_grise(etatCase):
   x, y, taille = 600, 400, 100
   dep = 100
   case_noir = None 
   #deplacement case_noir
   while True :
       if case_noir:
          efface(case_noir)
     
       case_noir = rectangle(x, y, x + taille, y + taille, remplissage='grey')

       ev = donne_evenement()
       type_ev = type_evenement(ev)
 
       dx = 0
       dy = 0
       if type_ev == 'Touche':
          name_t = touche(ev) 
          if name_t == 'q':
              dx = max(-dep, -x+100)# '+100' afin que la case ne dépasse pas le plateau
          elif name_t == 'd':
              dx = min(dep, 800-x-taille*2) # même chose
          elif name_t == 'z':
              dy = max(-dep, -y+100)
          elif name_t == 's':
              dy = min(dep, 800-y-taille*2)    
          x += dx
          y += dy
 
          if name_t == 't':
              if etatCase[str(x+50) + str(y+50)] == 'Vide':                
                 # si la case n'est pas vide ça ne marche pas 
                 return [x,y, taille]
                 break 
       
              
       mise_a_jour() 


# case violette_______________________  
def case_violette(etatCase):
   x, y, taille = 100, 300, 100
   dep = 100
   case_noir = None 
   #deplacement case_noir
   while True :
       if case_noir:
          efface(case_noir)
     
       case_noir = rectangle(x, y, x + taille, y + taille, remplissage='purple')

       ev = donne_evenement()
       type_ev = type_evenement(ev)
 
       dx = 0
       dy = 0
       if type_ev == 'Touche':
          name_t = touche(ev) 
          if name_t == 'j':
              dx = max(-dep, -x+100)# '+100' afin que la case ne dépasse pas le plateau
          elif name_t == 'l':
              dx = min(dep, 800-x-taille*2) # même chose
          elif name_t == 'i':
              dy = max(-dep, -y+100)
          elif name_t == 'k':
              dy = min(dep, 800-y-taille*2)    
          x += dx
          y += dy
 
          if name_t == 'p':
              if etatCase[str(x+50) + str(y+50)] == 'Vide': 
                  # si la case n'est pas vide ça ne marche pas
                  return [x,y, taille] 
                  break 
       
          
          
          
    
       mise_a_jour()          


       
#case_marron________________________
def case_marron(a, b, etatCase):
   riposte = verifPLace(a,b) # fonction expliquée juste en dessous
   q, p, taille = riposte[4], riposte[5], 100
   return [q-50, p-50, taille] 
   
                       
                       
                       

         
############################################################
#verificateurs de fin de parties................................  
"""fonction IMPORTANTE, elle sert à avoir beaucoup d'informations sur une case
on peut donc savoir, si la partie est finie ou aider l'ordinateur à détecter son adversaire et sortir de ses pièges"""  
# Attention j'ai mis 2 MAJUSCULES à cette fonction accidentellement
def verifPLace(a,b):       
    comptBloc = 0 # la case où il y a le pion est prise !
    comptPrise = 0
    comptVide = 0
    m,n =0, 0
    reponse = False
    if  150 < a < 650 and 150 < b < 650:
        for q in range(a-100,a+200, 100):
           for p in range(b-100, b+200, 100):
               if plateau[str(q)+str(p)] == 'Bloc':
                   comptBloc += 1
               elif plateau[str(q)+str(p)] == 'Prise':
                   comptPrise += 1
               elif plateau[str(q)+str(p)] == 'Vide':
                   m, n = q, p # On stocke le dernière case vide détectée
                   comptVide += 1 
        
        if (comptBloc + comptPrise) == 9: 
           reponse = True
        
       #...à gauche ou à droite...               
    elif  (a == 150 or a == 650) and 150 < b < 650:
        if a == 150:
            for q in range(a,a+200, 100):
                for p in range(b-100, b+200, 100):
                   if plateau[str(q)+str(p)] == 'Bloc':
                       comptBloc += 1
                   elif plateau[str(q)+str(p)] == 'Prise':
                       comptPrise += 1
                   elif plateau[str(q)+str(p)] == 'Vide':
                       m, n = q, p # On stocke le dernière case vide détectée
                       comptVide += 1   
       
        elif a == 650:
            for q in range(a-100,a+100, 100):
                for p in range(b-100, b+200, 100):
                   if plateau[str(q)+str(p)] == 'Bloc':
                         comptBloc += 1
                   elif plateau[str(q)+str(p)] == 'Prise':
                         comptPrise += 1
                   elif plateau[str(q)+str(p)] == 'Vide':
                         m = q
                         n = p
                         # On stocke le dernière case vide détectée
                         comptVide += 1
                         
        if (comptBloc + comptPrise) == 6: 
           reponse = True
        
                         
                         
#-------    #en haut ou en bas...------------------------------------------
    elif  (b == 150 or b == 650) and 150 < a < 650:
        if b == 150:
            for q in range(a-100,a+200, 100):
                for p in range(b, b+200, 100):
                   if plateau[str(q)+str(p)] == 'Bloc':
                       comptBloc += 1
                   elif plateau[str(q)+str(p)] == 'Prise':
                       comptPrise += 1
                   elif plateau[str(q)+str(p)] == 'Vide':
                       m, n = q, p # On stocke le dernière case vide détectée
                       comptVide += 1
                            
        elif b == 650:
            for q in range(a-100,a+200, 100):
                for p in range(b-100, b+100, 100):
                    if plateau[str(q)+str(p)] == 'Bloc':
                       comptBloc += 1
                    elif plateau[str(q)+str(p)] == 'Prise':
                       comptPrise += 1
                    elif plateau[str(q)+str(p)] == 'Vide':
                        m, n = q, p # On stocke le dernière case vide détectée
                        comptVide += 1
        
        if (comptBloc + comptPrise) == 6: 
           reponse = True
                       
                       
#----------... ou dans les coins !------------------------------------------------
    elif  (a == 150 or a == 650) and (b == 150 or b == 650):
         if a == 150 and b == 150:
            for q in range(a, a+200, 100):
                for p in range(b, b+200, 100):
                   if plateau[str(q)+str(p)] == 'Bloc':
                       comptBloc += 1
                   elif plateau[str(q)+str(p)] == 'Prise':
                       comptPrise += 1
                   elif plateau[str(q)+str(p)] == 'Vide':
                       m, n = q, p # On stocke le dernière case vide détectée
                       comptVide += 1
                    
 
         elif a == 150 and b == 650:
             for q in range(a,a+200, 100):
                for p in range(b-100, b+100, 100):
                   if plateau[str(q)+str(p)] == 'Bloc':
                       comptBloc += 1
                   elif plateau[str(q)+str(p)] == 'Prise':
                       comptPrise += 1
                   elif plateau[str(q)+str(p)] == 'Vide':
                       m, n = q, p # On stocke le dernière case vide détectée
                       comptVide += 1
                                
 
         elif a == 650 and b == 150:
             for q in range(a-100,a+100, 100):
                for p in range(b, b+200, 100):
                   if plateau[str(q)+str(p)] == 'Bloc':
                       comptBloc += 1
                   elif plateau[str(q)+str(p)] == 'Prise':
                       comptPrise += 1
                   elif plateau[str(q)+str(p)] == 'Vide':
                       m, n = q, p # On stocke le dernière case vide détectée
                       comptVide += 1
                               
  
         elif a == 650 and b == 650:    
             for q in range(a-100,a+100, 100):
                for p in range(b-100, b+100, 100):
                   if plateau[str(q)+str(p)] == 'Bloc':
                       comptBloc += 1
                   elif plateau[str(q)+str(p)] == 'Prise':
                       comptPrise += 1
                   elif plateau[str(q)+str(p)] == 'Vide':
                       m, n = q, p # On stocke le dernière case vide détectée
                       comptVide += 1
        
         if (comptBloc + comptPrise) == 4: 
            reponse = True
         
    return [comptBloc, comptPrise, comptVide, reponse, m, n]                      
                
                
               
               

                    
               
               
           
       
       
def veriFinPartie(j,k):
    #print(verifPLace(j,k))    
    if verifPLace(j,k)[3]:
        i = 900
        while i > 30:
            sleep(0.001)
            efface('isola')
            texte(600, i, "ISOLA! Isolé ! ", taille = 36,
              police = 'Impact', couleur = 'red', ancrage= 'center', tag = 'isola')
            i -= 3
            mise_a_jour()
            
        texte(400,60 , 'Une autre partie ? \n Oui W  Menu X Quitter C',
              taille = 15, couleur = 'black', police = 'Impact', ancrage = 'se')
        
        while True:
            ev4 = donne_evenement()
            type_ev4 = type_evenement(ev4)
            reponse = 0
            if type_ev4 == 'Touche':
                if touche(ev4) == 'w':
                    return 'wi'
                    
                elif touche(ev4) == 'x':
                    return 'xi'
                elif touche(ev4) == 'c':
                    return 'ci'
            
            
            mise_a_jour()
    
       
       
       
       
       
       
       
       
##################################"---------------------------------------------------------------
#Générique et introduction


#------------------------------------------------------
def muqad():
   
    
   
   i = 0
   while i < 2:
       sleep(0.25)
       rectangle(100+2*i*100, 100, 200+2*i*100, 200,remplissage = 'yellow')
    
       rectangle(100+2*i*100,300, 200+2*i*100,400, remplissage = 'black')
       i += 1
       mise_a_jour()
   
   texte(150,150, 'Isola', ancrage = 'center', police = 'Magneto',
             couleur = 'blue')
   texte(350,150, 'Isola', ancrage = 'center', police = 'Magneto',
             couleur = 'blue')
   texte(150,350, 'Isola', ancrage = 'center', police = 'Magneto',
             couleur = 'white')
   texte(350,350, 'Isola', ancrage = 'center', police = 'Magneto',
             couleur = 'white')
       
    
   x = 0 
   y = 0

   while x <= 700 :
       sleep(0.002)
       cercle(x, 50, 50, couleur = 'yellow')
       cercle(x, 250, 50, couleur = 'blue')
       cercle(x, 450, 50, couleur = 'red')
       
       
       x += 10
       mise_a_jour()

   while y <= 700:
       sleep(0.002)
       cercle(50, y, 50)
       cercle(250, y, 50)
       cercle(450, y, 50)
       y += 10
       mise_a_jour()
   
      
def introTouches():
    
   texte(400, 100, 'Touches', taille = 36, ancrage = 'center', police = 'Impact')

   texte(200, 200, 'Joueur 1 : les flèches / "espace" pour valider', taille = 15, police = 'Impact')
   texte(200, 300, 'Joueur 2 : Z-Q-S-D / "T" pour valider', taille = 15, police = 'Impact')
   texte(200, 400, 'Joueur 3 : I-J-K-L / "P" pour valider', taille = 15, police = 'Impact')
   
   texte(400, 600, 'Cliquez puis...\n Appuyez sur une touche', ancrage = 's', couleur = 'red',
      police = 'Algerian', taille = 25, tag = 'intro')

   attente_touche()
   efface_tout()
   ferme_fenetre()
    




#intro----------------------------------
def intro():
   t = 0
   while t <= 150:
      sleep(0.01)
      efface('titre')
      cercle(400, 400, t*4, tag = 'titre', remplissage = 'lightgreen' )
      texte(400, 400, 'Isola', ancrage = 'center', couleur = 'yellow',
            police = 'Impact', taille = t, tag = 'titre')
      t+= 1
      mise_a_jour()
   texte(400, 600, 'Cliquez puis... \n Appuyez sur une touche', ancrage = 's', couleur = 'red',
            police = 'Algerian', taille = 25, tag = 'intro')
   attente_touche() 
   efface('intro')

   

#menu___________________________________________________   

def menu():    
    j = 0
    while j < 400:
        sleep(0.01)
        efface('menu')
        cercle(j,j ,j ,remplissage = 'black', tag = 'menu')
        j += 3
        mise_a_jour()
        
        
    texte(400, 100, 'Menu', ancrage = 'center', taille = 72,
          tag = 'menu', police = 'Impact', couleur = 'white' )
    
    
    texte(400, 430, 'Mode multijoueurs' , ancrage = 'center',
          tag = 'menu', police = 'Impact', couleur = 'white',taille = 35)    
    texte(300, 500, '2 Joueurs W  \n\n Attrappez-le X \n\n 3 Joueurs ! C ',
          tag = 'menu', police = 'Impact',
          couleur = 'white',taille = 14)
    cercle(200, 520, 25, remplissage = 'red',tag = 'menu')
    cercle(200, 560, 15, remplissage = 'yellow',tag = 'menu')
    cercle(200, 600, 25, remplissage = 'green',tag = 'menu')
    
    #cercle(200, 375, 20, remplissage = 'white', tag = 'menu')
    
    
    
    
    
    
    
    texte(400, 225, 'Mode Solo', ancrage = 'center',
          tag = 'menu', police = 'Impact', couleur = 'white',taille = 35)
    texte(400, 325, 'Niveau 1 : Affronte-moi ! Q \n\n Niveau 2: Attrappe-moi ! S \n\n Niveau 3: Fuis ! D',
          ancrage = 'center', tag = 'menu', police = 'Impact',
          couleur = 'white',taille = 14)
    cercle(200, 275, 25, remplissage = 'orange',tag = 'menu')
    cercle(200, 320, 15, remplissage = 'yellow', tag = 'menu')
    cercle(200, 375, 25, remplissage = 'grey',tag = 'menu')
    cercle(200, 375, 20, remplissage = 'white', tag = 'menu')
    
    while True: 
        ev5 = donne_evenement()
        type_ev5 = type_evenement(ev5)
        if type_ev5 == 'Touche':
            i = 0
            
  ############     ###### mode Solo #############           
            if touche(ev5) == 'q':
                efface('menu')
                while i < 25:
                    sleep(0.1)
                    efface('choix')
                    texte(400, 400, 'Mode ordinateur !',taille = 2*i, ancrage = 'center', tag = 'choix', police = 'Impact')
                    texte(400, 600, 'Impeccable et bon joueur',taille = i, ancrage = 'center', tag = 'choix', police = 'Impact')
                    
                    i += 1
                    mise_a_jour()
                return ['ordinateur','1']

            
            elif touche(ev5) == 's':
                efface('menu')
                while i < 25:
                    sleep(0.1)
                    efface('choix')
                    texte(400, 400, 'Mode ordinateur !',taille = 2*i, ancrage = 'center', tag = 'choix', police = 'Impact')
                    texte(400, 600, 'Insupportable et sprinteur',taille = i, ancrage = 'center', tag = 'choix', police = 'Impact')
                    
                    i += 1
                    mise_a_jour()
                return ['ordinateur','2']  
                
            
            elif touche(ev5) == 'd':
                efface('menu')
                while i < 25:
                    sleep(0.1)
                    efface('choix')
                    texte(400, 400, 'Mode ordinateur !',taille = 2*i, ancrage = 'center', tag = 'choix', police = 'Impact')
                    texte(400, 600, 'Imbattable et tricheur',taille = i, ancrage = 'center', tag = 'choix', police = 'Impact')
                    
                    i += 1
                    mise_a_jour()
                return ['ordinateur','3']
            
                
  #########         # mode multijoueurs------------------------     
            elif touche(ev5) == 'w':
                efface('menu')
                while i < 25:
                    sleep(0.2)
                    efface('choix')
                    texte(400, 400, 'Mode multijoueurs!',taille = 2*i, ancrage = 'center', tag = 'choix', police = 'Impact')
                    texte(400, 600, 'Bon duel !',taille = i, ancrage = 'center', tag = 'choix', police = 'Impact')
                    i += 1
                    mise_a_jour()
                return ['multijoueurs','2']
            
            elif touche(ev5) == 'x':
                efface('menu')
                while i < 25:
                    sleep(0.2)
                    efface('choix')
                    texte(400, 400, 'Mode multijoueurs!',taille = 2*i, ancrage = 'center', tag = 'choix', police = 'Impact')
                    texte(400, 600, "Qui l'attrappera en premier ? ",taille = i, ancrage = 'center', tag = 'choix', police = 'Impact')
                    
                    
                    i += 1
                    mise_a_jour()
                return ['multijoueurs','0']    
                           
                
            elif touche(ev5) == 'c':
                efface('menu')
                while i < 25:
                    sleep(0.2)
                    efface('choix')
                    texte(400, 400, 'Mode multijoueurs!',taille = 2*i, ancrage = 'center', tag = 'choix', police = 'Impact')
                    texte(400, 600, 'Serrez vous !',taille = i, ancrage = 'center', tag = 'choix', police = 'Impact')
                    
                    
                    i += 1
                    mise_a_jour()
                return ['multijoueurs','3']    
                
        mise_a_jour()   




#------------------------------------------------------------------------   


########################## PROGRAMME####################################   


#------------------------------------------------------------------------
        
cree_fenetre(500, 500)
muqad() 
attente_clic()
ferme_fenetre()

cree_fenetre(800,800)   
introTouches()       
        
        
        
        
        
   
   
cree_fenetre(800, 800)


#---------------------------------------------------------------      



##########################menu
while True:
    intro()
    choix = menu()
    
##########################jeu_________________________________________________________________

           

##############    #################   mode multijoueurs   ############################"
           
  #début-------------------------------------------
    if choix[0] == 'multijoueurs':
        efface('choix')
        
        if choix[1] == '2':
            while True:
    
        ############" 2 joueurs  ################"
                plato()
                
                # place initiales
                
                
                
                #mode 2 joueurs---------------------------------
                
                
                a, b, taille_p = 250, 250, 25       
                dep = 100
                
                j, k, taille_p = 550, 550, 25        
                dep = 100
                
                 
                while True:
                    #pions au debut de la partie
                    
                    cercle(a, b, taille_p, remplissage = 'blue', tag = 'tagDebut')
                    cercle(j, k, taille_p, remplissage = 'red', tag = 'tagDebut2')
                    #cercle(c, d, taille_p, remplissage = 'orange', tag = 'tagDebutZ')
                    
                    
                    limiteA1 = a + 100 #limite afin que le pion n'ait que 8 possibilités
                    limiteA2 = a - 100 # joueur 1
                    
                    limiteB1 = b + 100
                    limiteB2 = b - 100
                    
                    
                    limiteJ1 = j + 100 #limite afin que le pion n'ait que 8 possibilités
                    limiteJ2 = j - 100 #joueur 2
                    
                    limiteK1 = k + 100
                    limiteK2 = k - 100
                    
                    plateau[str(a)+str(b)] = 'Prise'
                    plateau[str(j)+str(k)] = 'Prise'
                    
                    
                    
                    
                ################vérifcation de possibilités de sorties pour le joueur 1          
                    over = veriFinPartie(a,b)    
                    if over == 'wi':
                        rep = 'try'
                        efface_tout()
                        plateau = etatCase()
                        break
                    elif over == 'xi':
                        rep = 'menu'
                        efface_tout()
                        plateau = etatCase()
                        break
                    elif over == 'ci':
                        rep = 'quit'
                        efface_tout()
                        plateau = etatCase()
                        break
                    
                    plateau[str(a)+str(b)] = 'Vide'
                           
                ##################################
                #joueur1
                
                    while True:    
                        
                        efface('tag')
                        placeP = dpion1(a,b, limiteA1, limiteA2, limiteB1, limiteB2)
                        a, b, tag = placeP[0], placeP[1], placeP[2]  
                        pion1 = cercle(a,b, taille_p, remplissage = 'blue', tag = tag)
                        efface('traces')
                        if placeP[3] == 'ok':
                            if plateau[str(a)+str(b)] == 'Vide':
                                # si la case n'est pas vide ça ne marche pas
                                efface('tagDebut')
                                plateau[str(a)+str(b)] = 'Prise'
                                break
                        else:
                            cercle(a,b, taille_p, couleur = 'blue', tag = 'traces')
                            continue
                        
                    Cnr = case_noir(plateau)     
                    x, y, taille = Cnr[0], Cnr[1], Cnr[2]
                    rectangle(x, y, x + taille, y + taille, remplissage = 'black')
                    plateau[str(x+50)+str(y+50)] = 'Bloc'
                    
                
                    
                ################vérifcation de possibilités de sorties pour le joueur 2          
                    over = veriFinPartie(j,k)    
                    if over == 'wi':
                        rep = 'try'
                        efface_tout()
                        plateau = etatCase()
                        break
                    elif over == 'xi':
                        rep = 'menu'
                        efface_tout()
                        plateau = etatCase()
                        break
                    elif over == 'ci':
                        rep = 'quit'
                        efface_tout()
                        plateau = etatCase()
                        break      
                            
                #####################----------------------------------------------
                #joueur 2    
                    
                    plateau[str(j)+str(k)] = 'Vide'
                    
                    #plateau[str(c)+str(d)] = 'Vide'
                    
                    while True:
                        efface('tag2')
                        placeP2 = dpion2(j,k, limiteJ1, limiteJ2, limiteK1, limiteK2)
                        j, k, tag2 = placeP2[0], placeP2[1], placeP2[2]  
                        pion2 = cercle(j, k, taille_p, remplissage = 'red', tag = tag2)  
                        efface('traces2')
                        if placeP2[3] == 'ok':
                            if plateau[str(j)+str(k)] == 'Vide':
                               # si la case n'est pas vide ça ne marche pas
                               efface('tagDebut2')
                               plateau[str(j)+str(k)] = 'Prise'
                               break
                           
                        else:
                            cercle(j,k, taille_p, couleur = 'red', tag = 'traces2')
                            continue
                
                        
                    Cnr2 = case_grise(plateau)
                    x2, y2, taille2 = Cnr2[0], Cnr2[1], Cnr2[2]
                    rectangle(x2, y2, x2 + taille2, y2 + taille2, remplissage = 'grey')
                    plateau[str(x2+50)+str(y2+50)] = 'Bloc'
                            
                    
                            
                    mise_a_jour        
                    
                if rep == 'menu':
                    break
                elif rep == 'quit':
                    ferme_fenetre()
                    
                mise_a_jour()
                
        
                
                
        elif choix[1] == '0':
            while True:
    
        ######### mode 2 joueurs contre ordi #############""
                plato()
                
                # place initiales
                
                
                
                #mode 2 joueurs attrappez-le !---------------------------------
                
                
                a, b, taille_p = 250, 250, 25       
                dep = 100
                
                j, k, taille_p = 250, 550, 25        
                dep = 100
                
                c, d, taille_p = 550, 550, 25        
                
                
                while True:
                    #pions au debut de la partie
                    
                    cercle(a, b, taille_p, remplissage = 'blue', tag = 'tagDebut')
                    cercle(j, k, taille_p, remplissage = 'red', tag = 'tagDebut2')
                    cercle(c, d, taille_p, remplissage = 'yellow', tag = 'tagDebutZ')
                    cercle(c, d, 20, remplissage = 'white', tag = 'tagDebutZ')
                    
                    
                    limiteA1 = a + 100 #limite afin que le pion n'ait que 8 possibilités
                    limiteA2 = a - 100 # joueur 1
                    
                    limiteB1 = b + 100
                    limiteB2 = b - 100
                    
                    
                    limiteJ1 = j + 100 #limite afin que le pion n'ait que 8 possibilités
                    limiteJ2 = j - 100 #joueur 2
                    
                    limiteK1 = k + 100
                    limiteK2 = k - 100
                    
                    plateau[str(a)+str(b)] = 'Prise'
                    plateau[str(j)+str(k)] = 'Prise'
                    
                    
                #joueur 1    
                    
                ################vérifcation de possibilités de sorties pour le joueur 2          
                    
                    
                    plateau[str(a)+str(b)] = 'Vide'
                           
                ##################################
                #joueur 1
                
                    while True:    
                        
                        efface('tag')
                        placeP = dpion1(a,b, limiteA1, limiteA2, limiteB1, limiteB2)
                        a, b, tag = placeP[0], placeP[1], placeP[2]  
                        pion1 = cercle(a,b, taille_p, remplissage = 'blue', tag = tag)
                        efface('traces')
                        if placeP[3] == 'ok':
                            if plateau[str(a)+str(b)] == 'Vide':
                                # si la case n'est pas vide ça ne marche pas
                                efface('tagDebut')
                                plateau[str(a)+str(b)] = 'Prise'
                                break
                        else:
                            cercle(a,b, taille_p, couleur = 'blue', tag = 'traces')
                            continue
                        
                    Cnr = case_noir(plateau)     
                    x, y, taille = Cnr[0], Cnr[1], Cnr[2]
                    rectangle(x, y, x + taille, y + taille, remplissage = 'black')
                    plateau[str(x+50)+str(y+50)] = 'Bloc'
                    
                ################vérifcation de possibilités de sorties pour l'ordi #######""          
                    
                    over = veriFinPartie(c,d)
                    if over == 'wi' or over == 'xi' or over == 'ci':     
                        i = 0
                        while i < 50:
                            sleep(0.1)
                            efface('resultat')
                            texte(400,400, 'CONGRATULATIONS joueur 1 !', taille = i, tag = 'resultat',
                                  police = 'Impact', couleur = 'green', ancrage = 'center' )
                            i += 1
                            mise_a_jour()
                        if over == 'wi':
                            rep = 'try'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'xi':
                            rep = 'menu'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'ci':
                            rep = 'quit'
                            efface_tout()
                            plateau = etatCase()
                            break
                                    #####################----------------------------------------------
                #ordi 2_______________________________________    
                    
                    f,g = c,d
                    """ on stocke les valeurs avant de les changer 
                    car sinon l'ordinateur resterait sur place"""
                    
                    #######################################      
                    #dpionZ
                    
                    
                    efface('tagZ')
                    placePZ = dpionZ(x+50,y+50) # il se placera selon le carré noir
                    print(placePZ)
                    c, d, tag = placePZ[0], placePZ[1], placePZ[2]  
                    pion1 = cercle(c,d, 25, remplissage = 'yellow', tag = tag)
                    cercle(c, d, 20, remplissage = 'white', tag = tag)
                    efface('tagDebutZ')
                    plateau[str(c)+str(d)] = 'Prise'
                    plateau[str(f)+str(g)] = 'Vide'
                    
                #####################----------------------------------------------
                #joueur 2    
                    
                    plateau[str(j)+str(k)] = 'Vide'
                    
                    #plateau[str(c)+str(d)] = 'Vide'
                    
                    while True:
                        efface('tag2')
                        placeP2 = dpion2(j,k, limiteJ1, limiteJ2, limiteK1, limiteK2)
                        j, k, tag2 = placeP2[0], placeP2[1], placeP2[2]  
                        pion2 = cercle(j, k, taille_p, remplissage = 'red', tag = tag2)  
                        efface('traces2')
                        if placeP2[3] == 'ok':
                            if plateau[str(j)+str(k)] == 'Vide':
                               # si la case n'est pas vide ça ne marche pas
                               efface('tagDebut2')
                               plateau[str(j)+str(k)] = 'Prise'
                               break
                           
                        else:
                            cercle(j,k, taille_p, couleur = 'red', tag = 'traces2')
                            continue
                
                        
                    Cnr2 = case_grise(plateau)
                    x2, y2, taille2 = Cnr2[0], Cnr2[1], Cnr2[2]
                    rectangle(x2, y2, x2 + taille2, y2 + taille2, remplissage = 'grey')
                    plateau[str(x2+50)+str(y2+50)] = 'Bloc'
                            
  ##############     vérification de sortie pour l'ordi      #################                  
                    over = veriFinPartie(c,d)
                    if over == 'wi' or over == 'xi' or over == 'ci':     
                        i = 0
                        while i < 50:
                            sleep(0.1)
                            efface('resultat')
                            texte(400,400, 'CONGRATULATIONS joueur 2 !', taille = i, tag = 'resultat',
                                  police = 'Impact', couleur = 'green', ancrage = 'center' )
                            i += 1
                            mise_a_jour()
                        if over == 'wi':
                            rep = 'try'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'xi':
                            rep = 'menu'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'ci':
                            rep = 'quit'
                            efface_tout()
                            plateau = etatCase()
                            break
                                    #####################----------------------------------------------
                #ordi 2    
                    
                    f,g = c,d
                    """ on stocke les valeurs avant de les changer 
                    car sinon l'ordinateur resterait sur place"""
                    
                    #######################################      
                    #dpionZ
                    
                    
                    efface('tagZ')
                    placePZ = dpionZ(x2+50,y2+50) # il se placera selon le carré gris
                    print(placePZ)
                    c, d, tag = placePZ[0], placePZ[1], placePZ[2]  
                    pion1 = cercle(c,d, 25, remplissage = 'yellow', tag = tag)
                    cercle(c, d, 20, remplissage = 'white', tag = tag)
                    efface('tagDebutZ')
                    plateau[str(c)+str(d)] = 'Prise'
                    plateau[str(f)+str(g)] = 'Vide'
                            
                            
                            
                            
                    mise_a_jour        
                    
                if rep == 'menu':
                    break
                elif rep == 'quit':
                    ferme_fenetre()
                    
                mise_a_jour()
                
            
                
        #######################################"    
        ######################  mode 3 joueurs   ###############"
        elif choix[1] == '3': 
            while True:
        
            
                plato()
                
                # place initiales
                
                
                
                #mode 2 joueurs---------------------------------
                
                
                a, b, taille_p = 150, 150, 25       
                dep = 100
                
                j, k, taille_p = 350, 350, 25        
                dep = 100
                
                e, f, taille_p = 550, 550, 25
                
                # dès que 2 vaudront True, c'est qu'il ne reste qu'un seul pion libre, qui aura gagné
                bloquee1 = False
                bloquee2 = False
                bloquee3 = False
                    
                while True:
                    #pions au debut de la partie
                    
                    cercle(a, b, taille_p, remplissage = 'blue', tag = 'tagDebut')
                    cercle(j, k, taille_p, remplissage = 'red', tag = 'tagDebut2')
                    cercle(e, f, taille_p, remplissage = 'green', tag = 'tagDebut3')
                    
                    
                    limiteA1 = a + 100 #limite afin que le pion n'ait que 8 possibilités
                    limiteA2 = a - 100 # joueur 1
                    
                    limiteB1 = b + 100
                    limiteB2 = b - 100
                    
                    
                    limiteJ1 = j + 100 #limite afin que le pion n'ait que 8 possibilités
                    limiteJ2 = j - 100 #joueur 2
                    
                    limiteK1 = k + 100
                    limiteK2 = k - 100
                    
                    limiteE1 = e + 100 #limite afin que le pion n'ait que 8 possibilités
                    limiteE2 = e - 100 #joueur 3
                    
                    limiteF1 = f + 100
                    limiteF2 = f - 100
                    
                    
                    
                    plateau[str(a)+str(b)] = 'Prise'
                    plateau[str(j)+str(k)] = 'Prise'
                    plateau[str(e)+str(f)] = 'Prise'
                    
                    
                #joueur 1    
                    
                ################vérifcation de possibilités de sorties pour le joueur 1          
                    if verifPLace(a,b)[3]:
                        bloquee1 = True
                        o, p = a,b # un des perdants activera la fin de la partie avec ses coordonnées
                    
                        if (bloquee1 and bloquee2) or (bloquee1 and bloquee3) or (bloquee2 and bloquee3):
                            i = 0
                            while i < 50:
                                sleep(0.1)
                                efface('resultat')
                                if(bloquee2 and bloquee3):
                                    texte(400,400, 'CONGRATULATIONS joueur 1 !', taille = i, tag = 'resultat',
                                      police = 'Impact', couleur = 'blue', ancrage = 'center' )
                                elif (bloquee1 and bloquee3) :
                                    texte(400,400, 'CONGRATULATIONS joueur 2 !', taille = i, tag = 'resultat',
                                      police = 'Impact', couleur = 'red', ancrage = 'center' )
                                elif (bloquee1 and bloquee2) :
                                    texte(400,400, 'CONGRATULATIONS joueur 3 !', taille = i, tag = 'resultat',
                                      police = 'Impact', couleur = 'green', ancrage = 'center' )
                                
                                i += 1
                                mise_a_jour()
                            
                                
                            over = veriFinPartie(o,p)    
                            if over == 'wi':
                                rep = 'try'
                                efface_tout()
                                plateau = etatCase()
                                break
                            elif over == 'xi':
                                rep = 'menu'
                                efface_tout()
                                plateau = etatCase()
                                break
                            elif over == 'ci':
                                rep = 'quit'
                                efface_tout()
                                plateau = etatCase()
                                break
                            
                    plateau[str(a)+str(b)] = 'Vide'
                           
                ##################################
                
                
                    while True:    
                        
                        efface('tag')
                        placeP = dpion1(a,b, limiteA1, limiteA2, limiteB1, limiteB2)
                        a, b, tag = placeP[0], placeP[1], placeP[2]  
                        pion1 = cercle(a,b, taille_p, remplissage = 'blue', tag = tag)
                        efface('traces')
                        if placeP[3] == 'ok':
                            if plateau[str(a)+str(b)] == 'Vide':
                                # si la case n'est pas vide ça ne marche pas
                                efface('tagDebut')
                                plateau[str(a)+str(b)] = 'Prise'
                                break
                        else:
                            cercle(a,b, taille_p, couleur = 'blue', tag = 'traces')
                            continue
                        
                    Cnr = case_noir(plateau)     
                    x, y, taille = Cnr[0], Cnr[1], Cnr[2]
                    rectangle(x, y, x + taille, y + taille, remplissage = 'black')
                    plateau[str(x+50)+str(y+50)] = 'Bloc'
                    
              
        
    ################vérifcation de possibilités de sorties pour le joueur 2          
             #joueur 2   
                    if verifPLace(j,k)[3]:
                        bloquee2 = True
                        o, p = j,k # un des perdants activera la fin de la partie avec ses coordonnées                   
                        if (bloquee1 and bloquee2) or (bloquee1 and bloquee3) or (bloquee2 and bloquee3):
                            i = 0
                            while i < 50:
                                sleep(0.1)
                                efface('resultat')
                                if(bloquee2 and bloquee3):
                                    texte(400,400, 'CONGRATULATIONS joueur 1 !', taille = i, tag = 'resultat',
                                      police = 'Impact', couleur = 'blue', ancrage = 'center' )
                                elif (bloquee1 and bloquee3) :
                                    texte(400,400, 'CONGRATULATIONS joueur 2 !', taille = i, tag = 'resultat',
                                      police = 'Impact', couleur = 'red', ancrage = 'center' )
                                elif (bloquee1 and bloquee2) :
                                    texte(400,400, 'CONGRATULATIONS joueur 3 !', taille = i, tag = 'resultat',
                                      police = 'Impact', couleur = 'green', ancrage = 'center' )
                                
                                i += 1
                                mise_a_jour()
                            over = veriFinPartie(o,p)    
                            if over == 'wi':
                                rep = 'try'
                                efface_tout()
                                plateau = etatCase()
                                break
                            elif over == 'xi':
                                rep = 'menu'
                                efface_tout()
                                plateau = etatCase()
                                break
                            elif over == 'ci':
                                rep = 'quit'
                                efface_tout()
                                plateau = etatCase()
                                break
                               
                #####################----------------------------------------------
                #joueur 2    
                    
                    plateau[str(j)+str(k)] = 'Vide'
                    
                    #plateau[str(c)+str(d)] = 'Vide'
                    
                    while True:
                        efface('tag2')
                        placeP2 = dpion2(j,k, limiteJ1, limiteJ2, limiteK1, limiteK2)
                        j, k, tag2 = placeP2[0], placeP2[1], placeP2[2]  
                        pion2 = cercle(j, k, taille_p, remplissage = 'red', tag = tag2)  
                        efface('traces2')
                        if placeP2[3] == 'ok':
                            if plateau[str(j)+str(k)] == 'Vide':
                               # si la case n'est pas vide ça ne marche pas
                               efface('tagDebut2')
                               plateau[str(j)+str(k)] = 'Prise'
                               break
                           
                        else:
                            cercle(j,k, taille_p, couleur = 'red', tag = 'traces2')
                            continue
                
                        
                    Cnr2 = case_grise(plateau)
                    x2, y2, taille2 = Cnr2[0], Cnr2[1], Cnr2[2]
                    rectangle(x2, y2, x2 + taille2, y2 + taille2, remplissage = 'grey')
                    plateau[str(x2+50)+str(y2+50)] = 'Bloc'
                   
                            
                            
                            
                            
       #################vérifcation de possibilités de sorties pour le joueur 3
             #joueur 3   
                    if verifPLace(e,f)[3]:
                        bloquee3 = True
                        o, p = e,f  # un des perdants activera la fin de la partie avec ses coordonnées
                    
                        if (bloquee1 and bloquee2) or (bloquee1 and bloquee3) or (bloquee2 and bloquee3):
                            i = 0
                            while i < 50:
                                sleep(0.1)
                                efface('resultat')
                                if(bloquee2 and bloquee3):
                                    texte(400,400, 'CONGRATULATIONS joueur 1 !', taille = i, tag = 'resultat',
                                      police = 'Impact', couleur = 'blue', ancrage = 'center' )
                                elif (bloquee1 and bloquee3) :
                                    texte(400,400, 'CONGRATULATIONS joueur 2 !', taille = i, tag = 'resultat',
                                      police = 'Impact', couleur = 'red', ancrage = 'center' )
                                elif (bloquee1 and bloquee2) :
                                    texte(400,400, 'CONGRATULATIONS joueur 3 !', taille = i, tag = 'resultat',
                                      police = 'Impact', couleur = 'green', ancrage = 'center' )
                                
                                i += 1
                                mise_a_jour()
                            over = veriFinPartie(o,p)    
                            if over == 'wi':
                                rep = 'try'
                                efface_tout()
                                plateau = etatCase()
                                break
                            elif over == 'xi':
                                rep = 'menu'
                                efface_tout()
                                plateau = etatCase()
                                break
                            elif over == 'ci':
                                rep = 'quit'
                                efface_tout()
                                plateau = etatCase()
                                break
                               
                #####################----------------------------------------------
                #joueur 2    
                    
                    plateau[str(e)+str(f)] = 'Vide'
                    
                    #plateau[str(c)+str(d)] = 'Vide'
                    
                    while True:
                        efface('tag3')
                        placeP3 = dpion3(e,f, limiteE1, limiteE2, limiteF1, limiteF2)
                        e, f, tag3 = placeP3[0], placeP3[1], placeP3[2]  
                        pion2 = cercle(e, f, taille_p, remplissage = 'green', tag = tag3)  
                        efface('traces3')
                        if placeP3[3] == 'ok':
                            if plateau[str(e)+str(f)] == 'Vide':
                               # si la case n'est pas vide ça ne marche pas
                               efface('tagDebut3')
                               plateau[str(e)+str(f)] = 'Prise'
                               break
                           
                        else:
                            cercle(e,f, taille_p, couleur = 'green', tag = 'traces3')
                            continue
                
                        
                    Cnr3 = case_violette(plateau)
                    x3, y3, taille3 = Cnr3[0], Cnr3[1], Cnr3[2]
                    rectangle(x3, y3, x3 + taille3, y3 + taille3, remplissage = 'purple')
                    plateau[str(x3+50)+str(y3+50)] = 'Bloc'        
                            
                            
                            
                    
                            
                    mise_a_jour        
                    
                if rep == 'menu':
                    break
                elif rep == 'quit':
                    ferme_fenetre()
                    
                mise_a_jour()

    #-------------------------------------------------------------------------------
##############    #################   mode ordi   ############################"
    ######## mode facile impeccable et bon joueur #####################################
    elif choix[0] == 'ordinateur':
        efface('choix')
        if choix[1] == '1':    
            while True:  
                plato()
                
                a, b, taille_p = 650, 650, 25       
                dep = 100
                
                c, d, taille_p = 150, 150, 25
                
                
                while True:
                    #pions au debut de la partie
                    
                    cercle(a, b, taille_p, remplissage = 'blue', tag = 'tagDebut')
                    #cercle(j, k, taille_p, remplissage = 'red', tag = 'tagDebut2')
                    cercle(c, d, taille_p, remplissage = 'orange', tag = 'tagDebutZ')
                    
                    
                    limiteA1 = a + 100 #limite afin que le pion n'ait que 8 possibilités
                    limiteA2 = a - 100 # joueur 1
                    
                    limiteB1 = b + 100
                    limiteB2 = b - 100
                    
                    
                    
                    plateau[str(a)+str(b)] = 'Prise'
                    plateau[str(c)+str(d)] = 'Prise'
                    
                    
                #joueur 1    
                    
                ################vérifcation de possibilités de sorties pour le joueur 2          
                    over = veriFinPartie(a,b)
                    if over == 'wi' or over == 'xi' or over == 'ci':     
                        i = 0
                        while i < 50:
                            sleep(0.1)
                            efface('resultat')
                            texte(400,400, 'GAME OVER', taille = i, tag = 'resultat',
                                  police = 'Impact', couleur = 'red', ancrage = 'center' )
                            i += 1
                            mise_a_jour()
                        if over == 'wi':
                            rep = 'try'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'xi':
                            rep = 'menu'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'ci':
                            rep = 'quit'
                            efface_tout()
                            plateau = etatCase()
                            break
                    
                    
                    plateau[str(a)+str(b)] = 'Vide'
                           
                ##################################
                #joueur 1
                
                    while True:    
                        
                        efface('tag')
                        placeP = dpion1(a,b, limiteA1, limiteA2, limiteB1, limiteB2)
                        a, b, tag = placeP[0], placeP[1], placeP[2]  
                        pion1 = cercle(a,b, taille_p, remplissage = 'blue', tag = tag)
                        efface('traces')
                        if placeP[3] == 'ok':
                            if plateau[str(a)+str(b)] == 'Vide':
                                # si la case n'est pas vide ça ne marche pas
                                efface('tagDebut')
                                plateau[str(a)+str(b)] = 'Prise'
                                break
                        else:
                            cercle(a,b, taille_p, couleur = 'blue', tag = 'traces')
                            continue
                        
                    Cnr = case_noir(plateau)     
                    x, y, taille = Cnr[0], Cnr[1], Cnr[2]
                    rectangle(x, y, x + taille, y + taille, remplissage = 'black')
                    plateau[str(x+50)+str(y+50)] = 'Bloc'
                    
                #----------------vérifcation de possibilités de sorties pour le joueur 2          
                          
                    over = veriFinPartie(c,d)
                    if over == 'wi' or over == 'xi' or over == 'ci':     
                        i = 0
                        while i < 50:
                            sleep(0.1)
                            efface('resultat')
                            texte(400,400, 'CONGRATULATIONS', taille = i, tag = 'resultat',
                                  police = 'Impact', couleur = 'green', ancrage = 'center' )
                            i += 1
                            mise_a_jour()
                        if over == 'wi':
                            rep = 'try'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'xi':
                            rep = 'menu'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'ci':
                            rep = 'quit'
                            efface_tout()
                            plateau = etatCase()
                            break
                                    #####################----------------------------------------------
                #ordi 2    
                    
                    f,g = c,d
                    """ on stocke les valeurs avant de les changer 
                    car sinon l'ordinateur resterait sur place"""
                    
                    #######################################      
                    #dpionZ
                    
                    
                    efface('tagZ')
                    placePZ = dpionZ(c,d)
                    print(placePZ)
                    c, d, tag = placePZ[0], placePZ[1], placePZ[2]  
                    pion1 = cercle(c,d, taille_p, remplissage = 'orange', tag = tag)
                    efface('tagDebutZ')
                    plateau[str(c)+str(d)] = 'Prise'
                    plateau[str(f)+str(g)] = 'Vide'
                    
                
                
                    CnrZ = case_marron(a,b, plateau)
                    xZ, yZ, taille2 = CnrZ[0], CnrZ[1], CnrZ[2]
                    rectangle(xZ, yZ, xZ + taille2, yZ + taille2, remplissage = 'brown')
                    plateau[str(xZ+50)+str(yZ+50)] = 'Bloc'
                #############################################
            
            
                            
                    
                    mise_a_jour        
                
                if rep == 'menu':
                    break
                elif rep == 'quit':
                    ferme_fenetre()
                    
            
            mise_a_jour()
            
    
    
    
######## mode moyen insupportable et sprinter #####################################             
        elif choix[1] == '2':    
            while True:  
                plato()
                
                a, b, taille_p = 150, 150, 25       
                dep = 100
                
                c, d, taille_pz = 650, 650, 15
                
                
                while True:
                    #pions au debut de la partie
                    
                    cercle(a, b, taille_p, remplissage = 'blue', tag = 'tagDebut')
                    #cercle(j, k, taille_p, remplissage = 'red', tag = 'tagDebut2')
                    cercle(c, d, taille_pz, remplissage = 'yellow', tag = 'tagDebutZ')
                    
                    
                    limiteA1 = a + 100 #limite afin que le pion n'ait que 8 possibilités
                    limiteA2 = a - 100 # joueur 1
                    
                    limiteB1 = b + 100
                    limiteB2 = b - 100
                    
                    
                    
                    plateau[str(a)+str(b)] = 'Prise'
                    plateau[str(c)+str(d)] = 'Prise'
                    
                    
                #joueur 1    
                    
                ################vérifcation de possibilités de sorties pour le joueur 2          
                    over = veriFinPartie(a,b)
                    if over == 'wi' or over == 'xi' or over == 'ci':     
                        i = 0
                        while i < 50:
                            sleep(0.1)
                            efface('resultat')
                            texte(400,400, 'GAME OVER', taille = i, tag = 'resultat',
                                  police = 'Impact', couleur = 'red', ancrage = 'center' )
                            i += 1
                            mise_a_jour()
                        if over == 'wi':
                            rep = 'try'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'xi':
                            rep = 'menu'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'ci':
                            rep = 'quit'
                            efface_tout()
                            plateau = etatCase()
                            break
                        
                    
                    plateau[str(a)+str(b)] = 'Vide'
                           
                ##################################
                #joueur 1
                
                    while True:    
                        
                        efface('tag')
                        placeP = dpion1(a,b, limiteA1, limiteA2, limiteB1, limiteB2)
                        a, b, tag = placeP[0], placeP[1], placeP[2]  
                        pion1 = cercle(a,b, taille_p, remplissage = 'blue', tag = tag)
                        efface('traces')
                        if placeP[3] == 'ok':
                            if plateau[str(a)+str(b)] == 'Vide':
                                # si la case n'est pas vide ça ne marche pas
                                efface('tagDebut')
                                plateau[str(a)+str(b)] = 'Prise'
                                break
                        else:
                            cercle(a,b, taille_p, couleur = 'blue', tag = 'traces')
                            continue
                        
                    Cnr = case_noir(plateau)     
                    x, y, taille = Cnr[0], Cnr[1], Cnr[2]
                    rectangle(x, y, x + taille, y + taille, remplissage = 'black')
                    plateau[str(x+50)+str(y+50)] = 'Bloc'
                    
                #----------------vérifcation de possibilités de sorties pour l'ordi          
                          
                    over = veriFinPartie(c,d)
                    if over == 'wi' or over == 'xi' or over == 'ci':     
                        i = 0
                        while i < 50:
                            sleep(0.1)
                            efface('resultat')
                            texte(400,400, 'CONGRATULATIONS', taille = i, tag = 'resultat',
                                  police = 'Impact', couleur = 'green', ancrage = 'center' )
                            i += 1
                            mise_a_jour()
                        if over == 'wi':
                            rep = 'try'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'xi':
                            rep = 'menu'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'ci':
                            rep = 'quit'
                            efface_tout()
                            plateau = etatCase()
                            break
                                    #####################----------------------------------------------
                #ordi 2    
                    
                    f,g = c,d
                    """ on stocke les valeurs avant de les changer 
                    car sinon l'ordinateur resterait sur place"""
                    
                    #######################################      
                    #dpionZ
                    
                    
                    efface('tagZ')
                    placePZ = dpionZ(x+50,y+50)
                    print(placePZ)
                    c, d, tag = placePZ[0], placePZ[1], placePZ[2]  
                    pion1 = cercle(c,d, 10, remplissage = 'yellow', tag = tag)
                    efface('tagDebutZ')
                    plateau[str(c)+str(d)] = 'Prise'
                    plateau[str(f)+str(g)] = 'Vide'
                    
                
                
                    """CnrZ = case_marron(a,b, plateau)
                    xZ, yZ, taille2 = CnrZ[0], CnrZ[1], CnrZ[2]
                    rectangle(xZ, yZ, xZ + taille2, yZ + taille2, remplissage = 'brown')
                    plateau[str(xZ+50)+str(yZ+50)] = 'Bloc'"""
                #############################################
            
            
                            
                    
                    mise_a_jour        
                
                if rep == 'menu':
                    break
                elif rep == 'quit':
                    ferme_fenetre()
                    
            mise_a_jour()
       
        
            
        
            
######## mode difficile, imbattable et tricheur #####################################
                
        elif choix[1] == '3':    
            while True:  
                plato()
                
                a, b, taille_p = 150, 150, 25       
                dep = 100
                
                c, d, taille_pz = 150, 250, 25
                
                
                while True:
                    #pions au debut de la partie
                    
                    cercle(a, b, taille_p, remplissage = 'blue', tag = 'tagDebut')
                    #cercle(j, k, taille_p, remplissage = 'red', tag = 'tagDebut2')
                    cercle(c, d, taille_pz, remplissage = 'black', tag = 'tagDebutZ')
                    cercle(c,d, 20, remplissage = 'white', tag = 'tagDebutZ')
                    
                    
                    limiteA1 = a + 100 #limite afin que le pion n'ait que 8 possibilités
                    limiteA2 = a - 100 # joueur 1
                    
                    limiteB1 = b + 100
                    limiteB2 = b - 100
                    
                    
                    
                    plateau[str(a)+str(b)] = 'Prise'
                    plateau[str(c)+str(d)] = 'Prise'
                    
                    
                #joueur 1    
                    
                ################vérifcation de possibilités de sorties pour le joueur 2          
                    over = veriFinPartie(a,b)
                    if over == 'wi' or over == 'xi' or over == 'ci':     
                        i = 0
                        while i < 50:
                            sleep(0.1)
                            efface('resultat')
                            texte(400,400, 'GAME OVER', taille = i, tag = 'resultat',
                                  police = 'Impact', couleur = 'red', ancrage = 'center' )
                            i += 1
                            mise_a_jour()
                        if over == 'wi':
                            rep = 'try'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'xi':
                            rep = 'menu'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'ci':
                            rep = 'quit'
                            efface_tout()
                            plateau = etatCase()
                            break
                    
                    plateau[str(a)+str(b)] = 'Vide'
                           
                ##################################
                #joueur 1
                
                    while True:    
                        
                        efface('tag')
                        placeP = dpion1(a,b, limiteA1, limiteA2, limiteB1, limiteB2)
                        a, b, tag = placeP[0], placeP[1], placeP[2]  
                        pion1 = cercle(a,b, taille_p, remplissage = 'blue', tag = tag)
                        efface('traces')
                        if placeP[3] == 'ok':
                            if plateau[str(a)+str(b)] == 'Vide':
                                # si la case n'est pas vide ça ne marche pas
                                efface('tagDebut')
                                plateau[str(a)+str(b)] = 'Prise'
                                break
                        else:
                            cercle(a,b, taille_p, couleur = 'blue', tag = 'traces')
                            continue
                        
                    Cnr = case_noir(plateau)     
                    x, y, taille = Cnr[0], Cnr[1], Cnr[2]
                    rectangle(x, y, x + taille, y + taille, remplissage = 'black')
                    plateau[str(x+50)+str(y+50)] = 'Bloc'
                    
                #----------------vérifcation de possibilités de sorties pour le joueur 2          
                          
                    over = veriFinPartie(c,d)
                    if over == 'wi' or over == 'xi' or over == 'ci':     
                        i = 0
                        while i < 50:
                            sleep(0.1)
                            efface('resultat')
                            texte(400,400, 'CONGRATULATIONS', taille = i, tag = 'resultat',
                                  police = 'Impact', couleur = 'green', ancrage = 'center' )
                            i += 1
                            mise_a_jour()
                        if over == 'wi':
                            rep = 'try'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'xi':
                            rep = 'menu'
                            efface_tout()
                            plateau = etatCase()
                            break
                        elif over == 'ci':
                            rep = 'quit'
                            efface_tout()
                            plateau = etatCase()
                            break
                           
                #####################----------------------------------------------
                #ordi 2    
                    
                    f,g = c,d
                    """ on stocke les valeurs avant de les changer 
                    car sinon l'ordinateur resterait sur place"""
                    
                    #######################################      
                    #dpionZ
                    
                    
                    efface('tagZ')
                    placePZ = dpion0(a,b)
                    print(placePZ)
                    c, d, tag = placePZ[0], placePZ[1], placePZ[2]  
                    pion1 = cercle(c,d, 25, remplissage = 'black', tag = tag)
                    cercle(c,d, 20, remplissage = 'white', tag = tag)
                    
                    efface('tagDebutZ')
                    plateau[str(c)+str(d)] = 'Prise'
                    plateau[str(f)+str(g)] = 'Vide'
                    
                
                
                    CnrZ = case_marron(a,b, plateau)
                    xZ, yZ, taille2 = CnrZ[0], CnrZ[1], CnrZ[2]
                    rectangle(xZ, yZ, xZ + taille2, yZ + taille2, remplissage = 'brown')
                    plateau[str(xZ+50)+str(yZ+50)] = 'Bloc'
                #############################################
            
            
                            
                    
                    mise_a_jour        
                
                if rep == 'menu':
                    break
                elif rep == 'quit':
                    ferme_fenetre()
                    
            
            mise_a_jour()
                
                    

