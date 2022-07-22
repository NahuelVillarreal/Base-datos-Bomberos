from tkinter import *
from tkinter import messagebox
import sqlite3

contador=0
mats = []
noms = []
aps = []
jes = []
cars = []
brs = []
coms = []

#-----------------------------------funcionesbasedatos----------------------------------
def conectar():
    try:
        conex=sqlite3.connect("Base de Datos Bomberil")
        cursor=conex.cursor()
        cursor.execute("CREATE TABLE BOMBEROS (MATRICULA VARCHAR UNIQUE, NOMBRE VARCHAR, APELLIDO VARCHAR, JERARQUIA VARCHAR,"
                       " CARGO VARCHAR, BRAVO VARCHAR(3), COMENTARIOS VARCHAR)")
        conex.close()
        messagebox.showinfo(title="Aviso", message="Se ha creado la Base de Datos con exito.")

    except sqlite3.OperationalError:
        messagebox.showinfo(title="Atencion", message="Ya hay una base de datos existente.")

def borrar():
    matricula.set("")
    nombre.set("")
    apellido.set("")
    jerarquia.set("")
    cargo.set("")
    bravo.set("")
    comentarioEntry.delete("1.0","end")

def crear():
    try:
        conex=sqlite3.connect("Base de Datos Bomberil")
        cur=conex.cursor()
        mat=(matricula.get()).upper()
        nom=(nombre.get()).upper()
        ap=(apellido.get()).upper()
        je=(jerarquia.get()).upper()
        car=(cargo.get()).upper()
        br=bravo.get()
        com=(comentarioEntry.get("1.0","end")).upper()
        if mat!="":
            cur.execute("INSERT INTO BOMBEROS VALUES (?,?,?,?,?,?,?)", (mat, nom, ap, je, car, br, com))
            conex.commit()
        else:
            messagebox.showerror(title="Error", message="Rellene al menos el campo de 'Matrícula'")
        conex.close()
        messagebox.showinfo(title="Aviso", message="El bombero ha sido creado con éxito.")
    except sqlite3.OperationalError:
        messagebox.showwarning(title="Error", message="No está creada la Base de Datos.")
    except sqlite3.IntegrityError:
        messagebox.showwarning(title="Error", message="La matrícula ya se encuentra registrada en la base de datos.")

def opcion():
    if opcion.get()==1:
        opcion.set(1)
    elif opcion.get()==2:
        opcion.set(2)
    elif opcion.get()==3:
        opcion.set(3)
    elif opcion.get()==4:
        opcion.set(4)
    elif opcion.get()==5:
        opcion.set(5)
    elif opcion.get()==6:
        opcion.set(6)

