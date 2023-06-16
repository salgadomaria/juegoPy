import tkinter as tk

class pregunta():
    def __int__(self):
        self

    def contestar(self, pregunta,rta,vida):
        # Crea una nueva ventana
        ventana = tk.Tk()

        # Establece las dimensiones de la ventana
        ventana.geometry("500x200")

        # Centra la ventana en la pantalla
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()
        x = (ancho_pantalla - ventana.winfo_reqwidth()) / 2
        y = (alto_pantalla - ventana.winfo_reqheight()) / 2
        ventana.geometry("+%d+%d" % (x, y))

        # Añade un título a la ventana
        ventana.title("Pregunta:")

        texto = tk.Label(ventana, text=pregunta)
        texto.pack(pady=10)

        # Crea un cuadro de texto donde el usuario pueda ingresar su rta
        usrrta = tk.Entry(ventana)

        # Posiciona el cuadro de texto en la ventana
        usrrta.pack(pady=10)

        # Agrega un botón para enviar el nombre ingresado, cerrar la ventana y guardar el nombre en un archivo de texto
        def enviar_rta():
            finalrta = None
            #print(f"Hola", usrrta.get())
            if rta == usrrta.get():
                finalrta = True
            else:
                finalrta = False
            with open("rta.txt", "w") as archivo:
                archivo.write(f"{finalrta}")
            ventana.destroy()

        boton = tk.Button(ventana, text="Enviar", command=enviar_rta)
        boton.pack(pady=10)

        # Inicia el bucle de la ventana
        ventana.mainloop()





