from tkinter import *
from tkinter import messagebox

import sys

#COMENTARIOS EN LAS LINEAS 365 Y 387!!!!!
#solo falta agregarle personalización a las ventanas de las preguntas y un botón u otra forma para cerrar el quiz al finalizarlo
#después de contestar la primera pregunta, minimice la ventana principal. luego, al darle next ya esta (ventana principal) no aparece más
def ventanaPrincipal():
    global root
    root = Tk()
    root.geometry("400x400")
    root.title("Inicio de Sesion")
    root.config(bg="grey")
    Label(root, text="Bienvenidos al mejor quiz para programadores", width="300",height="2", font=("calibri",12),bg="Lightgreen").pack()
    Label(root,text="",bg="grey").pack()
    Label(root, text="Escoja una opcion ", width="300",height="2", font=("calibri",12),bg="lightgreen").pack()
    Label(root,text="",bg="grey").pack()
    Label(root,text="",bg="grey").pack()
    Button(root,text="Login",width="30",height="2", command=login,bg="Lightblue").pack()
    Label(root,text="",bg="grey").pack()
    Button(root,text="Registro",width="30",height="2", command=registro,bg="Lightblue").pack()
    
    

    root.mainloop()


def login():
    global ventana_login
    ventana_login = Toplevel(root)
    ventana_login.title("Ventana Login")
    ventana_login.geometry("400x400")
    Label(ventana_login, text="Digite los datos para el login").pack()
    Label(ventana_login,text="").pack()
    global verifica_usuario
    global verifica_clave
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
    global entrada_login_usuario
    global entrada_login_clave
    Label(ventana_login, text="Nombre usaurio (requerido)").pack()
    entrada_login_usuario = Entry(ventana_login,textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login,text="").pack()
    Label(ventana_login, text="Contraseña").pack()
    entrada_login_clave = Entry(ventana_login,textvariable=verifica_clave,show="*")
    #entrada_login_clave.config(show="*")
    entrada_login_clave.pack()
    Label(ventana_login,text="").pack()
    Button(ventana_login, text="Acceder",width="20",height="2",bg="lightblue",command=ventanapreguntas1).pack()
    
    
   
    

usuarios = {}

def registro():
    global ventana_registro
    ventana_registro = Toplevel(root)
    ventana_registro.title("Ventana Registro")
    ventana_registro.geometry("300x300")
    Label(ventana_registro, text="Complete los campos para el registro").pack()
    Label(ventana_registro,text="").pack()
    global nombre_usuario
    global clave
    global entrada_usuario
    global entrada_clave

    nombre_usuario = StringVar()
    clave = StringVar()

    Label(ventana_registro, text="Nombre Usuario (requerido)").pack()
    entrada_usuario = Entry(ventana_registro,textvariable=nombre_usuario)
    entrada_usuario.pack()
    Label(ventana_registro,text="").pack()
    Label(ventana_registro, text="Digite la contraseña").pack()
    entrada_clave = Entry(ventana_registro,textvariable=clave, show="*")
    entrada_clave.pack()
    Label(ventana_registro,text="").pack()
    Label(ventana_registro,text="").pack()
    Button(ventana_registro, text="Acceder",width="10",height="2",bg="lightblue",command=registro_usuario).pack()
   

def registro_usuario():
    usuarios[entrada_usuario.get()] = entrada_clave.get()
    ventana_registro.destroy()
    messagebox.showinfo(message="Usuario creado correctamente", title="Mensaje")

    
def mostrar():

    global mostrar
    if seleccion.get()==1:
        messagebox.showinfo("Correcto","Next para continuar")
    
    elif seleccion.get()==2:
        messagebox.showerror("Incorrecto", "La respuesta es la opción A")

    else:
        messagebox.showerror("Incorrecto", "La respuesta es la opción A")



