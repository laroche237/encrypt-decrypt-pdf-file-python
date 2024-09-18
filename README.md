# encrypt-decrypt-pdf-file-python
Ce programme simple écrit en python permet de chiffrer et de déchiffrer des fichiers PDF à l'aide d'un mot de passe.

# Programme de Chiffrement et Déchiffrement de fichier PDF

## Description

Ce programme offre une solution basique et simple pour chiffrer et déchiffrer des fichiers PDF sensibles en utilisant un algorithme de chriffrement symétrique. Il permet aux utilisateurs de sécuriser leurs informations en toute simplicité grâce à une interface utilisateur intuitive ou via des commandes en ligne de commande. Les données sont chiffrées à l'aide de standards éprouvés pour garantir leur confidentialité.

## Pourquoi ce programme est-il utile ?

La protection des données est une priorité absolue pour les entreprises et les professionnels manipulant des informations sensibles. Que vous soyez développeur, administrateur réseau ou professionnel de la sécurité informatique, ce programme vous permet de :
- Chiffrer des fichiers avant de les transmettre ou de les stocker.
- Déchiffrer des données reçues ou archivées de manière sécurisée.
- Préserver l'intégrité des données sensibles face aux accès non autorisés.

Grâce à sa facilité d'utilisation et à son efficacité, ce programme peut être intégré dans des flux de travail existants pour renforcer la sécurité des données.

## Fonctionnalités principales
- Chiffrement de fichiers avec l'algorithme  (clé symétrique).
- Déchiffrement des fichiers chiffrés avec la clé appropriée.
- Des fonctions pour réaliser ces opérations en ligne de commande pour une intégration dans les scripts.
- Interface utilisateur simplifiée pour les utilisateurs non techniques.

## Comment utiliser ce programme ?

### Prérequis
- *Python 3.x* installé sur votre machine
- Bibliothèques Python : PyPDF2

Installez les dépendances requises en utilisant pip :
bash
pip install PyPDF2


### Chiffrement d'un fichier

Pour chiffrer un fichier, utilisez la commande suivante :
Dans le terminal ou bash
python crypter_pdf.py le_chemin_d_acces_jusqu_a_mon fichier_en_clair le_chemin_d_acces_jusqu_a_mon fichier_chiffrer mon_mot_de_passe


### Déchiffrement d'un fichier

Pour déchiffrer un fichier, utilisez cette commande :
Dans le terminal ou bash
python dechiffrer_pdf.py le_chemin_d_acces_jusqu_a_mon fichier_chiffrer le_chemin_d_acces_jusqu_a_mon fichier_dechiffrer mon_mot_de_passe



### Interface utilisateur

Si vous préférez une interface graphique, exécutez le programme principal, qui vous guidera dans les opérations de chiffrement et de déchiffrement via une interface utilisateur simple :
Dans le terminal ou bash
python chiffrer_dechiffrer_pdf.py


## Exemple d'utilisation

Supposons que vous ayez un fichier PDF contenant des informations sensibles (rapport_confidentiel.PDF). Vous souhaitez le chiffrer avant de l'envoyer à un collaborateur. Voici comment vous pouvez procéder :

1. *Chiffrement* : Vous lancez l'application et vous chiffrez votre fichier PDF
   

2. *Transmission* : Envoyez rapport_chiffre.pdf et partagez le mot de passe en toute sécurité par appel par exemple pour qu'il n'y est pas de trace.

3. *Déchiffrement (par le destinataire)* :
 Lancez l'application et déchiffrer le fichier PDF
   

Le fichier original sera restauré une fois déchiffré.

## Contribution

Ce projet est activement maintenu par NYABENG MINEME SANDRA ROCHELLE. Si vous avez des suggestions, des bugs à signaler ou souhaitez contribuer au développement, n'hésitez pas à soumettre des *issues ou des pull requests. J'ai encore pas mal de chose à améliorer!

Je suis également ouvert à la collaboration sur d'autres projets de sécurité informatique ou de cryptographie.

## Contact

Si vous avez besoin d'aide, des questions sur l'utilisation du programme, ou souhaitez simplement échanger à propos de la cryptographie, vous pouvez me contacter à :

- *Email* : nyabengrlle@gmail.com(mailto:nyabengrlle@gmail.com)
- *LinkedIn* : [Mon Profil LinkedIn](https://www.linkedin.com/in/rochelle-nyabeng-4658992a8/)
- *GitHub* : [Mon GitHub](https://github.com/laroche237)


## Auteurs et Mainteneurs

Ce projet est développé et maintenu par NYABENG MINEME SANDRA ROCHELLE. Si vous êtes intéressé à contribuer au projet CONTACTER MOI.
