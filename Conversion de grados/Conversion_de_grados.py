import tkinter as tk # Libreria que me permite trabajar con interfaz grafica

def convertir_a_fahrenheit():
        celsius = float(celsius_entry.get())
        fahrenheit = round(celsius * 9/5 +32, 2)
        result_label.config(text=f"{fahrenheit} Fahrenheit")

def convertir_a_Celsius():
        fahrenheit = float(Fahrenheit_entry.get())
        celsius = round((fahrenheit - 32) * 5/9, 2)
        result_label.config(text= f"{celsius} Celsius") 



ventana = tk.Tk()
ventana.title("Conversiones de temperatura")
ventana.geometry("400x300")
ventana.configure(bg = 'light green') #bg= back graund

label_font = ('Verdana', 10, 'bold') #font = fuente
entry_font = ('Verdana', 12)
button_font = ('Verdana', 10 , 'bold')

tk.Label(ventana, text = "Celsius a Fahrenheit: ", font=label_font,
         bg= 'light green').pack(pady=5)

celsius_entry = tk.Entry(ventana, font=entry_font) #Entry = entrada de datos
celsius_entry.pack(pady=5) #.pack= ponerlo dentro de la ventana

tk.Button(ventana, text="Convertir", font=button_font,
          command=convertir_a_fahrenheit, bg='light blue').pack(pady=5)

tk.Label(ventana, text = "Fahrenheit a Celsius: ", font=label_font,
         bg= 'light green').pack(pady=5)

Fahrenheit_entry = tk.Entry(ventana, font = entry_font)
Fahrenheit_entry.pack(pady=5)

tk.Button(ventana, text="Convertir", font=button_font,
          command=convertir_a_Celsius, bg='light blue').pack(pady=5)


result_label = tk.Label(ventana, text = "Resultado", font=label_font,
                       bg='light green')
result_label.pack(pady=10)

tk.Button(ventana, text="CLEAN", font=button_font,
           bg='light gray').pack(pady=10)


ventana.mainloop()