def ventanapreguntas1():

    global ventanapreguntas1
    ventanapreguntas1 = Toplevel(root)
    ventanapreguntas1.title("Primera pregunta")
    ventanapreguntas1.geometry("400x400")
    ventanapreguntas1.config(bg="lightgreen")
    Label(ventanapreguntas1, text="Que funcion cumple print en python?",width="300",height="2", font=("calibri",12),bg="Lightblue").pack()
    Label(ventanapreguntas1,text="",bg="lightgreen").pack()
    Label(ventanapreguntas1,text="",bg="lightgreen").pack()
    Label(ventanapreguntas1,text="",bg="lightgreen").pack()
    Label(ventanapreguntas1,text="",bg="lightgreen").pack()
    Label(ventanapreguntas1,text="",bg="lightgreen").pack()
    Button(ventanapreguntas1, text="Next",width="20",height="2",bg="lightblue",command=ventanapreguntas2).pack()

    ventana_login.destroy()
    
    global seleccion
    seleccion = IntVar()
    rad1 = Radiobutton(ventanapreguntas1,text='Muestra en pantalla',command=mostrar, variable=seleccion,value=1,bg="lightgreen").place(x=100,y=40)
    
    rad2 = Radiobutton(ventanapreguntas1,text='Almacena una variable',command=mostrar, variable=seleccion, value=2,bg="lightgreen").place(x=100,y=60)
   
    rad3 = Radiobutton(ventanapreguntas1,text='Es un ciclo',command=mostrar,variable=seleccion, value=3,bg="lightgreen").place(x=100,y=80)
    
    ventanapreguntas1.mainloop()
   


def mostrar2():

    global mostrar2
    if seleccion2.get()==1:
        messagebox.showerror("Incorrecto", "La respuesta es la opción B")
    
    elif seleccion2.get()==2:
        messagebox.showinfo("Correcto","Next para continuar")

    else:
        messagebox.showerror("Incorrecto", "La respuesta es la opción C")


def ventanapreguntas2():

    global ventanapreguntas2
    ventanapreguntas2=Toplevel(root)
    ventanapreguntas2.title("Segunda pregunta")
    ventanapreguntas2.geometry("400x400")
    ventanapreguntas2.config(bg="lightgreen")
    Label(ventanapreguntas2, text="Que funcion cumple input en python?",bg="lightblue").pack()
    Label(ventanapreguntas2,text="",bg="lightgreen").pack()
    Label(ventanapreguntas2,text="",bg="lightgreen").pack()
    Label(ventanapreguntas2,text="",bg="lightgreen").pack()
    Label(ventanapreguntas2,text="",bg="lightgreen").pack()
    Label(ventanapreguntas2,text="",bg="lightgreen").pack()
    Button(ventanapreguntas2, text="Next",width="20",height="2",bg="lightblue",command=ventanapreguntas3).pack()

    ventanapreguntas1.destroy()
    
    global seleccion2
    seleccion2 = IntVar()

    rad4 = Radiobutton(ventanapreguntas2,text='Muestra en pantalla',command=mostrar2, variable=seleccion2,bg="lightgreen", value=1).place(x=100,y=40)
    
    rad5 = Radiobutton(ventanapreguntas2,text='Almacena una variable',command=mostrar2, variable=seleccion2,bg="lightgreen", value=2).place(x=100,y=60)
   
    rad6 = Radiobutton(ventanapreguntas2,text='Es un ciclo',command=mostrar2,variable=seleccion2,bg="lightgreen", value=3).place(x=100,y=80)
       
    ventanapreguntas2.mainloop()

def mostrar3():

    global mostrar3
    if seleccion3.get()==1:
        messagebox.showerror("Incorrecto", "La respuesta es la opción C")
    
    elif seleccion3.get()==2:
        messagebox.showerror("Incorrecto","La respuesta es la opción C")

    else:
        messagebox.showinfo("Correcto","Next para continuar")


