import sys
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter

def crypter_pdf(input_pdf, output_pdf, password):
    #ouvrir le fichier  en mode lecture binaire
    with open(input_pdf, 'rb') as file:

        #creer un lecteur
        lecteur = PyPDF2.PdfReader(file)

        # creer un écrivain
        writer = PyPDF2.PdfWriter()

        #Ajouter toutes les pages du fichier
        for page_num in range(len(lecteur.pages)):

            writer.add_page(lecteur.pages[page_num])

            #chiffrer le fichier PDF avec un mot de passe
            writer.encrypt(password)

            #Enregister le fichier chiffrer dans un fichier en sortie
            with open(output_pdf, 'wb') as crypted_file:
                writer.write(crypted_file)
                print(f"le fichier {input_pdf} a été crypté avec succès dans {output_pdf}.")

 #Utilisation crypter_pdf('document.pdf', 'document_crype.pdf', 'mot_de_passe')
if __name__=="__main__":
    #les argumests sont passés par la ligne de commande
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]
    crypter_pdf(input_pdf, output_pdf, password)