# P4-Tournoi_echec
## Objet
>ce projet concerne un outil de gestion d'un tournoi d'échec offline. Il a été créé pour remplacer un outil ayant les 
mêmes objectifs mais fonctionnant online, mais qui ne donnait pas satisfaction en cas de coupure de réseaux.

## Prérequis
### Version de Python et pip
- Python 3.8 ou supérieur
- PIP version 21.0.1
### Les paquages suivants sont installés
- Pandas 1.3.2

## Installation
- vous pouvez installer Python à partir de ce lien https://www.python.org/downloads/
- vous pouvez installer pip en telechargeant l'installer à l'adresse suivante: https://bootstrap.pypa.io/get-pip.py
- à partir de l'invite de commande dans le répertoir du script tapez la commande suivante:
> python get-pip.py
- vous pouvez installer git à partir du lien suivant: https://git-scm.com/downloads
- dans votre terminal positionnez vous dans le répertoire souhaité pour lancer l'application:
> cd  MonDossier
- cloner le projet à partir de github
> git clone https://github.com/mrdouze/P4-Tournoi_echec.git
- positionner vous dans le repertoire projet:
> cd P4-Tournoi_echec
- lancez et activezl'environnement
> python -m venv venv
> > venv\Scripts\activate
- installer les packages necessaires:
>  python -m pip install -r requirements.txt
- Lancer le script:
> python main.py
- tester la conformité Flake8
> flake8 --format=html --htmldir=flake-report --max-line-length 119