def ventanapreguntas3():

    global ventanapreguntas3
    ventanapreguntas3=Toplevel(root)
    ventanapreguntas3.title("Tercera pregunta")
    ventanapreguntas3.geometry("400x400")
    ventanapreguntas3.config(bg="lightgreen")
    Label(ventanapreguntas3, text="Que es for y while en python?",bg="lightblue").pack()
    Label(ventanapreguntas3,text="",bg="lightgreen").pack()
    Label(ventanapreguntas3,text="",bg="lightgreen").pack()
    Label(ventanapreguntas3,text="",bg="lightgreen").pack()
    Label(ventanapreguntas3,text="",bg="lightgreen").pack()
    Label(ventanapreguntas3,text="",bg="lightgreen").pack()
    Button(ventanapreguntas3, text="Next",width="20",height="2",bg="lightblue",command=ventanapreguntas4).pack()

    ventanapreguntas2.destroy()
    
    global seleccion3
    seleccion3 = IntVar()

    rad7 = Radiobutton(ventanapreguntas3,text='Muestran en pantalla',command=mostrar3, variable=seleccion3,bg="lightgreen", value=1).place(x=100,y=40)
    
    rad8 = Radiobutton(ventanapreguntas3,text='Almacenan variables',command=mostrar3, variable=seleccion3,bg="lightgreen", value=2).place(x=100,y=60)
   
    rad9 = Radiobutton(ventanapreguntas3,text='Ambos son un ciclo',command=mostrar3,variable=seleccion3,bg="lightgreen", value=3).place(x=100,y=80)
       
    ventanapreguntas3.mainloop()


def mostrar4():

    global mostrar4
    if seleccion4.get()==1:
        messagebox.showerror("Incorrecto", "La respuesta es la opción C")
    
    elif seleccion4.get()==2:
        messagebox.showerror("Incorrecto","La respuesta es la opción C")

    else:
        messagebox.showinfo("Correcto","Next para continuar")
 

def ventanapreguntas4():

    global ventanapreguntas4
    ventanapreguntas4=Toplevel(root)
    ventanapreguntas4.title("Cuarta pregunta")
    ventanapreguntas4.geometry("400x400")
    ventanapreguntas4.config(bg="lightgreen")
    Label(ventanapreguntas4, text="Cuál es la diferencia entre tupla y lista?",bg="lightblue").pack()
    Label(ventanapreguntas4, text="",bg="lightgreen").pack()
    Label(ventanapreguntas4,text="",bg="lightgreen").pack()
    Label(ventanapreguntas4,text="",bg="lightgreen").pack()
    Label(ventanapreguntas4,text="",bg="lightgreen").pack()
    Label(ventanapreguntas4,text="",bg="lightgreen").pack()
    Button(ventanapreguntas4, text="Next",width="20",height="2",bg="lightblue",command=ventanapreguntas5).pack()

    ventanapreguntas3.destroy()
    
    global seleccion4
    seleccion4 = IntVar()

    rad10 = Radiobutton(ventanapreguntas4,text='la lista puede ser editada, pero la tupla no puede ser editada',command=mostrar4,bg="lightgreen", variable=seleccion4, value=1).place(x=50,y=40)
    
    rad11 = Radiobutton(ventanapreguntas4,text='la lista es más lenta, mientras que la tupla es más rápida',command=mostrar4,bg="lightgreen", variable=seleccion4, value=2).place(x=50,y=60)
   
    rad12 = Radiobutton(ventanapreguntas4,text='las dos opciones anteriores son correctas',command=mostrar4,variable=seleccion4,bg="lightgreen", value=3).place(x=50,y=80)
       
    ventanapreguntas4.mainloop()

def mostrar5():

    global mostrar5
    if seleccion5.get()==1:
        messagebox.showinfo("Correcto", "Next para continuar")
    
    elif seleccion5.get()==2:
        messagebox.showerror("Incorrecto","La respuesta es la opción A")

    else:
        messagebox.showerror("Incorrecto","La respuesta es la opción A")
 

def ventanapreguntas5():

    global ventanapreguntas5
    ventanapreguntas5=Toplevel(root)
    ventanapreguntas5.title("Quinta pregunta")
    ventanapreguntas5.geometry("400x400")
    ventanapreguntas5.config(bg="lightgreen")
    Label(ventanapreguntas5, text="Un diccionario en python es...",bg="lightblue").pack()
    Label(ventanapreguntas5, text="",bg="lightgreen").pack()
    Label(ventanapreguntas5,text="",bg="lightgreen").pack()
    Label(ventanapreguntas5,text="",bg="lightgreen").pack()
    Label(ventanapreguntas5,text="",bg="lightgreen").pack()
    Label(ventanapreguntas5,text="",bg="lightgreen").pack()
    Button(ventanapreguntas5, text="Next",width="20",height="2",bg="lightblue",command=ventanapreguntas6).pack()

    ventanapreguntas4.destroy()
    
    global seleccion5
    seleccion5 = IntVar()

    rad13 = Radiobutton(ventanapreguntas5,text='un método para almacenar cualquier tipo de valor',command=mostrar5,bg="lightgreen", variable=seleccion5, value=1).place(x=100,y=40)
    
    rad14 = Radiobutton(ventanapreguntas5,text='una condición',command=mostrar5, variable=seleccion5,bg="lightgreen", value=2).place(x=100,y=60)
   
    rad15 = Radiobutton(ventanapreguntas5,text='ninguna de las anteriores',command=mostrar5,bg="lightgreen",variable=seleccion5, value=3).place(x=100,y=80)
       
    ventanapreguntas5.mainloop()

