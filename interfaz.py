
import customtkinter as ctk
import tkinter as tk
from CTkMessagebox import CTkMessagebox
from tkinter import ttk
import re


class AplicacionConPestanas(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Programa Academico")
        self.geometry("1000x800")
        

        # Crear pestañas
        self.tabview = ctk.CTkTabview(self, width=600, height=500)
        self.tabview.pack(padx=20, pady=20)

        self.crear_pestanas()


    def crear_pestanas(self):
        # Crear y configurar las pestañas
        self.tab1 = self.tabview.add("Estudiantes")
        self.tab2 = self.tabview.add("Profesores")

        # Configurar el contenido de la pestaña 1
        self.configurar_pestana1()

        # Configurar el contenido de la pestaña 2
        self.configurar_pestana2()

    

    def configurar_pestana1(self):
        # Dividir la pestaña en dos frames
        frame_formulario = ctk.CTkFrame(self.tab1)
        frame_formulario.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        frame_treeview = ctk.CTkFrame(self.tab1)
        frame_treeview.pack(side="right", fill="both", expand=True, padx=10, pady=10)


        # Formulario nombre
        label_nombre = ctk.CTkLabel(frame_formulario, text="Nombre del Estudiante:")
        label_nombre.pack(pady=6)
        self.entry_nombre = ctk.CTkEntry(frame_formulario)
        self.entry_nombre.pack(pady=8)

        # combo opciones grupo
        label_cantidad=ctk.CTkLabel(frame_formulario, text="Grupo")
        label_cantidad.pack(pady=6)
        opcionesG = ["Opción 1", "Opción 2", "Opción 3"]
        self.comboboxG = ctk.CTkOptionMenu(frame_formulario, values=opcionesG)
        self.comboboxG.pack(pady=5)

        # combo opciones asignaturas
        label_cantidad=ctk.CTkLabel(frame_formulario, text="Asignaturas")
        label_cantidad.pack(pady=6)
        opcionesA = ["Opción 1", "Opción 2", "Opción 3"]
        self.comboboxA = ctk.CTkOptionMenu(frame_formulario, values=opcionesA)
        self.comboboxA.pack(pady=5)

        # combo opciones profesores
        label_cantidad=ctk.CTkLabel(frame_formulario, text="Profesores")
        label_cantidad.pack(pady=6)
        opcionesP = ["Opción 1", "Opción 2", "Opción 3"]
        self.comboboxP = ctk.CTkOptionMenu(frame_formulario, values=opcionesP)
        self.comboboxP.pack(pady=5)
        
        #Boton de ingreso
        self.boton_ingresar=ctk.CTkButton(frame_formulario, text="Ingresar Estudiante")
        self.boton_ingresar.configure(command=self.ingresar_ingrediente)
        self.boton_ingresar.pack(pady=25)

        # Botón para eliminar libro arriba del Treeview
        self.boton_eliminar=ctk.CTkButton(frame_treeview, text="Eliminar Estudiante", fg_color="black", text_color="white")
        self.boton_eliminar.configure(command=self.eliminar_ingrediente)
        self.boton_eliminar.pack(pady=10)

        #Boton de menú
        self.boton_menu=ctk.CTkButton(frame_treeview, text="Generar Menú")
        #self.boton_menu.configure(command=self.ingresar_libro)
        self.boton_menu.pack(side="bottom", fill="y", expand=False, padx=10, pady=10)
        
        
        # Treeview en el segundo frame
        self.tree = ttk.Treeview(frame_treeview, columns=("Estudiante","Asignatura", "Profesor"), show="headings")

        # Encabezado
        self.tree.heading("Estudiante", text="Estudiante")
        self.tree.heading("Asignatura", text="Asignatura")
        self.tree.heading("Profesor", text="Profesor")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        # Ancho de las columnas
        self.tree.column("Estudiante", width=150)
        self.tree.column("Asignatura", width=150)
        self.tree.column("Profesor", width=150)



    def configurar_pestana2(self):
        #Dividir la pestaña en tres frames

        #frame con imágenes
        frame_superior = ctk.CTkFrame(self.tab2)  #deja un frame arriba
        frame_superior.pack(side="top", fill="both", expand=True, padx=0, pady=0)

        frame_tarjetas = ctk.CTkFrame(frame_superior, fg_color="transparent", border_color="black", border_width=2)
        frame_tarjetas.pack(side="left", fill="both", expand=False, padx=10, pady=10)

        #frame con treeview y botones + label
        frame_inferior = ctk.CTkFrame(self.tab2)
        frame_inferior.pack(side="bottom", fill="both", expand=True, padx=0, pady=0)   # deja un frame abajo

        #Este será un frame entre medio de los otros 2 frames, el cual estará en el espacio sobrante del 'frame_inferior'.
        frame_boton = ctk.CTkFrame(self.tab2)  
        frame_boton.pack(fill="both", expand=True, padx=0, pady=5)


        #Boton de generar boleta
        self.boton_boleta=ctk.CTkButton(frame_inferior, text="Generar boleta")
        self.boton_boleta.pack(side="bottom", expand=False, padx=5, pady=15)

        #Boton de eliminar menú
        self.boton_menu=ctk.CTkButton(frame_boton, text="Eliminar Menú")    #este botón estará en el frame de entre medio
        self.boton_menu.configure()
        self.boton_menu.pack(side="right", fill="both", expand=False, padx=5, pady=5)

        #label del total
        self.label_total= ctk.CTkLabel(frame_boton, text="")
        self.label_total.configure(text=f"Total: $")
        self.label_total.pack(side="right", fill="both", padx=10, pady=0)



        # Treeview en el segundo frame
        self.tree2 = ttk.Treeview(frame_inferior, columns=("Nombre","Cantidad", "Precio"), show="headings")

        # Encabezado
        self.tree2.heading("Nombre", text="Nombre del Menú")
        self.tree2.heading("Cantidad", text="Cantidad")
        self.tree2.heading("Precio", text="Precio Unitario")
        self.tree2.pack(expand=True, fill="both", padx=0, pady=0)

        # Ancho de las columnas
        self.tree2.column("Nombre", width=150)
        self.tree2.column("Cantidad", width=150)
        self.tree2.column("Precio", width=150)


    def validar(self, nombre, cantidad):
        if not re.match(r"^[a-zA-Z\s]+$", nombre):
            CTkMessagebox(title="Error de Validación", message="El Nombre debe contener solo letras y espacios.", icon="warning")
            return False
        
        
        
        # Sí todo se cumple, se validaría cada campo
        return True
        

        
    def ingresar_Estudiante(self):
        estudiante = self.entry_nombre.get()
        grupo = self.comboboxG.get()
        profesor = self.comboboxP.get()
        asignatura = self.comboboxA.get()

        # Validar entradas
        if not self.validar(estudiante, grupo, asignatura, profesor):
            return
        
        # Crear una instancia de Ingrediente
        estudiante = Estudiante(nombre)

        # Agregar el ingrediente al stock
        if self.stock.agregar_ingrediente(estudiante):
            self.actualizar_treeview()
        else:
            CTkMessagebox(title="Error", message="El estudiante ya existe en el programa.", icon="warning")


    def eliminar_estudiante(self):
        seleccion = self.tree.selection()
        if not seleccion:
            CTkMessagebox(title="Error", message="Por favor selecciona un estudiante para eliminar.", icon="warning")
            return

        item = self.tree.item(seleccion)
        nombre = item['values'][0]
        

        # Eliminar el ingrediente del stock
        if self.stock.eliminar_ingrediente(nombre):
            self.actualizar_treeview()
        else:
            CTkMessagebox(title="Error", message="El ingrediente no se pudo eliminar.", icon="warning")



    def actualizar_treeview(self):
        # Limpiar el Treeview actual
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Agregar todos los ingredientes del stock al Treeview
        for ingrediente in self.stock.obtener_ingrediente():
            self.tree.insert("", "end", values=(ingrediente.nombre, ingrediente.cantidad))
     





if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = AplicacionConPestanas()
    app.mainloop()
