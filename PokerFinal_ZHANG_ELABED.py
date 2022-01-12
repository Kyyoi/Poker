import random
import time
#random.Random()
# Liste des symboles des cartes
couleur2 = ["Trefle","Carreau","Coeur","Pique"]
couleur= ["♥","♦","♠","♣"]

# Liste des valeurs dans un jeu de 32 cartes
vals = [(2, '2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),
        (8,'8'),(9,'9'),(10,'10'),(11,'Valet'),
        (12,'Dame'),(13,'Roi'),(14,'As')]

#on a du reformater les cartes, car inutilisable dans les anciennes versions
# Ensemble des valeurs dans un jeu de 52 cartes
#Programme soit avec dictionnaire soit avec tuple
class joueur:
    typ="humain"
    banque=500
    bet=False 
    call=False
    check=False
    fold=False
    nom=None
    main=[]
    carteHaute=[]#la plus grande combi de grandeMain
    grossblind=False
    ptitblind=False
    combi=0#numéro de la combi
    grandeMain=[]#la somme des cartes de la table+main du joueur
    
    def __init__(self):
        nom=input("Entrez le nom d'un joueur\n")
        self.nom=nom
    def __str__(self):
        return ""+str(self.nom)

class bot(joueur):
    typ="bot"
    choix=3
    mise=20
    listeN=["Rida","Kevin","Maxime","Rosen","Ange","Huna","Selim","Momo","Iskander",
            "Sarah","Yohan","Abdou","Madhusha","Youva","XuanHao",
            "Katia","Ahmed","Nassim"]
    listeP=["va pouvoir manger autre chose que du pain ce soir!",
            "pourra manger des pates au beurre!",
            "pourra s'endetter encore plus!",
    "va s'acheter un Happy Meal!","achetera une collection Stickers!",
            "pourra se prendre des vacances aux Alpes!"]
    def __init__(self,r=False):
        self.r=r
        self.nom=random.choice(self.listeN)
        self.listeN.remove(self.nom)
    def decisionrandom(self):
        r=float(random.random())
        if(r<0.20):
            self.choix=1
        if(r<0.40):
            print("Mmmh... Allons-y !")
            self.choix=2
        if(r<0.80):
            self.choix=3
        else:
            print("Je ne suivrai pas..")
            self.choix=4
        return self.choix
    def decision(self):
        if (self.combi<2):
            if(self.main[0][1]==14 or self.main[1][1]==14):
                self.mise=50
                self.choix=1
                return 1
            self.choix=3
        if (self.combi==4):
            self.choix=1
            self.mise=50
        if(self.combi==5):
            self.choix=1
            self.mise=75
        if(self.combi==6):
            self.choix=1
            self.mise=80
        if(self.combi==7):
            self.choix=1
            self.mise=100
        if(self.combi==8):
            self.choix=1
            self.mise=self.banque
        return self.choix
#space()
def nbjoueur(x):
    a=int(input("\nEntrez un nombre de joueur, max 5 \n"))
    while(a<=1 or a >5):
        print("Veuillez entrer un nombre de joueur valide entre 2 et 5\n")
        a=int(input("\nEntrez un nombre de joueur, max 5\n"))
    listej=[]
    if(x==False):
        for i in range(a):
            listej.append(joueur())
    if(x==True):
        if (a>2):
            i=2
            a-=i
            listej.append(bot())
        for i in range(a):
            listej.append(bot(True))
        #print(listej[i])
        listej.append(joueur())
    #print(listej)
    return listej

def creationPaquet():
    Paquet=[]
    while (("♣",14,"As") not in Paquet):
        for i in couleur:#on parcourt les couleurs possibles
            #print("On en est à la couleur",i)
            for j in vals:#parcours des valeurs
                #if ( (i,j[0],j[1]) not in Paquet):#si la carte n'existe pas dans le paquet, ajouter
                Paquet.append((i,j[0],j[1]))
    return Paquet

def tri(tab,i,j):
    temp=tab[i]
    tab[i]=tab[j]
    tab[j]=temp

#test
#u=random.random()*52
#print(u)

def shuffle(Paquet):
    for i in range(len(Paquet)):#on melange bien chaque carte
        r=int(random.random()*52)#prends une carte au hasard, melange simple
        tri(Paquet,i,r)#tri basique
    #print(Paquet)
    return Paquet

P=creationPaquet()
shuffle(P)
#print(P)
#print(len(P))

#liste=distribution(nbjoueur(3),P2)
#print(liste[0].main)

def affichej(listejoueur):
    #afficher simplement les cartes de chaque joueur
    cpt=0
    for i in listejoueur:
        cpt+=1#parcours le nb de joueur
        print("Joueur",cpt,"main=",listejoueur[cpt-1])
#affichej(listej)

def Flop(Paquet):
    Terrain=[]
    print("----Flop----")#on retourne les 3 premieres carte du terrain du paquet
    #A changer pour prendre 5 carte direct/A VOIR, le joueur ne verra pas la diff
    #On aurra juste a print les cartes de Terrain dans l'odre sinon
    for i in range(3):
        Terrain.append(Paquet[i])#on ajoute les 3 carte du paquet a la table
        Paquet.remove(Paquet[i])
    #print(Terrain)
    return Terrain

def affichagec(listec):
    l=[]
    for i in listec:
        l.append((i[2],i[0]))
    return l

def Turn(Paquet):
    #Terrain=[]
    #on appelle la fonction pour miser
    print("----Turn----")
    #Terrain.append(Paquet[i+1])
    #Paquet.remove(Paquet[i+1])
    #Terrain.append(Paquet[0])
    p=Paquet[0]
    Paquet.remove(Paquet[0])
    #print(Terrain)
    return p

def River(Paquet):
    #Terrain=[]
    #on appelle la fonction pour miser
    print("----River----")
    #Terrain.append(Paquet[0])
    p=Paquet[0]
    Paquet.remove(Paquet[0])
    #print(Terrain)
    #on apelle la fonction pour miser
    return p
#pas=tour(P2)

def QuinteFlushRoyal(listeC):
    #print("\nliste=",listeC)
    cpt=0
    coul=0
    for i in listeC:
        couleur=listeC[0][0]
        #print(i)
        if (couleur ==i[0]):
            coul+=1
        if ("10" in i):
            cpt+=1
        elif ("Valet" in i):
            cpt+=1
        elif ("Dame" in i):
            cpt+=1
        elif ("Roi" in i):
            cpt+=1
        elif ("As" in i):
            cpt+=1

    #print("Liste",i,cpt)
    if (cpt == 5) and (coul == 5):
        print("QUINTE FLUSH ROYAL!!!")
        return True
    else:
        return False

#count() peut etre utile ici...
#QuinteFlushRoyal(qfr)

listeQ=[("Carreau",8,"Huit"),("Carreau",2,"Deux"),("Pique",13,"Roi"),("Pique",3,"Trois"),
        ("Pique",4,"Quatre"),("coeur",5,"Cinq"),
        ("Coeur",6,"Six"),("Pique",7,"Sept"),("Pique",2,"Deux")]

listeq=[("Pique",4,"Quatre"),("Coeur",3,"Trois"),("Pique",3,"Trois"),("Carreau",3,"Trois")
        ,("Coeur",3,"Trois")]

def Quinte(listeC):
    #l=sorted(listeC)#rearrange dans le bon ordre pour verif
    l2=[]
    i=0
    cpt=0
    l=[]
    lm=[]
    #print("Dans Quinte-----\n",listeC,"longueur=",len(listeC))
    for i in listeC:
        #print("i",i[1])
        #print("Quinte===\n",i,"\nLISTEC\n",listeC)
        lm.append(i[1])
    l=sorted(lm)
    #print("liste rangée",l)
    #print(lm)
    i=0
    while(i<len(l)-1):#on parcourt toute les cartes
        if ( l[i]+1 == l[i+1]):#si la carte suivante et celle ou on se situe se suivent
            #alors on les ajoute
            cpt+=1
            l2.append(l[i])
        else:
            cpt=0
            l2=[]
        i+=1
    #print("longueur de la suite",cpt,l2)
    if (cpt >= 5):
        l3=[]
        for i in range(5):
            l3.append(l2[len(l2)-i-1])
        #print(l3)#resors la plus grande quinte de la main
        print("Quinte")
        return (True,l3)#return + gd quinte
    else :
        return (False,l2)
#Quinte(listeQ)

def Couleur(listeC):
    l=[]
    for j in listeC:
        l.append(j[0])
    #print("l",l)
    for i in l:
        #print(i)
        if ( l.count(i)==5):
            #print("Couleur de",i)
            return (True,i)
    #print("Coueleur fausse")
    return (False,1)
#Couleur(listeQ)

def Brelan(listeC):
    l=[]
    for i in listeC:
        l.append(i[1])
    listeC=sorted(listeC)
    #print(listeC)
    l2=[]
    for i in listeC:
        #print(i)
        l2.append(i[1])
    for i in range(len(l2)):
        #print(l2.count(l2[i]),i)
        if (l2.count(l2[i])==3):
            p=(True,i)
            #print(p[0])
            return (True,l2[i])
    return (False,1)
bre=[("Pique",4,"Quatre"),("Coeur",3,"Trois"),("Pique",3,"Trois"),("Carreau",3,"Trois")]
#Brelan(listeQ)

def Pair(listeC):
    lis=sorted(listeC)
    l=[]
    l2=[]
    for i in lis:
        l.append(i[1])
    #print(l)
    sorted(lis)
    for j in l:
        #print(j)
        if ( l.count(j)==2):
            l2.append(j)
    if (l2!=[]):
        m=max(l2)#on retourne la plus grande pair dans notre main
        for i in listeC:
            if m in i:
                #print("Paire de", i[2]) 
                return (True,(i[2],i[0]))
    return (False,1)
p=Pair([("Carreau",4,"Quatre"),("Coeur",13,"Roi")
        ,("Carreau",4,"Quatre"),("Carreau",14,"As"),("Pique",13,"Roi")])
#print(p)

def DoublePair(listeC):
    cpt=0
    lis=listeC
    p=Pair(lis)
    #print(p)
    if (p[0]==True):
        cpt+=1
    else:
      return (False,1)
    #print(lis,p[1][0])
    #print(lis)
    for i in lis:
      #print(i,p[1])
    
      if (i[2]==p[1][0]):
        temp=i
        lis.remove(i)
        #print("---------------------DB------------------")
    #print(lis,i[2])
    p2=Pair(lis)
    #print(p2)
    #print(lis)
    lis.append(temp)
    #print(lis)
    if (p2[0]==True):
        cpt+=1
    if cpt==2:
        return (True,(p2[1][0],p[1][0]))
    else:
        return [False]
db=DoublePair([("Carreau",4,"Quatre"),("Coeur",13,"Roi")
        ,("Carreau",4,"Quatre"),("Carreau",14,"As"),("Pique",13,"Roi")])
#print(db)
def full(listeC):
    b=Brelan(listeC)
    p=Pair(listeC)
    if( b[0]==True):
        if(p[0]==True):
            print('Full de',p[1][0],b[1])
            return (True,(p[1][0],b[1]))
    return (False,1)
fu=[("Coeur",3,"Trois"),("Carreau",2,"Deux"),("Coeur",3,"Trois"),("Pique",2,"Deux"),("Coeur",3,"Trois")]
#full(fu)

def Carre(listeC):
    l=[]
    for j in listeC:
        l.append(j[1])
    #print("l",l)
    for i in l:
        #print("i",i)
        if ( l.count(i)==4):
            #print("Carre de",i)
            return (True,i)
    return (False,1)
#Carre(listeq)
#print(listeq)

def CarteHaute(listeC):
    l=[]
    
    dic={11:"Valet",
    12:"Dame",
    13:"Roi",
    14:"As"
    }
    lis=listeC
    for i in lis:
        l.append(i[1])
    if (max(l) in dic):
        return (True,dic[max(l)])
    return (True,max(l))

#CarteHaute(listeQ)

def plusHaut(listeC,j):
    #methode pour ressortir la combinaison la plus haute
    lis=listeC
    a=QuinteFlushRoyal(lis)
    
    if(a==True):
        if (j.typ=="humain"):
            print("QFR",a)
        return (a,8)
    c=Carre(lis)
    
    if (c[0]==True):
        if (j.typ=="humain"):
            print("Carre de",c[1])
        return (c,7)
    h=full(lis)
    
    if (h==True):
        #print("full",h[1])
        return (h,6)
    d=Couleur(lis)
    
    if (d[0]==True):
        if (j.typ=="humain"):
            print("Couleur de",d[1])
        return (d,5)
    b=Quinte(lis)
    
    if (b[0]==True):
        if (j.typ=="humain"):
            print("quinte",b)
        return (b,4)
    e=Brelan(lis)
    
    if (e[0]==True):
        if (j.typ=="humain"):
            print("Brelan de",e[1])
        return (e,3)
    i=DoublePair(lis)
    
    if (i[0]==True):
        if (j.typ=="humain"):
            print("Double Pair de",i[1])
        return (i,2)
    f=Pair(lis)
    
    if (f[0]==True):
        if (j.typ=="humain"):
            print("Paire de",f[1])
        return (f,1)
    g=CarteHaute(lis)

    if (g[0]==True):
        #print("Carte Haute:\n",g[1])
        return (g,0)

li=[("Pique",13,"Roi"),("Pique",3,"Trois"),
    ("Pique",4,"Quatre"),("Pique",5,"Cinq"),
    ("Pique",9,"Neuf")]
#plusHaut(li)

def GrosseMain(Terrain,main):
    #methode qui retourne quel est notre 'grosse main'
    main=Terrain+main#à utliser avec joueur.main
    #print(main)

    return main
#a=GrosseMain([("Coeur",5,"Cinq"),
    #("Pique",9,"Neuf")],[("Pique",13,"Roi"),("Pique",3,"Trois"),
    #("Pique",4,"Quatre")])
#plusHaut(a)
#print("grosse main",a)

def miser(j):
    if (j.typ=="humain"):
        a=int(input("Choisissez votre mise\n"))
        
    else:
        print(j.nom,"veut miser...")
        time.sleep(3)
        if (j.mise>j.banque):
            j.mise=j.banque
        a=j.mise
    return a

def option(j):
    if (j.typ=="humain"):
        choix=int(input("Voulez vous: \n1-Miser \n2-Suivre \n3-Check \n4-Fold\n5-Quitter la partie\n"))
        while(choix not in [1,2,3,4,5]):
            choix=int(input("Je n'ai pas compris: \n1-Miser \n2-Suivre \n3-Check \n4-Fold\n5-Quitter la partie\n"))
            
    else:
        print(j.nom,"est entrain de réfléchir...")
        time.sleep(3)
        if (j.r==False):
            choix=j.decision()
            return choix
        else:
            choix=j.decisionrandom()
            return choix
    return choix

def out(listej):
    #vérifie si un joueur peut continuer de jouer
    listOut = []
    for i in listej:
        if i.banque <= 0 : 
            listOut.append(i)
            print(i,"est out")
    return listOut

def betFalse (listej): 
#parcours tous les joueurs, et mets leur bet à false
    for i in range(len(listej)):
        listej[i].bet=False
    return listej

def seReveiller (listej):
    #parcours tous les joueurs et met leur fold à false 
    for i in range(len(listej)):
        listej[i].fold=False
    return listej

def isSleeping (listej):
    #parcours tous les joueurs, et vérifie combien de joueurs se sont couchés.
    #S'il ne reste plus que 1 joueur non couché, alors le tour se fini
    cpt = 0

    for i in listej:
        if (i.fold == True):
            cpt += 1
        if (i.fold == False):
            p=i
            #print("Dans sleep",i)
    #print("cpt",cpt)
    if (cpt == len(listej)-1):
        #print("ici",i)
        return (True,p)
    else :
        return [False]

def distribution(listej,Paquet):
    cpt=0
    for i in listej:
        #distribution pour chaque joueur
        #print(i.main)
        taille=51
        i.main=[]#probleme de classe, car ne supprime pas la main chaque fois, cours POO
        for j in range(2):#nombre de carte a distribuer
            taille-=cpt
            r=int(random.random()*taille)#on prend une carte random(ou le dessus normalement
            #donc Paquet[j] +simple, mais là c'est en random poru test) 52=notre nombre de carte
            while(r<0 or r>51):#il ne faut pas que r<0 sinon valeur négative dans le paquet
                #print(r)
                r=int(abs(random.random()*taille))
            #print("0000apres",r)
            i.main.append(Paquet[r])#on ajoute la carte a la main du joueur
            Paquet.remove(Paquet[r])#on retire la carte du paquet
            cpt+=1#on utilise le compteur pour reduire le choix de carte tirable
        #print("Joueur",i.nom,i.main)
    #print(len(listej))
    #for i in listej:
    #    if len(i.main)<2:
    #        print(erreur)
    return (listej,Paquet)

"""
p=[]
for i in range(15):
    p.append(bot())
j=distribution(p,P)

for i in j[0]:
    print(i.main)
    if len(i.main)<2:
        print("-------------------------------------------")
"""
def space():
    for i in range(10):
        print()

def reset(listej):
    P=creationPaquet()
    P=shuffle(P)
    j,P=distribution(listej,P)
    for i in j:
        while (len(i.main)<2):
            j,P=distribution(listej,P)
    for i in listej:
        i.grossblind=False
        i.ptitblind=False
        i.fold=False
    return (j,P)

def gdcombi(listej):
    l=[]
    l2=[]
    val=(joueur,0)
    for i in listej:
        for j in i.grandeMain:
            #print(j)
            l2.append(int(j[1]))
        temp1=(i,max(l2))
        if (temp1[1]>val[1]):
            val=(i,max(l2))
    #print(val[0])
    #if(val[1]==temp1[1]):
        #print("égalité")
        #return (val,temp1)
    return val

#pi=nbjoueur(3)
#gdcombi(pi)

def gagnant(listej):
    #quel joueur à la plus grande main et gagne à la fin du tour
    #niveau 0 combi la plus faible à + combi la plus élevée comme un dictionnaire
    #niveau 0 = carte haute simple
    #niveau 1 = pair etc...
    dic={0:[],
         1:[],
         2:[],
         3:[],
         4:[],
         5:[],
         6:[],
         7:[],
         8:[]
         }
    for i in listej:#on ajoute les joueurs dans la liste du dic
        if (i.fold==False):
            dic[i.combi].append(i)
    i=7#on commence par la combi la plus haute
    while i!=-1:#on parcourt toutes les combi possibles
        if (len(dic[i])>1):#si on a 2 joueurs sur une meme combi
            p=gdcombi(dic[i])#alors on vérifie qui a la plus grande combi
            #print("ici",p[0])
            return p[0]#retourner ce joueur gagnant
        if(len(dic[i])==1):#si il y a exactement 1 seul joueur gagnant
            #print(dic[i])
            #print(len(dic[i]))
            #print("icin",dic)
            return dic[i][0]#retourner ce joueur
        if (len(dic[i])==0):#si il n'ya aucune combi on continue
            i-=1
    #retourne le joueur gagnant avec a combi la plus haute

#gagnant(pi)
def mise(listej):
    #retourne True si un joueur a déjà miser
    cpt=0
    for i in listej:
        if i.bet==False:
            cpt+=1
    if cpt==len(listej):
        return True

def table(x):
     #à donner
    #a=2
    pot=0
    call=0#on initialise toute la table
    blind=30
    j=nbjoueur(x)
    #---------distribution des cartes pourchaque joueur
    P=creationPaquet()
    P=shuffle(P)
    j,P=distribution(j,P)#chaque joueur à sa main rempli
    for i in j:
        while (len(i.main)<2):
            j,P=distribution(j,P)
    carteTable=[]
    ##commencement du jeu
    nbround=1
    tourblind=1
    b=0
    j[b].grossblind=True
    j[b+1].ptitblind=True
    space()
    print("La partie se lance, bonne chance !")
    pot=blind+int(blind/2)
    while(len(j)!=1):#tant qu'il reste au moins 2 joueurs sur la table     ----len(j)
        #pot=45
        call=0
        m=0
        if (x==True):#partie avec les bots
            for d in j:#determine l'emplacement du joueur
                if d.typ=="humain":
                    hu=d
            if (hu not in j):#si le joueur humain n'est plus de la partie
                print("Vous avez perdu la partie...")
                c=5#fin de partie
                break
        if(int(nbround/5)==1):
            nbj=0
            u=out(j)#liste des joueurs qui n'ont plus de credits
            for i in u:
                j.remove(i)
            j,P=reset(j)#nouveau paquet et distribution
            carteTable=[]
            nbround=0#à changer de variable si on veut afficher nbround
            seReveiller(j)#mets tous les joueurs fold à false
            b+=1
            pot=blind+int(blind/2)
            if ((b+1)==len(j)):
                #print("---------------------------------------------------------------")
                j[b].grossblind=True
                #print(1,j[b])
                j[0].ptitblind=True
                b=0
            else:
                #print(2,j[b])
                #print("b=",b,"b+1=",b+1,"long",len(j))
                #b+=1
                #print(j[b],j[b+1])
                j[b].grossblind=True
                j[b+1].ptitblind=True
            
            tourblind+=1
            if(tourblind%3==0):
                blind=blind*2
                print("---------------------------------------------------------------")
                print("Les blinds vont augmenter au prochain tour!",int(blind/2),"/",blind)
        print("\nTour numero:",tourblind)
        nbround+=1
        if (nbround==3):#prochain tour on flop
            carteTable=Flop(P)
        if(nbround==4):#puis turn
            carteTable.append(Turn(P))
        if(nbround==5):#enfin river
            carteTable.append(River(P))
        af=affichagec(carteTable)
        
        i=0
        #print(j[i].banque)
        spe=0
        while(i<len(j)):#on fait jouer les joueurs
            if(j[i].banque==0 or j[i].bet==True):
                j[i].bet=False
                #print("\n",j[i],j[i].main,"\n")
                #if(carteTable!=[]):
                #    print("\nVoici les cartes de la Table:\n",carteTable,"\n")
                i+=1
                #nbround-=1
                #tourblind=1
                #print("nbround-1",nbround)
                #pour miser à l'infini entre les joueurs tant qu'ils ont l'argent
                continue
                
            if(j[i].fold==True):
                i+=1
                continue
            #print('i\n',i)
            #print("ici",j[i].bet)
            op=isSleeping(j)
            if(op[0]==True):
                op[1].banque+=pot
                print("Le gagnant du tour est:", op[1])
                print(op[1],"récupere",pot)
                #seReveiller(j)
                #print("issleeping")
                nbround=5
                break
            if (mise(j)==False):
                m=0
                for i in j:
                    i.bet=False
                print("Tour du joueur",j[i].nom)
            print("\nNombres de joueurs en jeu",len(j),"\n")
            gr=GrosseMain(carteTable,j[i].main)
            j[i].grandeMain=gr
            #print(j[1].grossblind)
            print("Pot en cours:",pot)
            #print(j[i].banque)
            if (carteTable != []):
                print("\nVoici les cartes de la Table:\n",carteTable,"\n")
            #print(j[i].banque,j[1].grossblind)
            if j[i].typ=="humain":
            	print("\nMeilleure combinaison de votre main:")
            ca=plusHaut(gr,j[i])
            j[i].carteHaute=ca[0][1]#mettre de coté la plus haute combi
            j[i].combi=ca[1]
            if (j[i].combi==0):
                """if (len(j[i].main)<2):
                    print(ca,j[i],"------------------------------------------")
                    exit"""
                ca=plusHaut(j[i].main,j[i])
                """if (len(j[i].main)<2):
                    print(ca,j[i],"2------------------------------------------")
                    exit"""
                j[i].combi=ca[1]
                j[i].carteHaute=ca[0][1]
                if j[i].typ=="humain":
                	print("Carte Haute:\n",ca[0][1])
            if j[i].fold==False:
                if j[i].typ=="humain":
                	print("\nVoici vos cartes:\n   ",affichagec(j[i].main),"\n")
                else:
                	print("\nVoici les cartes du Joueur",j[i].nom,":\n[(****),(****)]")
                #if (carteTable!=[]):
                #    print("\nVoici votre main combinée à celle de la table:\n",affichagec(gr),"\n")
                #print("\nCombi Haute:\n",j[i].carteHaute,"\n")
                #print(j[i].banque)
                #afficher les blinds des joueurs
                #Histoire de Blind
                if (nbround<=2):
                    if (j[i].grossblind==True): 
                        print("Vous êtes la grosse Blind")
                        j[i].banque-=blind
                        if(j[i].banque<=0):
                            j[i].banque=0
                        #j[i].grossblind=False
                    #print(j[1].ptitblind)
                        #print(4,j[b].grossblind)
                    if (j[i].ptitblind==True):
                        print("Vous êtes la petite Blind")
                        j[i].banque-=int(blind/2)
                        if(j[i].banque<=0):
                            j[i].banque=0
                        #j[i].ptitblind=False
                #print(j[i].banque)
                if(nbround>2):
                    for ip in j:
                        ip.grossblind=False
                        ip.ptitblind=False
                #print(j[i].banque)
                #print(5,j[b].grossblind)
                print("\nVotre Argent restant, Joueur",j[i].nom,":",j[i].banque)
                #print(j[i].banque)
                #if (len(j[i].main)<2):
                #    print("--------------------------",len(P),P)
                c=option(j[i])
                #print(c)
                space()
                #print("choix du joueur",j[i].nom,"Choix",c)
                #print("type de c",type(c))
                #print("i",j[i].bet)
                if(nbround<=0):
                    #print("nnnnnnnnnnnnnnn",nbround)
                    nbround=1
                
                if c==1 and j[i].bet==False: #miser
                    #mis=nbround
                    print("Pot en cours",pot)
                    print("Votre argent restant:",j[i].banque)
                    if (j[i].banque<0):
                        
                        print("Vous n'avez pas assez d'argent")
                        i+=1
                        continue
                    
                    m=miser(j[i])
                    m+=spe
                    spe=m
                    if(m<blind):
                        m=blind
                    while(m<=0):
                        print("Veuillez saisir une mise valide")
                        m=miser(j[i])
                    if (m>j[i].banque):
                        #ne doit pas dépasser la somme dans la banque du joueur
                        m=j[i].banque
                        print("\nAll-IN!\n")
                    if (m>call):
                        call=m
                    space()
                    j[i].banque-=m
                    if (nbround<=2 and j[i].grossblind==False):
                        #print("ici")
                        if(j[i].banque>blind):
                            j[i].banque-=blind
                            pot+=blind
                    if(j[i].banque<0):
                        j[i].banque=0
                    print(j[i].nom,"mise",m)
                    pot+=m
                    
                    #reparcourir les autres joueurs, et mettre leur bet à false
                    j=betFalse(j)
                    j[i].bet=True
                    i=0
                    print("Nouveau pot",pot,"\n")
                    #i+=1
                    #print('nbround3',nbround)
                    #nbround-=1
                    continue
                
                if c==2:#call
                    mis=0
                    #print("Joueur",j[i].nom,"check")
                    print("Ancien pot",pot)
                    if (nbround<=2 and j[i].grossblind==False):
                        #print(blind)
                        mis=blind
                    if (nbround<=2 and j[i].ptitblind==True):
                        mis=int(blind/2)
                        
                        j[i].ptitblind=False
                    j[i].banque-=mis
                    pot+=mis
                    if(j[i].banque<=0):
                        i+=1
                        continue
                    #print(j[i].nom,j[i].ptitblind)
                    if (m>j[i].banque):
                        #ne doit pas dépasser la somme dans la banque du joueur
                        call=j[i].banque
                    #print(pot,call,mis)
                    pot+=call
                    #print(pot,call,mis)
                    j[i].banque-=call
                    if(j[i].banque<0):
                        j[i].banque=0
                    #pot+=m
                    if(m==0):
                        print(j[i].nom,"check")
                    else:
                        print(j[i].nom,"call",m)
                        #j[i].banque-=m
                    if(j[i].banque<0):
                        j[i].banque=0
                        j[i].bet=True
                    print("\nNouveau pot\n",pot)
                    j[i].grossblind=False
                    i+=1
                    continue
                    
                if c==3:#check
                    mis=0
                    #print("Joueur",j[i].nom,"check")
                    print("Ancien pot",pot)
                    if (nbround<=2 and j[i].grossblind==False):
                        #print(blind)
                        mis=blind
                    if (nbround<=2 and j[i].ptitblind==True):
                        mis=int(blind/2)
                        
                    j[i].banque-=mis
                    j[i].ptitblind=False
                    pot+=mis
                    if(j[i].banque<=0):
                        i+=1
                        continue
                    #print(j[i].nom,j[i].ptitblind)
                    if (m>j[i].banque):
                        #ne doit pas dépasser la somme dans la banque du joueur
                        call=j[i].banque
                    #print(pot,call,mis)
                    pot+=call
                    #print(pot,call,mis)
                    j[i].banque-=call
                    if(j[i].banque<0):
                        j[i].banque=0
                    #pot+=m
                    if(m==0):
                        print(j[i].nom,"check")
                    else:
                        print(j[i].nom,"call",m)
                        #j[i].banque-=m
                    if(j[i].banque<0):
                        j[i].banque=0
                        j[i].bet=True
                    print("\nNouveau pot\n",pot)
                    j[i].grossblind=False
                    i+=1
                    continue

                if c==4:
                    print(j[i].nom,"fold")
                    j[i].fold=True
                    print("Pot en cours",pot,"\n")
                    i+=1
                    continue
                    
                if c==5:
                    break
                else :
                    continue
        if c==5:
            break
    #if(c==5):
        #exit
        if ((nbround==5) and (op[0]==False)):
            #A la fin de la river on détermine qui gagne et ajoute le pot
            ga=gagnant(j)
            ga.banque+=pot
            print("Le gagnant du tour est:",ga)
            print(ga,"récupere",pot)
            pot=blind+int(blind/2)
        #condition de sortie du while
            u=out(j)#liste des joueurs qui n'ont plus de credits
            for i in u:
                j.remove(i)
    print ('Le gagnant du jeu est:',j[0],"!")
    if j[0].typ=="bot":
            	print(j[0].nom,random.choice(j[0].listeP))
    if c==5:
        exit
    print("Retour au menu...")
    time.sleep(3)
    space()
    initialisation()
    exit
#table()
def initialisation():
    print("\nBienvenue Au Jeu De Poker !")
    print("Menu du Jeu:")
    print("1- Jouer")
    print("2- Crédits")
    print("3- Quitter")
    a=int(input())
    if (a==1):
        x=input("\nVoulez-vous jouez seul?o/n\n")
        if (x=="n"):
            x=False
        else:
            x=True
        table(x)
    if(a==2):
        print("\nProjet de CAA réalisé par Rida EL ABED et Kevin ZHANG")
        print("Encadré par Mr.Amir NAKIB et Mr.Jonathan CAILLIEZ")
        print("Université Paris-Est Créteil")
        time.sleep(1)
        print("\nRetour au menu, veuillez patienter...")
        time.sleep(2)
        initialisation()
    if(a==3):
        print("Merci de votre participation!")
        exit
initialisation()