def mostrar6():

    global mostrar6
    if seleccion6.get()==1:
        messagebox.showinfo("Correcto", "Next para continuar")
    
    elif seleccion6.get()==2:
        messagebox.showerror("Incorrecto","La respuesta es la opción A")

    else:
        messagebox.showerror("Incorrecto","La respuesta es la opción A")
 

def ventanapreguntas6():

    global ventanapreguntas6
    ventanapreguntas6=Toplevel(root)
    ventanapreguntas6.title("Sexta pregunta")
    ventanapreguntas6.geometry("400x400")
    ventanapreguntas6.config(bg="lightgreen")
    Label(ventanapreguntas6, text="Qué es tkinter?",bg="lightblue").pack()
    Label(ventanapreguntas6, text="",bg="lightgreen").pack()
    Label(ventanapreguntas6,text="",bg="lightgreen").pack()
    Label(ventanapreguntas6,text="",bg="lightgreen").pack()
    Label(ventanapreguntas6,text="",bg="lightgreen").pack()
    Label(ventanapreguntas6,text="",bg="lightgreen").pack()
    Button(ventanapreguntas6, text="Next",width="20",height="2",bg="lightblue",command=ventanapreguntas7).pack()

    ventanapreguntas5.destroy()
    
    global seleccion6
    seleccion6 = IntVar()

    rad16 = Radiobutton(ventanapreguntas6,text='es la biblioteca gráfica de Python',command=mostrar6,bg="lightgreen", variable=seleccion6, value=1).place(x=100,y=40)
    
    rad17 = Radiobutton(ventanapreguntas6,text='es la biblioteca gráfica de Java',command=mostrar6, variable=seleccion6,bg="lightgreen", value=2).place(x=100,y=60)
   
    rad18 = Radiobutton(ventanapreguntas6,text='es la biblioteca gráfica de C++',command=mostrar6,variable=seleccion6,bg="lightgreen", value=3).place(x=100,y=80)
       
    ventanapreguntas6.mainloop()

def mostrar7():

    global mostrar7
    if seleccion7.get()==1:
        messagebox.showinfo("Correcto", "Next para continuar")
    
    elif seleccion7.get()==2:
        messagebox.showerror("Incorrecto","La respuesta es la opción A")

    else:
        messagebox.showerror("Incorrecto","La respuesta es la opción A")
 

def ventanapreguntas7():

    global ventanapreguntas7
    ventanapreguntas7=Toplevel(root)
    ventanapreguntas7.title("Séptima pregunta")
    ventanapreguntas7.geometry("400x400")
    ventanapreguntas7.config(bg="lightgreen")
    Label(ventanapreguntas7, text="Cuál fue el primer lenguaje de programación?",bg="lightblue").pack()
    Label(ventanapreguntas7, text="",bg="lightgreen").pack()
    Label(ventanapreguntas7,text="",bg="lightgreen").pack()
    Label(ventanapreguntas7,text="",bg="lightgreen").pack()
    Label(ventanapreguntas7,text="",bg="lightgreen").pack()
    Label(ventanapreguntas7,text="",bg="lightgreen").pack()
    Button(ventanapreguntas7, text="Next",width="20",height="2",bg="lightblue",command=ventanapreguntas8).pack()

    ventanapreguntas6.destroy()
    
    global seleccion7
    seleccion7 = IntVar()

    rad19 = Radiobutton(ventanapreguntas7,text='Fortran',command=mostrar7, variable=seleccion7,bg="lightgreen", value=1).place(x=100,y=40)
    
    rad20 = Radiobutton(ventanapreguntas7,text='Java',command=mostrar7, variable=seleccion7,bg="lightgreen", value=2).place(x=100,y=60)
   
    rad21 = Radiobutton(ventanapreguntas7,text='C#',command=mostrar7,variable=seleccion7,bg="lightgreen", value=3).place(x=100,y=80)
       
    ventanapreguntas7.mainloop()

