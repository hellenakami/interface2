from tkinter import *

#criar a função para gerar arquivo .txt
def save_data():
    fileD = open("entregas.txt" , "a")
    fileD.write("Depósito:\n")
    fileD.write("%s\n"%depot.get())
    #descrição
    fileD.write("Descrição:\n")
    fileD.write("%s\n"%description.get())
    #Endereço
    fileD.write("Endereço\n:")
    fileD.write("%s\n"%address.get("1.0", END))
    #apagar os campos
    depot.delete(0,END)
    description.get()
    description.delete(0,END)
    address.delete("1.0",END)
    
#criando a interface gráfica
app = Tk()
app.title("Aula 22")
app.geometry("400x300+100+100")

#campo entry
Label(app, text="Depósito:").pack()
depot = Entry(app)
depot.pack()

Label(app, text="Descrição").pack()
description = Entry(app)
description.pack()

#campo text
Label(app, text="Endereço").pack()
address = Text(app,height=5, width=40)
address.pack()

#criando  botão
Label(app, text="").pack()
Button(app, text="Salvar", command=save_data).pack()

app.mainloop()