def leersinex():
    global opcion, noms, aps, jes, cars, brs, coms
    conex=sqlite3.connect("Base de Datos Bomberil")
    cur=conex.cursor()

    mat=(matricula.get()).upper()
    nom=(nombre.get()).upper()
    ap=(apellido.get()).upper()
    je=(jerarquia.get()).upper()
    car=(cargo.get()).upper()
    br=bravo.get()
    com=(comentarioEntry.get("1.0","end")).upper()

    if opcion.get()==1:
        cur.execute("SELECT * FROM BOMBEROS where MATRICULA=:matricula", {"matricula": mat})
        busqueda=cur.fetchall()
        conex.close()

        matricula.set(busqueda[0][0])
        nombre.set(busqueda[0][1])
        apellido.set(busqueda[0][2])
        jerarquia.set(busqueda[0][3])
        cargo.set(busqueda[0][4])
        bravo.set(busqueda[0][5])
        comentarioEntry.delete("1.0","end")
        comentarioEntry.insert(1.0, busqueda[0][6])

    elif opcion.get()==2:
        cur.execute("SELECT * FROM BOMBEROS where NOMBRE=:nombre", {"nombre": nom})
        busqueda = cur.fetchall()
        conex.close()

        if len(busqueda)>1:
            botonder.config(state=NORMAL)
            botonizq.config(state=NORMAL)

        for i in busqueda:
            mats.append(i[0])
            noms.append(i[1])
            aps.append(i[2])
            jes.append(i[3])
            cars.append(i[4])
            brs.append(i[5])
            coms.append(i[6])

        matricula.set(mats[0])
        nombre.set(noms[0])
        apellido.set(aps[0])
        jerarquia.set(jes[0])
        cargo.set(cars[0])
        bravo.set(brs[0])
        comentarioEntry.delete("1.0","end")
        comentarioEntry.insert(1.0, coms[0])

    elif opcion.get()==3:
        cur.execute("SELECT * FROM BOMBEROS where APELLIDO=:apellido", {"apellido": ap})
        busqueda = cur.fetchall()
        conex.close()

        if len(busqueda)>1:
            botonder.config(state=NORMAL)
            botonizq.config(state=NORMAL)

        for i in busqueda:
            mats.append(i[0])
            noms.append(i[1])
            aps.append(i[2])
            jes.append(i[3])
            cars.append(i[4])
            brs.append(i[5])
            coms.append(i[6])

        matricula.set(mats[0])
        nombre.set(noms[0])
        apellido.set(aps[0])
        jerarquia.set(jes[0])
        cargo.set(cars[0])
        bravo.set(brs[0])
        comentarioEntry.delete("1.0","end")
        comentarioEntry.insert(1.0, coms[0])

    elif opcion.get()==4:
        cur.execute("SELECT * FROM BOMBEROS where JERARQUIA=:jerarquia", {"jerarquia": je})
        busqueda = cur.fetchall()
        conex.close()

        if len(busqueda)>1:
            botonder.config(state=NORMAL)
            botonizq.config(state=NORMAL)

        for i in busqueda:
            mats.append(i[0])
            noms.append(i[1])
            aps.append(i[2])
            jes.append(i[3])
            cars.append(i[4])
            brs.append(i[5])
            coms.append(i[6])

        matricula.set(mats[0])
        nombre.set(noms[0])
        apellido.set(aps[0])
        jerarquia.set(jes[0])
        cargo.set(cars[0])
        bravo.set(brs[0])
        comentarioEntry.delete("1.0","end")
        comentarioEntry.insert(1.0, coms[0])

    elif opcion.get()==5:
        cur.execute("SELECT * FROM BOMBEROS where CARGO=:cargo", {"cargo": car})
        busqueda = cur.fetchall()
        conex.close()

        if len(busqueda)>1:
            botonder.config(state=NORMAL)
            botonizq.config(state=NORMAL)

        for i in busqueda:
            mats.append(i[0])
            noms.append(i[1])
            aps.append(i[2])
            jes.append(i[3])
            cars.append(i[4])
            brs.append(i[5])
            coms.append(i[6])

        matricula.set(mats[0])
        nombre.set(noms[0])
        apellido.set(aps[0])
        jerarquia.set(jes[0])
        cargo.set(cars[0])
        bravo.set(brs[0])
        comentarioEntry.delete("1.0","end")
        comentarioEntry.insert(1.0, coms[0])

    elif opcion.get()==6:
        cur.execute("SELECT * FROM BOMBEROS where BRAVO=:bravo", {"bravo": br})
        busqueda = cur.fetchall()
        conex.close()

        if len(busqueda)>1:
            botonder.config(state=NORMAL)
            botonizq.config(state=NORMAL)

        for i in busqueda:
            mats.append(i[0])
            noms.append(i[1])
            aps.append(i[2])
            jes.append(i[3])
            cars.append(i[4])
            brs.append(i[5])
            coms.append(i[6])

        matricula.set(mats[0])
        nombre.set(noms[0])
        apellido.set(aps[0])
        jerarquia.set(jes[0])
        cargo.set(cars[0])
        bravo.set(brs[0])
        comentarioEntry.delete("1.0","end")
        comentarioEntry.insert(1.0, coms[0])

    else:
        messagebox.showwarning(title="Error", message="Seleccione el filtro para la búsqueda.")

