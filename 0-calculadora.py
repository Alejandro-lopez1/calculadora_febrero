import tkinter as tk 
import ast

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculadora Básica')

        #variable para almacenar la expresión
        self.expresion = tk.StringVar()

        #pantalla
        pantalla = tk.Entry(root, textvariable=self.expresion, font=('Arial', 14), bd=10, insertwidth=4, width=14, justify='right')
        pantalla.grid(row=0, column=0, columnspan=4)

        #botones
        botones = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', 'C', '=', '+'
        ]

        #agregar botones a la interfaz
        row_val = 1
        col_val = 0
        for boton_texto in botones:
            tk.Button(root, text=boton_texto, font=('Arial', 14), command=lambda x=boton_texto: self.presionar_boton(x)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def presionar_boton(self, valor):
        if valor == 'C':
            self.expresion.set('')
        elif valor == '=':
            try:
                resultado = eval(self.expresion.get())
                self.expresion.set(str(resultado))
            except Exception as e:
                self.expresion.set('Error: ' + str(e))
        else:
            current_expresion = self.expresion.get()
            new_expresion = current_expresion + str(valor)
            self.expresion.set(new_expresion)

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()