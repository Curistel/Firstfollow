from tabulate import tabulate
## Ingresar datos
#print("Hallar primeros y siguientes ")
#i=input("Cuantas Reglas tiene su gramatica: ")
#Gr=[]
#for k in range(0,int(i)):
#    R=[]
#    nom=input("Termino izq: ")
#    der=input("Terminos derecha separados por comas y por espacios el interior: ").split(",")
#    R=der
#    R.insert(0,nom)
#    Gr.append(R)
    
## Evaluar gramatica
    
lenguajes={}
#------ ejercicio a

#------ ejercicio x1
#R1=["A","B","A or C"]
#R2=["B","C","B and C"]
#R3=["C","b","( A ) not C"]
#Gr=[R1,R2,R3]

#------ ejercicio x2
#R1=["Q","I ( Q )","I [ Q ]","I"]
#R2=["I","a","f","z"]
#Gr=[R1,R2]

#-----ejercicio 1
#R1=["X","Y","X b Z"]
#R2=["Y","Z","Y a Z"]
#R3=["Z","f","d x e","c Z"]
#Gr=[R1,R2,R3]

#-----ejercicio 2

#R1=["S","x","( S R"]
#R2=["R","; S R",")"]
#Gr=[R1,R2]

#-----ejercicio 3
#R1=["Z","S"]
#R2=["S","w S","A B"]
#R3=["A","x A"]
#R4=["B","y"]
#Gr=[R1,R2,R3,R4]

#-----ejercicio 4
R1=["S","( A )"]
R2=["A","C B"]
R3=["B","; A","E"]
R4=["C","x","S"]
Gr=[R1,R2,R3,R4]

primero=Gr[0][0]

#otros metodos
#------unir arr
def unir(arr):
    pab=""
    for i in range(0,len(arr)):
        pab=pab+arr[i]+" "
    return pab

#------imprimir reglas
def imprimir(Gr):
    for i in range(0,len(Gr)):
        for j in range (1,len(Gr[i])):
            print(Gr[i][0]," -> ",Gr[i][j])

# AMBIGUEDAD

def ambiguedad(Gr):
    countt=0
    for i in range(0,len(Gr)):
        palab=""
        sob=[]
        for j in range (2,len(Gr[i])):
            dos=(Gr[i][j]).split(" ")
            if(palab==""):
                rep=[]
                uno=(Gr[i][1]).split(" ")
                un=uno
                men=len(dos)
                if (len(uno)<len(dos)):
                    men=len(uno)
                for k in range (0,men):
                    if(uno[k]==dos[k]):
                        palab=palab+uno[k]+" "
                        rep.append(uno[k])
                    else:
                        break
                for k in range(0,len(rep)):
                    un.remove(rep[k])
                    dos.remove(rep[k])
                asp=unir(un)
                sob.append(asp)
                asd=unir(dos)
                sob.append(asd)
                
            else:
                rep=[]
                tres=palab.split(" ")
                men=len(dos)
                if (len(tres)<len(dos)):
                    men=len(tres)
                for k in range (0,men):
                    if(tres[k]==dos[k]):
                        dos.pop(k)
                    else:
                        break
                for k in range(0,len(rep)):
                        dos.remove(rep[k])
                asd=unir(dos)
                sob.append(asd)
            
        if(palab!=""):
            Gr[i]=[Gr[i][0],(palab+" "+"P")]
            Gx=["P"]
            for n in range(0,len(sob)):
                if(sob[n]==""):
                    Gx.append("E")
                else:
                    Gx.append(sob[n])
            Gr.insert(i+1,Gx)
            countt=countt+1
    if(countt>0):
        print("La gramatica tiene ambiguedad .... vamos a resolverla ->")
        print("========GRAMATICA sin ambiguedad =========")
        imprimir(Gr)
    else:
        print("No hubo ambiguedad ....")
    
    
# RECURSION
    
def poner(Gr,lenguajes):
    for i in range(0,len(Gr)):
            x=Gr[i][0]
            Gr[i].pop(0)
            lenguajes[x]=Gr[i]        