def leer():
    try:
        leersinex()
    except:
        messagebox.showerror(title="Error", message="El bombero no se encuentra en la base de datos.")

def eliminar():
    conex=sqlite3.connect("Base de Datos Bomberil")
    cur=conex.cursor()
    mat = (matricula.get()).upper()
    cur.execute("SELECT * FROM BOMBEROS where MATRICULA=:matricula", {"matricula": mat})
    busqueda = cur.fetchall()
    cur.execute("DELETE from BOMBEROS where MATRICULA=:matricula", {"matricula": mat})
    conex.commit()
    conex.close()
    if busqueda==[]:
        messagebox.showinfo(title="Aviso", message="El bombero no se encuentra en la base de datos.")
    else:
        messagebox.showinfo(title="Aviso", message="El bombero fue eliminado de la base de datos con éxito.")
        borrar()

def actualizar():
    conex=sqlite3.connect("Base de Datos Bomberil")
    cur=conex.cursor()
    mat=matricula.get()
    cur.execute("UPDATE BOMBEROS SET NOMBRE=:nombre, APELLIDO=:apellido, JERARQUIA=:jerarquia, CARGO=:cargo,"
                "BRAVO=:bravo, COMENTARIOS=:comentarios where MATRICULA=:matricula",
                {"matricula":mat, "nombre":nombre.get().upper(), "apellido":apellido.get().upper(),
                 "jerarquia":jerarquia.get().upper(), "cargo":cargo.get().upper(), "bravo":bravo.get().upper(),
                "comentarios":comentarioEntry.get("1.0","end")})


    conex.commit()
    conex.close()


n=0
def desplazamientoder():
    global n, noms, aps, jes, cars, brs, coms
    try:
        if n==len(noms)-1:
            pass
        else:
            n+=1
            matricula.set(mats[n])
            nombre.set(noms[n])
            apellido.set(aps[n])
            jerarquia.set(jes[n])
            cargo.set(cars[n])
            bravo.set(brs[n])
            comentarioEntry.delete("1.0", "end")
            comentarioEntry.insert(1.0, coms[n])
    except:
        pass

def desplazamientoizq():
    global n, noms, aps, jes, cars, brs, coms
    try:
        if n==0:
            pass
        else:
            n-=1
            matricula.set(mats[n])
            nombre.set(noms[n])
            apellido.set(aps[n])
            jerarquia.set(jes[n])
            cargo.set(cars[n])
            bravo.set(brs[n])
            comentarioEntry.delete("1.0", "end")
            comentarioEntry.insert(1.0, coms[n])
    except:
        pass

#----------------------------interfaz grafica------------------------------------------------------------
root=Tk()
root.title("Base de Datos Bomberil")
root.resizable(0,0)
root.geometry("360x480+400+100")
barramenu=Menu(root)
root.config(menu=barramenu)
frame=Frame(root)
frame.pack()
root.iconbitmap("logoabvpa.ico")

matricula=StringVar()
nombre=StringVar()
apellido=StringVar()
jerarquia=StringVar()
cargo=StringVar()
bravo=StringVar()

matriculaEntry=Entry(frame, width=27, textvariable=matricula).grid(row=0, column=1, columnspan=5, padx=5, pady=5, ipadx=5, ipady=5)
nombreEntry=Entry(frame, width=27, textvariable=nombre).grid(row=1, column=1, columnspan=5, padx=5, pady=5, ipadx=5, ipady=5)
apellidoEntry=Entry(frame, width=27, textvariable=apellido).grid(row=2, column=1, columnspan=5, padx=5, pady=5, ipadx=5, ipady=5)
jerarquiaEntry=Entry(frame, width=27, textvariable=jerarquia).grid(row=3, column=1, columnspan=5, padx=5, pady=5, ipadx=5, ipady=5)
cargoEntry=Entry(frame, width=27, textvariable=cargo).grid(row=4, column=1, columnspan=5, padx=5, pady=5, ipadx=5, ipady=5)
bravoEntry=Entry(frame, width=27, textvariable=bravo).grid(row=5, column=1, columnspan=5, padx=5, pady=5, ipadx=5, ipady=5)
comentarioEntry=Text(frame, height=10, width=21)
comentarioEntry.grid(row=6, column=1, columnspan=5, padx=5, pady=5, ipadx=5, ipady=5)
scrollbar=Scrollbar(frame, command=comentarioEntry.yview)
scrollbar.grid(row=6, column=5, pady=10, sticky="NSW")
comentarioEntry.config(yscrollcommand=scrollbar.set)

