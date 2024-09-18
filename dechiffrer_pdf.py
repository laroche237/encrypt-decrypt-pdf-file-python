import sys
import PyPDF2

def dechiffrer_pdf(input_pdf, output_pdf, password):
    #ouvrir le fichier PDF crypté
    with open(input_pdf, 'rb') as file:
        lecteur = PyPDF2.PdfReader(file)

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
                print(f"le fichier {input_pdf} a été déchiffrer avec succès dans {output_pdf}.")

            else: print("le mot de passe est incorrect.")
        else:print("le fichier PDF n'est pas crypté.")
# Utilisation dechiffrer_pdf('document_crypté.pdf', 'document_déchiffrer.pdf', 'mot_de_passe')
if __name__=="__main__":
    #les argumests sont passés par la ligne de commande
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]
    dechiffrer_pdf(input_pdf, output_pdf, password)