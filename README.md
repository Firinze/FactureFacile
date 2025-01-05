# FactureFacile
FactureFacile est une solution complète de gestion des factures,  pour aider les entreprises à gérer efficacement leur processus de facturation. Grâce à son architecture modulaire et à son design réactif, l'application est adaptée à une utilisation sur différents appareils et peut évoluer avec les besoins de l'entreprise. L'application est construite avec Django et utilise Bootstrap pour un design réactif et moderne.

## Fonctionnalités
- Enregistrement de nouveaux clients
- Création et gestion de factures
- Ajout et suppression d'articles dans les factures
- Calcul automatique des totaux
- Interface utilisateur conviviale et réactive
- Génération de factures au format PDF

## Technologies Utilisées
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Base de données**: SQLite (ou autre selon la configuration)

## Prérequis
Avant de commencer, assurez-vous d'avoir installé les éléments suivants :
- Python 3.x
- Django
- pip (gestionnaire de paquets Python)

## Installation
1. **Clonez le dépôt** :
   ```bash
   git clone https://github.com/votre-utilisateur/facturefacile.git
   cd facturefacile
   ```

2. **Créez un environnement virtuel** (optionnel mais recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
   ```

3. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Appliquez les migrations** :
   ```bash
   python manage.py migrate
   ```

5. **Démarrez le serveur de développement** :
   ```bash
   python manage.py runserver
   ```

6. **Accédez à l'application** :
   Ouvrez votre navigateur et allez à `http://127.0.0.1:8000/`.

## Utilisation
- **Ajouter un client** : Accédez à la page d'ajout de client pour enregistrer un nouveau client.
- **Créer une facture** : Sélectionnez un client et ajoutez des articles pour créer une facture.
- **Gérer les articles** : Ajoutez ou supprimez des articles dans la facture en cours.
- **Télécharger une facture** : Vous pouvez télécharger la facture au format PDF.

## Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez contribuer, veuillez suivre ces étapes :
1. Forkez le projet
2. Créez une nouvelle branche (`git checkout -b feature/YourFeature`)
3. Apportez vos modifications et validez (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/YourFeature`)
5. Ouvrez une Pull Request

## Auteurs
- Firinze Gbènito DOSSOU - [Votre Profil GitHub](https://github.com/votre-utilisateur)

## License
Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements
- Merci à [Bootstrap](https://getbootstrap.com/) pour le framework CSS.
- Merci à [Django](https://www.djangoproject.com/) pour le framework web.