#------Verificar recursion
def recursion(Gr,lenguajes):
    countt=0
    index=[]
    arr=[]
    for i in range(0,len(Gr)):
        for j in range (1,len(Gr[i])):
            if(len(Gr[i][j])>1):
                prueb=(Gr[i][j]).split(" ")
                if(Gr[i][0]==prueb[0]):
                    countt=countt+1
                    Gx=[]
                    ani=Gr[i][0]+"_"
                    ana=Gr[i][j]
                    for h in range(1,len(Gr[i])):
                        if(h!=j):
                            Gx.append(Gr[i][h]+" "+ani)
                    Gx.insert(0,Gr[i][0])
                    Gr[i]=Gx
                    prueb.pop(0)
                    asd=unir(prueb)
                    Grx =[ani,(asd+ani),"E"]
                    index.append(i+countt)
                    arr.append(Grx)
                    break;
    for i in range(0,len(arr)):
        Gr.insert(index[i],arr[i])
    
    if(countt>0):
        print("La gramatica tiene recursion .... vamos a resolverla ->")
        print("========GRAMATICA sin recursion =========")
        imprimir(Gr)
    else:
        print("No hubo recursion ....")
    
    poner(Gr,lenguajes)
#---
def noTerminales(lenguajes1):
    noTerminales=[]
    for noTerminal in lenguajes1:
        if(str(noTerminal).isupper()):
            noTerminales.append(noTerminal)
    print('Simbolos no Terminales -->',noTerminales)
    return(noTerminales)
def terminales(lenguajes1):
    termi=[]
    for noTerminal in lenguajes1:
        print(noTerminal)
        for terminal in lenguajes1[noTerminal]:
            terminales=terminal.split()
            print(terminales)
            for i in range(0,len(terminales)):
                if(terminales[i].isupper()==False):
                    termi.append(terminales[i])
    print('Simbolos Terminales -->',termi)
    return(termi)
def primeros(lenguajes,terminal,noTerminal):
    primero={}
    for ter in range(0,len(terminal)):
        #print('Primero(',terminal[ter],') = ',terminal[ter])
        primero[terminal[ter]]=[terminal[ter]]
    for note in noTerminal:
        rspta=[]
        x=primeroNoTerminal(note,lenguajes,terminal,rspta)
        primero[note]=x
    return primero
def primeroNoTerminal(noTerminal,lenguajes1,terminales,rspta):
    for x in range(0,len(lenguajes1[noTerminal])):
        elem=lenguajes1[noTerminal][x].split()
        if elem[0] in terminales or elem[0]=='E':
            rspta.append(elem[0])
        else:
            primeroNoTerminal(elem[0],lenguajes1,terminales,rspta)
    return(rspta)
def siguiente(sgtori,noTerminal,lenguaje1,terminales,noTerminales,gen,siguientes1,pri):
    for j in range(0,len(noTerminales)):
        for i in range(0,len(lenguaje1[noTerminales[j]])):
            x=lenguaje1[noTerminales[j]][i].split()
            if(noTerminal== primero and ('$'not in gen)):
                gen.append('$')
            if noTerminal in x:
                indice=x.index(noTerminal)
                if((indice+1)==len(x)):
                    if noTerminal!=noTerminales[j]:
                        try:
                            for h in range(0,len(siguientes1[noTerminales[j]])):
                                if siguientes1[noTerminales[j]][h] not in gen:
                                    gen.append(siguientes1[noTerminales[j]][h])
                        except KeyError:
                            print(' ')
                    #siguiente(noTerminales[j],lenguaje1,terminales,noTerminales,gen)
                else:
                    if(str(x[indice+1]) in terminales):
                        for k in range(0,len(pri[x[indice+1]])):
                           gen.append(pri[x[indice+1]][k])  
                    else:
                        if('E'in pri[str(x[indice+1])]):
                            for k in range(0,len(pri[x[indice+1]])):
                                if pri[x[indice+1]][k] not in gen:
                                    gen.append(pri[x[indice+1]][k])
                            gen.remove('E')
                            siguiente(sgtori,x[indice+1],lenguajes,terminales,noTerminales,gen,siguientes1,pri)
                        else:
                            gen.append(pri[str(x[indice+1])])
    
    if sgtori==noTerminal:
        siguientes1[noTerminal]=gen
    return siguientes1

