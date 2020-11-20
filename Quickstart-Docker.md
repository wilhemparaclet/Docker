1)Comprendre la différence entre images et containers et à quoi sert un Dockerfile.

Une image Docker est un fichier immuable, qui constitue une capture instantanée d’un conteneur et un conteneur Docker est une instance exécutable d’une image.

Un Dockerfile est un fichier texte décrivant les différentes étapes permettant de partir d'une base pour aller vers une application fonctionnelle

2)installer docker sur votre machine (Ubuntu de préférence, si pas de machine ubuntu vous pouvez faire un double boot ou bien installer une VM en profitant de l’accès gratuit d’un éditeur cloud GCP, Azur, AWS…)

$ sudo apt-get update && sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
$ sudo apt update && sudo apt-get install docker-ce docker-ce-cli containerd.io

3)lancer votre premier container ubuntu, l’équivalent du hello-world de docker
$ docker container run hello-world

4)regarder si votre container est bien lancer

$ docker start mon_container

5)expliquer les commandes docker build, run et exec

FROM	Image parente
ENV	Variable d'environnement
RUN	Commande(s) utilisée(s) pour construire l'image
COPY	Ajoute un fichier dans l'image
WORKDIR	Permet de changer le chemin courant
BUILD Créer une image à partir d'un Dockerfile

6)expliquer ce qu’est un port dans un container

List Répertorier les mappages de ports ou un mappage spécifique pour le conteneur

7)vérifier en vous connectant à votre container qu’il est bien up et qu’il s’aggit bien
$ docker ps
IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
nginx               "/docker-entrypoint.…"   39 minutes ago      Up 39 minutes       0.0.0.0:8000->80/tcp  mon_container