baseMenu=Menu(barramenu, tearoff=0)
baseMenu.add_command(label="Crear", command=conectar)
baseMenu.add_separator()
baseMenu.add_command(label="Salir", command=root.destroy)

borrarMenu=Menu(barramenu,tearoff=0)
borrarMenu.add_command(label="Borrar", command=borrar)

crudMenu=Menu(barramenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Eliminar", command=eliminar)

acercaMenu=Menu(barramenu, tearoff=0)
acercaMenu.add_command(label="Licencia")

barramenu.add_cascade(label="Base de Datos", menu=baseMenu)
barramenu.add_cascade(label="Edición", menu=borrarMenu)
barramenu.add_cascade(label="CRUD", menu=crudMenu)
barramenu.add_cascade(label="Acerca de", menu=acercaMenu)

matriculaLabel=Label(frame, text="Matrícula:").grid(row=0, column=0, columnspan=2, padx=5, pady=5, ipadx=5, ipady=5)
nombreLabel=Label(frame, text="Nombre:").grid(row=1, column=0, columnspan=2, padx=5, pady=5, ipadx=5, ipady=5)
apellidoLabel=Label(frame, text="Apellido:").grid(row=2, column=0, columnspan=2, padx=5, pady=5, ipadx=5, ipady=5)
jerarquiaLabel=Label(frame, text="Jerarquía:").grid(row=3, column=0, columnspan=2, padx=5, pady=5, ipadx=5, ipady=5)
cargoLabel=Label(frame, text="Cargo:").grid(row=4, column=0, columnspan=2, padx=5, pady=5, ipadx=5, ipady=5)
bravoLabel=Label(frame, text="N° Bravo").grid(row=5, column=0, columnspan=2, padx=5, pady=5, ipadx=5, ipady=5)
comentarioLabel=Label(frame, text="Comentarios:").grid(row=6, columnspan=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)

botonCrear=Button(frame, text="Crear", command=crear).grid(row=7, column=2, padx=5, pady=5, ipadx=5, ipady=5)
botonLeer=Button(frame, text="Leer", command=leer).grid(row=7, column=3, padx=5, pady=5, ipadx=5, ipady=5)
botonActualizar=Button(frame, text="Actualizar", command=actualizar).grid(row=7, column=4, padx=5, pady=5, ipadx=5, ipady=5)
botonBorrar=Button(frame, text="Borrar", command=eliminar).grid(row=7, column=5, padx=5, pady=5, ipadx=5, ipady=5)

opcion=IntVar()
Radiobutton(frame, variable=opcion, value=1, command=opcion).grid(row=0, column=5)
Radiobutton(frame, variable=opcion, value=2, command=opcion).grid(row=1, column=5)
Radiobutton(frame, variable=opcion, value=3, command=opcion).grid(row=2, column=5)
Radiobutton(frame, variable=opcion, value=4, command=opcion).grid(row=3, column=5)
Radiobutton(frame, variable=opcion, value=5, command=opcion).grid(row=4, column=5)
Radiobutton(frame, variable=opcion, value=6, command=opcion).grid(row=5, column=5)

botonizq=Button(frame, text="<=", state=DISABLED, command=lambda:desplazamientoizq())
botonizq.grid(row=7, column=0, padx=5, pady=5, ipadx=5, ipady=5)
botonder=Button(frame, text="=>", state=DISABLED, command=lambda:desplazamientoder())
botonder.grid(row=7, column=1, padx=5, pady=5, ipadx=5, ipady=5)

root.mainloop()