def tabla(pri,sig,lenguaje,terminal):
    lengua=lenguaje
    tabla=[]
    #crear matrix con error
    for i in range(0,len(sig)):
        fila=[]
        for j in range(0,len(terminal)):
            fila.append("error")
        tabla.append(fila)
    cont=0
    for letra in pri:
        if(str(letra).isupper()):
            inte=pri[letra]
            pues=False
            for i in range(0,len(inte)):
                for k in range(0,len(terminal)):
                    
                    if(terminal[k]==inte[i]):
                        a=lengua[letra]
                        if(len(a)>1):
                            tabla[cont][k]=lengua[letra][0]
                            lengua[letra].pop(0)
                        else:
                            tabla[cont][k]=lengua[letra][0]
                if(inte[i]=="E"):
                    pues=True
            if pues:
                intep=sig[letra]
                for i in range(0,len(intep)):
                    for k in range(0,len(terminal)):
                        if(terminal[k]==intep[i]):
                            tabla[cont][k]="E"
                            tabla[cont][len(terminal)-1]="E"
            cont=cont+1
    return tabla

def cadenaok(cadena,tabla,ter,noter):
    pila=[]
    pila.append(primero)
    cadenita=cadena
    t=0
    huboe=0
    try:
        while(t==0):
            if cadena[0] in ter:
                ind=ter.index(cadena[0])
                if pila[0] in noter:
                    ind2= noter.index(pila[0])
                    if(tabla[ind2][ind]=="error"):
                        print(pila," $","  |  ", cadenita,' $',"  |  ",tabla[ind2][ind])
                        huboe=huboe+1
                        t=1
                    else:
                        print(pila," $","  |  ", cadenita,' $',"  |  ",pila[0],"  ->  ",tabla[ind2][ind])
                        pila.pop(0)
                        if (len(tabla[ind2][ind])>1):
                            nep=(tabla[ind2][ind]).split(" ")
                            nep=nep[::-1]
                            for i in range(0,len(nep)):
                                pila.insert(0, nep[i])
                        else:
                            if (tabla[ind2][ind]!="E"):
                                pila.insert(0,tabla[ind2][ind])
                            #pila.append(tabla[ind2][ind])
                    
                else:
                    print(pila," $","  |  ", cadenita,' $',"  |  ","coincide")
                    cadenita.pop(0)
                    pila.pop(0)
            else:
                print(pila," $","  |  ", cadenita,' $',"  |  ","error")
                print("Existe error de sintaxis")
                break
    except:
        if(len(pila)==0):
            print(pila," $","  |  ",' $',"  |  ","correcto")
        else:
            print(pila," $","  |  ", cadenita,' $',"  |  ","error")
            huboe=huboe+1
            
    if (huboe ==0 and len(pila)==0):
        print("La cadena es válida para esta gramática")
    else:
        print("La cadena no es valida para esta gramática")
                       
def sgte(lenguaje):
    print('|---------------------LENGUAJE--------------------!')
    for letra in lenguaje:
        print(letra,' --> ',lenguaje[letra])
    terminal=terminales(lenguajes)
    noterminal=noTerminales(lenguajes)
    siguientes={}
    gen=[]
    pri=primeros(lenguajes,terminal,noterminal)
    print('----------------PRIMEROS--------------')
    for letra in pri:
        print('Primero (',letra,') --> ',pri[letra])
    for i in range(0,len(noterminal)):
        siguientes=siguiente(noterminal[i],noterminal[i],lenguajes,terminal,noterminal,gen,siguientes,pri)
        gen=[]
    print('---------------SIGUIENTES-------------')
    for letra in siguientes:
        print('Siguiente (',letra,') --> ',siguientes[letra])
    #pa la tablaaa
    terminal.append('$')
    teibol=tabla(pri,siguientes,lenguaje, terminal)
    print('---------------TABLA------------------')
    print(tabulate(teibol, headers=terminal, showindex=noterminal,tablefmt='orgtbl'))
    print('---------------CADENA-----------------')
    #cadena="( x ; x ; x ; x )"
    #cadena="( x ; x ; x )"
    cadena="( x ; x )"
    print("La cadena es: ",cadena)
    print(" PILA          |    CADENA         | ACCION      ")
    cadena=cadena.split(' ')
    cadenaok(cadena,teibol,terminal,noterminal)
    
print("========GRAMATICA INICIAL =========")
imprimir(Gr)
print(" **** ")
ambiguedad(Gr)
print(" **** ")
recursion(Gr,lenguajes)
print(" **** ")
sgte(lenguajes)



    

                           
    
                    
                
        
    
