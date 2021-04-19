import tkinter as tk #tkinter er en pakke som jeg gjør alt det visuellet med
from cryptography.fernet import Fernet #en krypterings pakke
import os #os er en pakke som gjør det lettere å gjøre ting med filer

stamme = tk.Tk() #stamme er stammen på det visuelle
stamme.config(bg="#263D41")

consol1 = tk.Entry(stamme,width=60,borderwidth=10,fg="white",bg="#263D42") #her lager jeg en consol
consol2 = tk.Entry(stamme,width=60,borderwidth=10,fg="white",bg="#263D42")

class Kalkukator():

    def kalkuler(tallListe,regnemaate): #selve kalkuleringen

        for lengde in range(len(tallListe)): #går igjennom hvor mange tall det er

            #gjør at alt blir riktig ved at den hopper over det første tallet i listen
            if lengde > 0:
                resultat = eval(str(resultat) + regnemaate +  str(tallListe[lengde])) #eval kan regne sammen et stykke i str
            
            else:
                resultat = tallListe[0]

        return resultat #returnerer Kalkulator.kalkuler som "resultat"

    def knapp_press(nummer): #legger til nummeret i consollen
        current = consol1.get() #får consol1 inputen
        consol1.delete(0,"end") #sletter consol data
        consol1.insert(0,str(current) + str(nummer)) #skriver inn consol data

    def clear(): #clearer loggen
        consol1.delete(0,"end")

        #resetter lister
        tallListe.clear()
        regnemaate_skjekk.clear()

    def metode(regnemet): #får tall og regnemetode
        global regnemaate
        tallListe.append(int(consol1.get())) #tallListe er liste for tallene jeg regner sammen
        regnemaate = regnemet #lagrer metoden i en variabel
        regnemaate_skjekk.append(regnemaate) #legger til regnemåte

        #sørger for at man kan bruke flere regnemåter i ett stykke
        if len(regnemaate_skjekk) > 1:
            if regnemaate_skjekk[0] != regnemaate_skjekk[1]:
                resultat = Kalkukator.kalkuler(tallListe,regnemaate_skjekk[0]) #kalkulerer mellomsteg og lagrer i "resultat"
                tallListe.clear()
                tallListe.append(resultat)
            regnemaate_skjekk.clear()
            regnemaate_skjekk.append(regnemaate)

        consol1.delete(0,"end")

    def erLik(): #erlik
        tallListe.append(int(consol1.get()))
        consol1.delete(0,"end")
        resultat = Kalkukator.kalkuler(tallListe,regnemaate) #kalkulerer
        consol1.insert(0,resultat) #legger til "resultat" i consolen

    def save(operation): #fil bruk

        if operation == "save": #lagrer

            #lager om lagrings filen til en liste 
            with open("save.txt","r") as fil: #åpner en fil som "fil"
                save_res = fil.read() #leser filen
                save_res = save_res.split(",") #splitter filen til en liste

            save_res.append(consol1.get())

            #skriver filen omigjen med ny data
            with open("save.txt","w") as fil:
                for res in save_res:
                    if res != "":
                        fil.write(res + " , ") #skriver i filen

        #viser fil loggen
        elif operation == "log": 
            consol1.delete(0,"end")
            
            with open("save.txt","r") as fil:
                save_res = fil.read()
            consol1.insert(0,save_res)
        
        #sletter logg
        elif operation == "delete":
            with open("save.txt","w") as fil: #åpner filen
                fil.truncate() #sletter dataen i filen
                save_res = []

    def OpenCal(): #åpner det visuellet i kalkulatoren
        global tallListe, regnemaate_skjekk, knapp_1,knapp_2,knapp_3,knapp_4,knapp_5,knapp_6,knapp_7,knapp_8,knapp_9,knapp_0,knapp_add,knapp_minus,knapp_gange,knapp_dele,knapp_erLik,knapp_clear,opennew,knapp_saveRes,knapp_log,knapp_delete,knapp_ophd,knapp_Tab
        #global er at man kan bruke varibalene globalt i koden
        if not os.path.isfile("save.txt"): #leter etter filen "save.txt"
            open("save.txt","w+") #lager filen hvis den ikke finner den
            
        stamme.title("Calculator / BrukerInfo") #tittel

        #variabler
        tallListe = []
        regnemaate_skjekk = []
        opennew = 0

        #calkulator knapper og functioner

        consol1.grid(row=0,column=0,columnspan=3,padx=20,pady=20) #fester konsollen

        #knapper
        knapp_1 = tk.Button(stamme, text="           1           ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.knapp_press(1)) #alt før "command=" er for utseende
        knapp_2 = tk.Button(stamme, text="           2           ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.knapp_press(2)) #"Knapp_press" og "metode" er en function som jeg sender inn ulike verdier til
        knapp_3 = tk.Button(stamme, text="           3           ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.knapp_press(3))
        knapp_4 = tk.Button(stamme, text="           4           ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.knapp_press(4))
        knapp_5 = tk.Button(stamme, text="           5           ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.knapp_press(5))
        knapp_6 = tk.Button(stamme, text="           6           ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.knapp_press(6))
        knapp_7 = tk.Button(stamme, text="           7           ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.knapp_press(7))
        knapp_8 = tk.Button(stamme, text="           8           ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.knapp_press(8))
        knapp_9 = tk.Button(stamme, text="           9           ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.knapp_press(9))
        knapp_0 = tk.Button(stamme, text="           0           ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.knapp_press(0))
        knapp_add = tk.Button(stamme, text="            +            ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.metode("+"))
        knapp_minus = tk.Button(stamme, text="             -            ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.metode("-"))
        knapp_gange = tk.Button(stamme, text="            *           ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.metode("*"))
        knapp_dele = tk.Button(stamme, text="           /            ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.metode("/"))
        knapp_ophd = tk.Button(stamme, text="           x^           ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.metode("**"))
        knapp_erLik = tk.Button(stamme, text="            =            ", padx=50, pady=30,fg="white", bg="#263D42", command= Kalkukator.erLik)
        knapp_clear = tk.Button(stamme, text="            C            ", padx=50, pady=30,fg="white", bg="#263D42", command= Kalkukator.clear)
        knapp_saveRes = tk.Button(stamme, text="Lagre resultat", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.save("save"))
        knapp_log = tk.Button(stamme, text="     vis logg      ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.save("log"))
        knapp_delete = tk.Button(stamme, text="    Slett logg    ", padx=50, pady=30,fg="white", bg="#263D42", command=lambda: Kalkukator.save("delete"))
        knapp_Tab = tk.Button(stamme, text="          Tab          ", padx=50, pady=30,fg="white", bg="#263D42", command= openTab)

        #fester knapper
        knapp_1.grid(row=3,column=0)
        knapp_2.grid(row=3,column=1)
        knapp_3.grid(row=3,column=2)
        knapp_clear.grid(row=3,column=3)

        knapp_4.grid(row=2,column=0)
        knapp_5.grid(row=2,column=1)
        knapp_6.grid(row=2,column=2)
        knapp_minus.grid(row=2,column=3)

        knapp_7.grid(row=1,column=0)
        knapp_8.grid(row=1,column=1)
        knapp_9.grid(row=1,column=2)
        knapp_add.grid(row=1,column=3)

        knapp_Tab.grid(row=0,column=3)

        knapp_0.grid(row=4,column=0)
        knapp_gange.grid(row=4,column=1)
        knapp_dele.grid(row=4,column=2)
        knapp_erLik.grid(row=4,column=3)

        knapp_saveRes.grid(row=5,column=0)
        knapp_log.grid(row=5,column=1)
        knapp_delete.grid(row=5,column=2)
        knapp_ophd.grid(row=5,column=3)

class brukerInfo():

    def login(): #logger deg inn
        #fester functioner
        consol1.grid(row=0,column=1,columnspan=3,padx=20,pady=20)
        passord = tk.Label(stamme, text= "Passord: " ,fg="white", bg="#263D42")

        passord.grid(row=0,column=0)

        #lager knapp til log in eller lage bruker
        if os.path.isfile("logininfo.txt"):
            
            #lager knapper
            knapp_login = tk.Button(stamme, text="     Login     ", padx=50, pady=30,fg="white", bg="#263D42",command=brukerInfo.LogIn)
            knapp_login.grid(row=1,column=1)

        else:
            open("logininfo.txt","w+")#lager fil

            knapp_lagPass = tk.Button(stamme, text="     Lagburker     ", padx=50, pady=30,fg="white", bg="#263D42", command = brukerInfo.lagPassord)
            knapp_lagPass.grid(row=1,column=1)
    
    def lagPassord(): #lager passord får bruker
        passord = consol1.get()
        consol1.delete(0,"end")

        with open("logininfo.txt","w") as fil:
            fil.write(passord) #skriver passord i filen
        
        krypter("logininfo.txt",nokkel) #krypterer filen

        for widget in stamme.winfo_children(): #går igjennom functionene festet til "stammen"
                widget.grid_forget() #sletter functionen

        brukerInfo.openBrukerInf() #starter application
 
    def LogIn(): #Login
        Input = consol1.get()
        consol1.delete(0,"end")

        deKrypter("logininfo.txt",nokkel) #dekrypterer

        with open("logininfo.txt","r") as fil:
            passord = fil.read() #leser og lagrer
        
        krypter("logininfo.txt",nokkel) #krypterer

        if Input == passord: #skjekker om Inputen er lik passordet
            for widget in stamme.winfo_children():
                widget.grid_forget()
            brukerInfo.openBrukerInf()
        
    def openBrukerInf(): #åpner det visuellet i bruker info
        global knapp_saveBrukInf, saveBrukernavn, skrift,knapp_slettinfo,knapp_Tab,brukernavn, passord, savePassord, knapp_visPassord, row

        #lager knapper
        knapp_slettinfo = tk.Button(stamme, text="     slett Info     ", padx=50, pady=30,fg="white", bg="#263D42", command= brukerInfo.slettInfo)
        knapp_saveBrukInf = tk.Button(stamme, text="     save Info     ", padx=50, pady=30,fg="white", bg="#263D42", command= brukerInfo.getInfo)
        knapp_visPassord = tk.Button(stamme, text="   vis Passord   ", padx=50, pady=30,fg="white", bg="#263D42", command= brukerInfo.visPassord)
        brukernavn = tk.Label(stamme, text= "Brukernavn: " ,fg="white", bg="#263D42")
        passord = tk.Label(stamme, text= "Passord: " ,fg="white", bg="#263D42")
        consol1.grid(row=0,column=1,columnspan=3,padx=20,pady=20)
        consol2.grid(row=1,column=1,columnspan=3,padx=20,pady=20)
        brukernavn.grid(row=0,column=0)
        passord.grid(row=1,column=0)
        knapp_Tab.grid(row=0,column=4)
        knapp_saveBrukInf.grid(row=1,column=4)
        knapp_slettinfo.grid(row=2,column=4)
        knapp_visPassord.grid(row=3,column=4)

        row = 2
        #Laster inn og skriver filene
        #leser filene og lagrer det i en liste
        if not os.path.isfile('Brukernavn.txt') and not os.path.isfile('Passord.txt'): #skjekker om filene du må ha er der
            #lager filene du trenger
            open("Brukernavn.txt","w+")
            open("Passord.txt","w+")

            savePassord = []
            saveBrukernavn = []

        if os.stat("Brukernavn.txt").st_size > 0 and os.stat("Passord.txt").st_size > 0: #skjekker lengden på fil
            deKrypter("Brukernavn.txt",nokkel)
            deKrypter("Passord.txt",nokkel)

        #lager om lagrings filen til en liste 
        with open("Brukernavn.txt","r") as fil:
            saveBrukernavn = fil.read()
            saveBrukernavn = saveBrukernavn.split(",")

        with open("Passord.txt","r") as fil:
            savePassord = fil.read()
            savePassord = savePassord.split(",")

        #Krypterer filen
        krypter("Brukernavn.txt",nokkel)
        krypter("Passord.txt",nokkel)

        #skriver brukernavnene
        with open("Brukernavn.txt","r") as fil:
            
            #lager all infoen til "labels" og printer det
            for inf in range(len(saveBrukernavn)): #går igjenom lengden
                
                skrift = tk.Label(stamme, text= saveBrukernavn[inf] ,fg="white", bg="#263D42",padx=50, pady=30,)
                skrift.grid(row=row,column=1)
                row+=1
        row = 2

    def getInfo(): #lagrer infoen i consollen

        #lagrer infoen fra consolen
        brukernavn = str(consol1.get())
        passord = str(consol2.get())
        consol1.delete(0,"end")
        consol2.delete(0,"end")

        #lager det den skal lagre
        bruker = "Brukernavn: " + brukernavn
        passord = "Passord: " + passord

        #legger det til i en liste
        savePassord.append(passord)
        saveBrukernavn.append(bruker)

        #dekrypterer filene
        deKrypter("Brukernavn.txt",nokkel)
        deKrypter("Passord.txt",nokkel)

        #skriver i filene
        with open("Brukernavn.txt","w") as fil:
            for resu in saveBrukernavn:
                if resu != "":
                    fil.write(resu + ",")
        
        with open("Passord.txt","w") as fil:
            for resu in savePassord:
                if resu != "":
                    fil.write(resu + ",")

        #krypterer filene
        krypter("Brukernavn.txt",nokkel)
        krypter("Passord.txt",nokkel)

        #sletter for å opptatere
        for widget in stamme.winfo_children():
            widget.grid_forget()

        brukerInfo.openBrukerInf() #kaller får å opptatere knapper

    def slettInfo(): #sletter lagret data
        global savePassord, saveBrukernavn
        consol1.delete(0,"end")
        consol2.delete(0,"end")

        
        with open("Brukernavn.txt","w") as fil: #åpner filen
            fil.truncate() #sletter dataen i filen
            saveBrukernavn = []
        
        
        with open("Passord.txt","w") as fil: #åpner filen
            fil.truncate() #sletter dataen i filen
            savePassord = []

            for widget in stamme.winfo_children():
                widget.grid_forget()

            brukerInfo.openBrukerInf()
                
    def visPassord(): #viser passord info
        global row, vsPass
        vsPass += 1

        if vsPass < 2:
            for inf in savePassord: #lager skrifter med passord
                skrift = tk.Label(stamme, text= inf ,fg="white", bg="#263D42")
                skrift.grid(row=row,column=2)
                row+=1
            
        else:
            vsPass = 0
            for widget in stamme.winfo_children():
                widget.grid_forget()
            brukerInfo.openBrukerInf()



def openTab(): #skifter "vindu"
    global opennew
    opennew+=1

    #skjuler alle ting festet til stammen
    if opennew >= 2:
        for widget in stamme.winfo_children():
            widget.grid_forget()
        Kalkukator.OpenCal()
    
    else:
        for widget in stamme.winfo_children():
            widget.grid_forget()

        brukerInfo.login()


def lagNokkel(): #Lager en nøkkel for krypteringen
    nokkel = Fernet.generate_key() #lager nøkkel

    #lagrer nøkkelen her
    with open("Nokkel.txt","wb") as fil:
        fil.write(nokkel)
    
def lastNokkel(): #Laster inn nøkkelen
    return open("Nokkel.txt","rb").read()

def krypter(filnavn,nokkel): #kryperer "filnavn"
    Fer = Fernet(nokkel)

    #leser filen
    with open(filnavn,"rb") as fil:
        data = fil.read()
    
    #krypterer filen
    kryptertData = Fer.encrypt(data)

    #skriver om filen
    with open(filnavn,"wb") as fil:
        fil.write(kryptertData)

def deKrypter(filnavn,nokkel): #gjørom "filnavn" tilbake fra kryptering
    Fer = Fernet(nokkel)

    #Leser filen
    with open(filnavn,"rb") as fil:
        kryptertData = fil.read()

    #dekrypterer filen
    deKryptertData = Fer.decrypt(kryptertData)

    #skriver om filen
    with open(filnavn, "wb") as fil:
        fil.write(deKryptertData)

if not os.path.isfile("Nokkel.txt"): #om du ikke har nøkkel, lager den en
    open("Nokkel.txt","w+")
    lagNokkel()

vsPass = 0

nokkel = lastNokkel()
Kalkukator.OpenCal()
tk.mainloop() #looper sånn at jeg kan trykke på knappene.