def mostrar8():

    global mostrar8
    if seleccion8.get()==1:
        messagebox.showerror("Incorrecto", "La respuesta es la opción B")
    
    elif seleccion8.get()==2:
        messagebox.showinfo("Correcto", "Finalizar para acabar el quiz")

    else:
        messagebox.showerror("Incorrecto","La respuesta es la opción B")
 

def ventanapreguntas8():

    global ventanapreguntas8
    ventanapreguntas8=Toplevel(root)
    ventanapreguntas8.title("Última pregunta")
    ventanapreguntas8.geometry("400x400")
    ventanapreguntas8.config(bg="lightgreen")
    Label(ventanapreguntas8, text="Qué función cumple el siguiente codigo?",bg="lightblue").pack()
    Label(ventanapreguntas8, text="",bg="lightgreen").pack()
    Label(ventanapreguntas8,text="name = str(input(Digite su nombre))",bg="lightblue").pack()
    Label(ventanapreguntas8,text="print(name)",bg="lightblue").pack()
    Label(ventanapreguntas8, text="",bg="lightgreen").pack()

    #este botón debe cerrar el programa
    Label(ventanapreguntas8, text="",bg="lightgreen").pack()
    Label(ventanapreguntas8, text="",bg="lightgreen").pack()
    Label(ventanapreguntas8, text="",bg="lightgreen").pack()
    Label(ventanapreguntas8, text="",bg="lightgreen").pack()
    Button(ventanapreguntas8, text="Finalizar",width="20",height="2",bg="lightblue",command=ventanapreguntas9).pack()

    ventanapreguntas7.destroy()
    
    global seleccion8
    seleccion8 = IntVar()

    rad22 = Radiobutton(ventanapreguntas8,text='muestra un nombre aleatorio',command=mostrar8, variable=seleccion8,bg="lightgreen", value=1).place(x=100,y=100)
    
    rad23 = Radiobutton(ventanapreguntas8,text='muestra el nombre que el usuario digito',command=mostrar8, variable=seleccion8,bg="lightgreen", value=2).place(x=100,y=120)
   
    rad24 = Radiobutton(ventanapreguntas8,text='muestra error',command=mostrar8,variable=seleccion8,bg="lightgreen", value=3).place(x=100,y=140)
       
    ventanapreguntas8.mainloop()


def CerrarPrograma():
    sys.exit()
#esta ventana es por mientras, en esta misma se podría crear el fin del quiz 
def ventanapreguntas9():
    ventanapreguntas9=Toplevel(root)
    ventanapreguntas9.title("Fin")
    ventanapreguntas9.geometry("400x400")
    ventanapreguntas9.config(bg="lightgreen")
    Label(ventanapreguntas9, text="GRACIAS POR PARTICIPAR",font=("Arial"),bg="lightblue").pack()
    Label(ventanapreguntas9, text="",bg="lightgreen").pack()
    Label(ventanapreguntas9, text="",bg="lightgreen").pack()
    Label(ventanapreguntas9, text="",bg="lightgreen").pack()
    Label(ventanapreguntas9, text="",bg="lightgreen").pack()
    Label(ventanapreguntas9, text="",bg="lightgreen").pack()
    Label(ventanapreguntas9, text="",bg="lightgreen").pack()
    Label(ventanapreguntas9, text="",bg="lightgreen").pack()
    Label(ventanapreguntas9, text="",bg="lightgreen").pack()
    Label(ventanapreguntas9, text="",bg="lightgreen").pack()
    Button(ventanapreguntas9,text="Cerrar Programa",width="20",height="2",bg="Red",command=CerrarPrograma).pack()
    ventanapreguntas9.mainloop()
    ventanapreguntas8.destroy()




ventanaPrincipal()
