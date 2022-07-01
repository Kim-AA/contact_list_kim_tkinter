from tkinter import *
from tkinter import messagebox
from functools import partial
# partial crida funcio amb parametres i guardar en variable

# funcio per sortir del programa
def exit(finestra):
    finestra.destroy()

# funcio per tornar a finestra menu
def volver_menu(finestra):
    finestra.destroy()
    menu()

#:::::::::::::::::::::::::::::::::::::::::::# 
#::::::::::::::::: AFEGIR ::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::# 
def afegir(finestra):
    # funcio per esborrar
    def neteja():
        text_nom.set('')
        text_telf.set('')
        text_email.set('')
        out_afegit.delete("0.0","end")

    # funcio per mostrar el llistat de dades
    def afegeix():
        contacte = []
        v_nom = ent_nom.get()
        contacte.append(v_nom)
        v_telf = ent_telf.get()
        contacte.append(v_telf)
        v_email = ent_email.get()
        contacte.append(v_email)

        # escriure nou contacte a l'arxiu
        with open("agenda.csv", 'a') as doc:
            nou_contacte = ''
            for i in contacte:
                nou_contacte += i + ','
            nou_contacte += '\n'
            doc.write(nou_contacte)  

        #mostra contacte afegit
        out_afegit.insert(0.0, contacte)
       
                        
    # finestra per afegir
    finestra.destroy()
    finestra = Tk()
    finestra.title('::: AFEGIR CONTACTE :::')
    finestra.configure(bg = "black")
    text_nom = StringVar()
    text_telf = StringVar()
    text_email = StringVar()
    volver = partial(volver_menu, finestra)
    sortir = partial(exit, finestra)

    #:::::::::::::LABELS:::::::::::::#  
    lbl_nom = Label(finestra,text='Nom',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_nom.grid(row=0,column=0)
    lbl_telf = Label(finestra,text='Telf',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_telf.grid(row=0,column=1)
    lbl_email = Label(finestra,text='Email',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_email.grid(row=0,column=2)
    
    #:::::::::::::INPUTS:::::::::::::#           
    ent_nom=Entry(finestra,width=10,font=('summer 18 bold'),textvar=text_nom,bg='white')
    ent_nom.grid(row=1,column=0)
    ent_telf=Entry(finestra,width=10,font=('summer 18 bold'),textvar=text_telf,bg='white')
    ent_telf.grid(row=1,column=1)
    ent_email=Entry(finestra,width=15,font=('summer 18 bold'),textvar=text_email,bg='white')
    ent_email.grid(row=1,column=2)

    #::::::::::AFEGIR i NETEJAR::::::::::# 
    btn_afegir = Button(finestra,padx=2,pady=2,text='Afegeix',font=('summer 18 bold'), bg = "green", fg = "white", command = afegeix)
    btn_afegir.grid(row=2,column=1)
    btn_neteja = Button(finestra,padx=2,pady=2,text='Neteja',font=('summer 18 bold'),bg = "black", fg = "white", command = neteja)
    btn_neteja.grid(row=3,column=1)

    #:::::::::::::OUTPUT:::::::::::::#  
    lbl_afegit = Label(finestra,text='Contacte Afegit',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_afegit.grid(row=4,column=1)
    out_afegit = Text(finestra, width = 30, height = 2, font = ('Time 20 bold'), fg = "black")
    out_afegit.grid(row = 5, column = 0, columnspan = 3)

    #::::::::::TORNAR A MENU:::::::::::#
    btn_menu = Button(finestra, padx = 2, pady = 2, text = 'menu', command = volver, bg = 'orange', font = ('summer 18 bold'))
    btn_menu.grid(row = 6, column = 0)

    #:::::::::::BOTO SORTIR::::::::::::#
    btn_sortir = Button(finestra, padx = 2, pady = 2, text = 'sortir', command = sortir, bg = 'red', font = ('summer 18 bold'))
    btn_sortir.grid(row = 6, column = 2)

    # ----- fi afegir ----- #


#:::::::::::::::::::::::::::::::::::::::::::# 
#::::::::::::::::: BUSCAR ::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::# 
def buscar(finestra):
    
    # funcio per esborrar
    def neteja():
        text_nom.set('')
        text_telf.set('')
        text_email.set('')
        out_mostrar.delete("0.0","end")
    
    # funcio per mostrar el llistat de dades
    def busca():
        llista = []
        contactes = []
        num_linies = 0
        
        with open("agenda.csv", 'r') as doc:
            for linea in doc:
                valors = linea.strip().split(',')
                llista.append(valors)
                num_linies += 1
            
            llista_valors = llista[1:num_linies]
            nom, telf, email = llista[0][0:3]
            clau = [nom, telf, email]

            for v in llista_valors:
                d = dict(zip(clau,v))
                contactes.append(d)
        
            for p in contactes:
                #print(p)
                for k,v in p.items():
                    nom = ent_nom.get()
                    telf = ent_telf.get()
                    email = ent_email.get()
                    if nom == v:
                        out_mostrar.insert(0.0, p)
                    elif telf == v:
                        out_mostrar.insert(0.0, p)
                    elif email == v:
                        out_mostrar.insert(0.0, p)
                        #or messagebox
            
                        
    # finestra per buscar
    finestra.destroy()
    finestra = Tk()
    finestra.title('::: BUSCAR CONTACTE :::')
    finestra.configure(bg = "black")
    text_nom = StringVar()
    text_telf = StringVar()
    text_email = StringVar()
    volver = partial(volver_menu, finestra)
    sortir = partial(exit, finestra)

    #:::::::::::::LABELS:::::::::::::#  
    lbl_nom = Label(finestra,text='Nom',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_nom.grid(row=0,column=0)
    lbl_telf = Label(finestra,text='Telf',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_telf.grid(row=0,column=1)
    lbl_email = Label(finestra,text='Email',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_email.grid(row=0,column=2)
    
    #:::::::::::::INPUTS:::::::::::::#           
    ent_nom=Entry(finestra,width=10,font=('summer 18 bold'),textvar=text_nom,bg='white')
    ent_nom.grid(row=1,column=0)
    ent_telf=Entry(finestra,width=10,font=('summer 18 bold'),textvar=text_telf,bg='white')
    ent_telf.grid(row=1,column=1)
    ent_email=Entry(finestra,width=15,font=('summer 18 bold'),textvar=text_email,bg='white')
    ent_email.grid(row=1,column=2)

    #::::::::::BUSCAR i NETEJAR::::::::::# 
    btn_mostra = Button(finestra,padx=2,pady=2,text='Mostra',font=('summer 18 bold'),bg = "green", fg = "white", command = busca)
    btn_mostra.grid(row=2,column=1)
    btn_neteja = Button(finestra,padx=2,pady=2,text='Neteja',font=('summer 18 bold'),bg = "black", fg = "white", command = neteja)
    btn_neteja.grid(row=3,column=1)

    #:::::::::::::OUTPUT:::::::::::::#  
    out_mostrar = Text(finestra, width = 30, height = 2, font = ('Time 20 bold'), fg = "black")
    out_mostrar.grid(row = 4, column = 0, columnspan = 3)

    #::::::::::TORNAR A MENU:::::::::::#
    btn_menu = Button(finestra, padx = 2, pady = 2, text = 'menu', command = volver, bg = 'orange', font = ('summer 18 bold'))
    btn_menu.grid(row = 5, column = 0)

    #:::::::::::BOTO SORTIR::::::::::::#
    btn_sortir = Button(finestra, padx = 2, pady = 2, text = 'sortir', command = sortir, bg = 'red', font = ('summer 18 bold'))
    btn_sortir.grid(row = 5, column = 2)
    
    # ----- fi buscar ----- #

    
#:::::::::::::::::::::::::::::::::::::::::::# 
#:::::::::::::::: LLISTAR ::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::# 
def mostrar(finestra):

    # funcio per mostrar el llistat de dades
    def veure():
        llista = []
        contactes = []
        num_linies = 0
        
        with open("agenda.csv", 'r') as doc:
            #valores = doc.read()
            for linea in doc:
                valors = linea.strip().split(',')
                llista.append(valors)
                num_linies += 1
            
            llista_valors = llista[1:num_linies]
            nom, telf, email = llista[0][0:3]
            clau = [nom, telf, email]
            
            for v in llista_valors:
                d = dict(zip(clau,v))
                contactes.append(d)

                
            for p in contactes:
                print(p)
                for v in p:
                # al fer scroll es descoloca
                # el bucle es repeteix x3
                # cal millorar-ho
                    out_nom.insert(0.0, p[nom]+'\n')
                    out_telf.insert(0.0, p[telf]+'\n')
                    out_email.insert(0.0, p[email]+ '\n')
                
                        
    # finestra per mostrar dades
    finestra.destroy()
    finestra = Tk()
    finestra.title('::: LLISTA DE CONTACTES :::')
    finestra.configure(bg = "black")
    volver = partial(volver_menu, finestra)
    sortir = partial(exit, finestra)

    #:::::::::::::LABELS:::::::::::::#  
    lbl_nom = Label(finestra,text='Nom',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_nom.grid(row=0,column=0,sticky=W)
    lbl_telf = Label(finestra,text='Telf',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_telf.grid(row=0,column=1,sticky=W)
    lbl_email = Label(finestra,text='Email',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_email.grid(row=0,column=2,sticky=W)
    
    #:::::::::::::OUTPUT:::::::::::::#           
    out_nom = Text(finestra, width = 10, height = 5, font = ('Time 20 bold'), fg = "black")
    out_nom.grid(row = 1, column = 0)
    out_telf = Text(finestra, width = 10, height = 5, font = ('Time 20 bold'), fg = "black")
    out_telf.grid(row = 1, column = 1)
    out_email = Text(finestra, width = 10, height = 5, font = ('Time 20 bold'), fg = "black")
    out_email.grid(row = 1, column = 2)

    #::::::::::TORNAR A MENU:::::::::::#
    btn_menu = Button(finestra, padx = 2, pady = 2, text = 'menu', command = volver, bg = 'orange', font = ('summer 18 bold'))
    btn_menu.grid(row = 2, column = 0)

    #:::::::::::BOTO SORTIR::::::::::::#
    btn_sortir = Button(finestra, padx = 2, pady = 2, text = 'sortir', command = sortir, bg = 'red', font = ('summer 18 bold'))
    btn_sortir.grid(row = 2, column = 2)

    veure()
        # ----- fi llistar ----- #


#:::::::::::::::::::::::::::::::::::::::::::# 
#::::::::::::::::: EDITAR ::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::#

# ------ NO HE ACABAT AMB AQUESTA OPCIO -----#
    
def editar(finestra):

    def edita():
        arxiu = 'agenda.csv'

        nom = ent_nom.get()
        nou_nom = ent_nou_nom.get()
        
        with open(arxiu, 'r+') as doc:
            contactes = doc.readlines()
            # ens posicionem a l'inici del document, bit 0
            doc.seek(0)
            for line in contactes:
                if nom not in line:
                    doc.write(line)
                elif nom in line:
                    line.replace(nom, nou_nom)
                    doc.write(line)
            # eliminem la resta de linies que quedin
            doc.truncate()

        box = messagebox.showinfo("INFO", "El contacte s'ha actualitzat")
        finestra.destroy()
        menu()

    # finestra per editar
    finestra.destroy()
    finestra = Tk()
    finestra.title('::: EDITAR CONTACTE :::')
    finestra.configure(bg = "black")
    text_nom = StringVar()
    text_nou_nom = StringVar()
    volver = partial(volver_menu, finestra)
    sortir = partial(exit, finestra)
 

    #:::::::::::::LABELS:::::::::::::#  
    lbl_nom = Label(finestra,text='Nom',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_nom.grid(row=0,column=0)
    
    #:::::::::::::INPUTS:::::::::::::#           
    ent_nom=Entry(finestra,width=10,font=('summer 18 bold'),textvar=text_nom,bg='white')
    ent_nom.grid(row=1,column=0)
    
    ent_nou_nom=Entry(finestra,width=10,font=('summer 18 bold'),textvar=text_nou_nom,bg='white')
    ent_nou_nom.grid(row=2,column=0)

    #:::::::::::::EDITAR:::::::::::::# 
    btn_edita = Button(finestra,padx=2,pady=2,text='Edita',font=('summer 18 bold'),bg = "blue",fg='white', command = edita)
    btn_edita.grid(row=3,column=0)

    #:::::::::::BOTO NETEJA::::::::::::#
    btn_neteja = Button(finestra,padx=2,pady=2,text='Neteja',font=('summer 18 bold'),bg = "black",fg='white')
    btn_neteja.grid(row=4,column=0)

    #::::::::::TORNAR A MENU:::::::::::#
    btn_menu = Button(finestra, padx = 2, pady = 2, text = 'menu', command = volver, bg = 'orange', font = ('summer 18 bold'))
    btn_menu.grid(row = 4, column = 1)

    #:::::::::::BOTO SORTIR::::::::::::#
    btn_sortir = Button(finestra, padx = 2, pady = 2, text = 'sortir', command = sortir, bg = 'red', font = ('summer 18 bold'))
    btn_sortir.grid(row = 4, column = 2)
        
    # ----- fi editar ----- #

#:::::::::::::::::::::::::::::::::::::::::::# 
#:::::::::::::::: ELIMINAR :::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::# 
def eliminar(finestra):

    # esborrar
    def neteja():
        text_nom.set('')
        text_telf.set('')
        text_email.set('')

    # funcio per mostrar el llistat de dades
    def elimina():
        arxiu = 'agenda.csv'
        eliminar = []

        # rebre inputs  i afegir-ho a una llista
        nom = ent_nom.get()
        eliminar.append(nom)
        telf = ent_telf.get()
        eliminar.append(telf)
        email = ent_email.get()
        eliminar.append(email)
            
        with open(arxiu, 'r+') as doc:
            contactes = doc.readlines()
            # ens posicionem a l'inici del document, bit 0
            doc.seek(0)
            for line in contactes:
                for i in eliminar:
                    # si la dada no esta a la linia la escribim
                    if i not in line:
                        doc.write(line)
            # eliminem la resta de linies que quedin
            doc.truncate()

        box = messagebox.showinfo("ELIMINAT", "El contacte s'ha eliminat")
        finestra.destroy()
        menu()
        
            
                        
    # finestra per eliminar
    finestra.destroy()
    finestra = Tk()
    finestra.title('::: ELIMINAR CONTACTE :::')
    finestra.configure(bg = "black")
    text_nom = StringVar()
    text_telf = StringVar()
    text_email = StringVar()
    volver = partial(volver_menu, finestra)
    sortir = partial(exit, finestra)
 

    #:::::::::::::LABELS:::::::::::::#  
    lbl_nom = Label(finestra,text='Nom',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_nom.grid(row=0,column=0)
    lbl_telf = Label(finestra,text='Telf',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_telf.grid(row=0,column=1)
    lbl_email = Label(finestra,text='Email',font=('summer 20 bold'),bg = "black",fg='white')
    lbl_email.grid(row=0,column=2)
    
    #:::::::::::::INPUTS:::::::::::::#           
    ent_nom=Entry(finestra,width=10,font=('summer 18 bold'),textvar=text_nom,bg='white')
    ent_nom.grid(row=1,column=0)
    ent_telf=Entry(finestra,width=10,font=('summer 18 bold'),textvar=text_telf,bg='white')
    ent_telf.grid(row=1,column=1)
    ent_email=Entry(finestra,width=15,font=('summer 18 bold'),textvar=text_email,bg='white')
    ent_email.grid(row=1,column=2)

    #::::::::::ELIMINAR i NETEJAR::::::::::# 
    btn_elimina = Button(finestra,padx=2,pady=2,text='Elimina',font=('summer 18 bold'),bg = "blue",fg='white', command = elimina)
    btn_elimina.grid(row=2,column=1)
    btn_neteja = Button(finestra,padx=2,pady=2,text='Neteja',font=('summer 18 bold'),bg = "black",fg='white', command = neteja)
    btn_neteja.grid(row=3,column=1)


    #::::::::::TORNAR A MENU:::::::::::#
    btn_menu = Button(finestra, padx = 2, pady = 2, text = 'menu', command = volver, bg = 'orange', font = ('summer 18 bold'))
    btn_menu.grid(row = 4, column = 0)

    #:::::::::::BOTO SORTIR::::::::::::#
    btn_sortir = Button(finestra, padx = 2, pady = 2, text = 'sortir', command = sortir, bg = 'red', font = ('summer 18 bold'))
    btn_sortir.grid(row = 4, column = 2)
    
    # ----- fi eliminar ----- #
    
#:::::::::::::::::::::::::::::::::::::::::::# 
#:::::::::::::::::: MENU :::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::#

# menu finestra, finestra principal
def menu():
    menu = Tk()
    menu.geometry("250x260")
    menu.title("AGENDA")
    list = partial(mostrar, menu)
    sortir = partial(exit, menu)
    append = partial(afegir, menu)
    cerca = partial(buscar,menu)
    borrar = partial(eliminar, menu)
    actualitza = partial(editar, menu) 
    # aquesta opcio no esta acabada

    # afegir 
    B1 = Button(menu, text = " AFEGIR ", command = append, activebackground = "#FFBB20", bg = "white", fg = "black", width = 500, font = 'summer', bd = 5)
    # buscar
    B2 = Button(menu, text = " BUSCAR CONTACTE ", command = cerca, activebackground = "#FFBB20", bg = "white", fg = "black", width = 500, font = 'summer', bd = 5)
    # llistar
    B3 = Button(menu, text = " LLISTAR ",  command = list, activebackground = "#FFBB20", bg = "white", fg = "black", width = 500, font = 'summer', bd = 5)
    # editar
    B4 = Button(menu, text = " EDITAR ", command = actualitza, activebackground = "#FFBB20", bg = "white", fg = "black", width = 500, font = 'summer', bd = 5)
    # eliminar
    B5 = Button(menu, text = " ELIMINAR ", command = borrar, activebackground = "#FFBB20", bg = "white", fg = "black", width = 500, font = 'summer', bd = 5)
    # sortir
    B6 = Button(menu, text = "Sortir", command = sortir, activebackground = "red", bg = "white", fg = "black", width = 500, font = 'summer', bd = 5)
    
    # posicio menu
    B1.pack(side = 'top')
    B2.pack(side = 'top')
    B3.pack(side = 'top')
    B4.pack(side = 'top')
    B5.pack(side = 'top')
    B6.pack(side = 'top')
     
    menu.mainloop()

# cridem funcio principal
menu()