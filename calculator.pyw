from builtins import int
from tkinter import *

root = Tk()
#root.geometry("270x200")
root.title("my calculator")
root.config(bg="#6818CF")

frame= Frame(root)
frame.pack()
frame.config(bg="#18CF42")

operacion=""
resultado=0
reset_pantalla=False

#------display--------
displaynum = StringVar()
display = Entry(frame,textvariable=displaynum)
display.pack()
display.grid(row=1,column=1,padx=10,pady=10,columnspan=4,ipady=10)
display.config(bg="black",fg="#18CFCC",justify="right",width=20,font="Arial 15 bold")


#-----pulsaciones teclado------

def numero(num):
    global operacion
    global reset_pantalla

    if reset_pantalla!=False:
        displaynum.set(num)
        reset_pantalla=False
    else:
        displaynum.set(displaynum.get() + num)

#----------funcion operacion-------
def suma(num):

    global operacion
    global resultado
    global reset_pantalla

    if num.count(".")==1:

      resultado+=float(num)
      displaynum.set(resultado)

    else:
        resultado+=int(num)
        displaynum.set(resultado)

    operacion = "suma"
    reset_pantalla=True

num1=0
contador_resta=0

def resta(num):

    global operacion
    global resultado
    global contador_resta
    global num1
    global reset_pantalla

    if contador_resta==0:
            num1=int(num)
            resultado=num1

    else:


         if  contador_resta==1:

            resultado=num1- int(num)

         else:
            resultado=int(resultado) - int(num)

         displaynum.set(resultado)
         resultado=displaynum.get()

    contador_resta+=1
    operacion = "resta"
    reset_pantalla=True


contador_multi=0
def multiplicacion(num):

    global operacion
    global resultado
    global reset_pantalla
    global num1
    global contador_multi


    if contador_multi==0:

        num1 = int(num)
        resultado = num1



    else:
        if contador_multi==1:
            resultado =num1 * int(num)


        else:

            resultado=int(resultado) * int(num)

    displaynum.set(resultado)
    resultado=displaynum.get()
    contador_multi+=1
    operacion = "multiplicacion"
    reset_pantalla=True

contador_div=0

def division(num):
    global contador_div
    global num1

    global resultado
    global reset_pantalla

    if contador_div==0:
        if num.count(".")==1:

            num1 = float(num)
            resultado = num1
        else:
            num1 = int(num)
            resultado = num1


    else:

        if contador_div==1:
            if num.count(".")==1:
                resultado = num1 / float(num)

            else:
                resultado = num1 / int(num)


        else:
            if num.count(".")==1:

                resultado = float(resultado) / float(num)
            else:
                resultado = int(resultado) / int(num)

    displaynum.set(resultado)
    resultado = displaynum.get()
    contador_div+=1

    reset_pantalla = True



#resultado
def result(num):

    global operacion
    global  resultado
    global contador_resta
    global contador_multi
    global contador_div

    if  operacion=="suma":

        if num.count(".")==1:
            displaynum.set(resultado + float(displaynum.get()))
            resultado = 0

        else:
            displaynum.set((resultado + int(displaynum.get())))
            resultado = 0


    elif operacion=="resta":

        if num.count(".") == 1:
            displaynum.set(float(resultado)-float(displaynum.get()))
            resultado = 0
            contador_resta = 0

        else:
            displaynum.set(int(resultado)-int(displaynum.get()))
            resultado = 0
            contador_resta = 0

    elif operacion=="multiplicacion":

        if num.count(".") == 1:
            displaynum.set(float(resultado) * float(displaynum.get()))
            resultado = 0
            contador_multi = 0

        else:
            displaynum.set(int(resultado) * int(displaynum.get()))
            resultado = 0
            contador_multi = 0

    else:

        if num.count(".")==1:
            displaynum.set(float(resultado) / float(displaynum.get()))
            resultado = 0
            contador_div = 0

        else:
            displaynum.set(float(resultado) / int(displaynum.get()))
            resultado = 0
            contador_div = 0







def clear():
    displaynum.set(" ")


def delete(num):

    if num!="":
        displaynum.set("")
    else:
        pass



#----------row1--------

boton7=Button(frame,text="7",width=8,command=lambda : numero("7"))
boton7.grid(row=3,column=1)
boton8=Button(frame,text="8",width=8,command=lambda : numero("8"))
boton8.grid(row=3,column=2)
boton9=Button(frame,text="9",width=8,command=lambda : numero("9"))
boton9.grid(row=3,column=3)
boton_divi=Button(frame,text="÷",width=10,command=lambda : division(displaynum.get()))
boton_divi.grid(row=3,column=4)

#----------row2------------

boton6=Button(frame,text="4",width=8,command= lambda:numero("4"))
boton6.grid(row=4,column=1)
boton5=Button(frame,text="5",width=8,command= lambda : numero("5"))
boton5.grid(row=4,column=2)
boton4=Button(frame,text="6",width=8,command= lambda:numero("6"))
boton4.grid(row=4,column=3)
boton_mult=Button(frame,text="X",width=10,command=lambda: multiplicacion(displaynum.get()))
boton_mult.grid(row=4,column=4)

#----------------row3------------------

boton3=Button(frame,text="1",width=8,command=lambda : numero("1"))
boton3.grid(row=5,column=1)
boton2=Button(frame,text="2",width=8,command=lambda : numero("2"))
boton2.grid(row=5,column=2)
boton1=Button(frame,text="3",width=8,command=lambda : numero("3"))
boton1.grid(row=5,column=3)
boton_resta=Button(frame,text="-",width=10,command=lambda: resta(displaynum.get()))
boton_resta.grid(row=5,column=4)

#-------------row4-----------
botonnegate=Button(frame,text=".",width=8,command=lambda:numero("."))
botonnegate.grid(row=6,column=1)
boton0=Button(frame,text="0",width=8,command=lambda: numero("0"))
boton0.grid(row=6,column=2)
botonigual=Button(frame,text="=",width=8,command=lambda:result(displaynum.get()))
botonigual.grid(row=6,column=3)
boton_equals=Button(frame,text="+",width=10,command=lambda : suma(displaynum.get()))
boton_equals.grid(row=6,column=4)

#------------row clear------------------------
boton_limpiar=Button(frame,text="C",width=8,command=lambda: clear())
boton_limpiar.grid(row=2,column=1)
boton_ce= Button(frame,text="Ce",width=8)
boton_ce.grid(row=2,column=2)
boton_delete=Button(frame,text="Del",width=8,command=lambda:delete(displaynum.get()))
boton_delete.grid(row=2,column=3)
boton_percent=Button(frame,text="%",width=10)
boton_percent.grid(row=2,column=4)


root.mainloop()