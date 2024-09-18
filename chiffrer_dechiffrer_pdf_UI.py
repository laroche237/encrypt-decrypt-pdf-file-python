import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import os

def chiffrer_dechiffrer_pdf(input_pdf, output_pdf, password, action):
    #action correspond à chiffrer ou déchiffer
   try:

    #ouvrir le fichier  en mode lecture binaire
      with open(input_pdf, 'rb') as file:
    
    #creer un lecteur
        lecteur = PyPDF2.PdfReader(file)

        # creer un écrivain
        writer = PyPDF2.PdfWriter()

#Chiffrer le PDF
#vérifions s'il est déja chiffré
       
        if action == 'chiffrer': 
            for page_num in range(len(lecteur.pages)):

                writer.add_page(lecteur.pages[page_num])
            #chiffrer le fichier PDF avec un mot de passe
            writer.encrypt(password)

            #Enregister le fichier chiffrer dans un fichier en sortie
            with open(output_pdf, 'wb') as crypted_file:
                writer.write(crypted_file)
                messagebox.showinfo("Succèes","le fichier {input_pdf} a été crypté avec succès dans {output_pdf}.")

        elif action=='dechiffrer':
             #Vérifier si le PDF est chiffré
            if lecteur.is_encrypted:

            #déchiffrer avec le mot de passe fourni
                if lecteur.decrypt(password):

                   #créer un écrivain pour ce fichier
                   writer = PyPDF2.PdfWriter()

                   #ajouter toutes les pages du fichier d'entrée au fichier de sortie 
                for page_num in range(len(lecteur.pages)):
                    #enregistré le fichier déchiffré dans le fichier de sortie
                        with open(output_pdf, 'wb') as decrypted_file:
                           writer.write(decrypted_file)
                           messagebox.showinfo("Succèes",f"le fichier {input_pdf} a été déchiffrer avec succès dans {output_pdf}.")

                else:  messagebox.showinfo("Erreur","le mot de passe est incorrect.")
            else: messagebox.showinfo("Erreur","le fichier PDF n'est pas crypté.") 
   except Exception as e :  messagebox.showinfo("Erreur",str(e))



 #Fonction pour parcourir et sélectionner le fichier PDF 
def parcourir_fichier():
   file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
   if file:
      enter_file.delete(0, tk.END)
      enter_file.insert(0, file)

#fonction appelée lors du clic sur le bouton de chiffrement
def chiffrer_pdf():
   file = enter_file.get()
   password = enter_password.get()
   if file and password : 
      output_file = os.path.splitext(file)[0]+"_chiffrer.pdf"
      chiffrer_dechiffrer_pdf(file, output_file, password, 'chiffrer')
   else :messagebox.showinfo("Erreur","Veuillez entrer le fichier et le mot de passe.")

#fonction appelée lors du clic sur le bouton de dechiffrement
def dechiffrer_pdf():
   file = enter_file.get()
   password = enter_password.get()
   if file and password : 
      output_file = os.path.splitext(file)[0]+"_dechiffrer.pdf"
      chiffrer_dechiffrer_pdf(file, output_file, password, 'dechiffrer')
   else :messagebox.showinfo("Erreur","Veuillez entrer le fichier et le mot de passe.")

#Interface graphique
fenetre = tk.Tk()
fenetre.title("Chiffrage et Dechiffrage PDF")

#Sélection du fichier 
tk.Label(fenetre, text="Fichier PDF :").grid(row=0, column=0, padx=10, pady=10)
enter_file = tk.Entry(fenetre, width=40)
enter_file.grid(row=0, column=1, padx=10, pady=10)
btn_parcourir = tk.Button(fenetre, text="Parcourir ", command=parcourir_fichier)
btn_parcourir.grid(row=0, column=2, padx=10, pady=10)

#Saisie du mot de passe
tk.Label(fenetre, text="Mot de passe : ").grid(row=1, column=0, padx=10, pady=10)
enter_password = tk.Entry(fenetre, width=40, text = "*")
enter_password.grid(row=1, column=1, padx=10, pady=10)

#Bouton pour chiffrer
btn_chiffrer = tk.Button(fenetre, text="Chiffrer", command = chiffrer_pdf)
btn_chiffrer.grid(row=2, column=0, padx=10, pady=10)

#Bouton pour déchiffrer
btn_dechiffrer = tk.Button(fenetre, text="Déchiffrer", command = dechiffrer_pdf)
btn_dechiffrer.grid(row=2, column=1, padx=10, pady=10)     

#lancer la fenêtre 
fenetre.mainloop()

