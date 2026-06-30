# PRD — VotezPour

**Équipe :** Kaïs Hadj Said, Djibrill Mokrani, Omar Rachid, Marc Elie Aziagnon
**Date :** Mardi 30 juin 2026

## 🎯 Le problème
Organiser un événement ou une réunion à plusieurs nécessite souvent de comparer les disponibilités ou préférences de chacun. Échanger par messages ou e-mails pour ça est long et confus, surtout au-delà de 3-4 personnes.

## 💡 La solution
VotezPour permet de créer un sondage en quelques secondes, de le partager via un simple lien, et de voir les résultats des votes en direct.

## 👥 Les utilisateurs cibles
Des groupes (amis, associations, équipes de travail, étudiants) qui doivent rapidement se mettre d'accord sur un choix commun (date, lieu, option).

## ⭐ Les fonctionnalités (priorisées — méthode MoSCoW)

### MUST (le MVP — sans ça, le produit n'existe pas)
- [x] Créer un sondage avec une question et plusieurs options
- [x] Générer un lien de partage unique
- [x] Voter pour une option
- [x] Voir les résultats en direct avec le nombre de votes par option

### SHOULD (important, si on a le temps)
- [ ] Empêcher un même utilisateur de voter plusieurs fois
- [ ] Date d'expiration du sondage

### COULD (bonus, le "waouh")
- [ ] Graphiques animés des résultats
- [ ] Export des résultats en CSV
- [ ] Mode sombre

### WON'T (ce qu'on a décidé de NE PAS faire cette semaine)
- Système de comptes utilisateurs / authentification
- Sondages à choix multiples (plusieurs réponses possibles)

## 🛤️ Le parcours utilisateur principal
"En tant qu'utilisateur, je veux créer un sondage et partager un lien afin que mon groupe puisse voter rapidement et que je voie les résultats en direct."

Étape par étape :
1. L'utilisateur arrive sur la page d'accueil et remplit une question + des options
2. Il clique sur "Créer le sondage" et obtient un lien unique
3. Il partage ce lien à son groupe
4. Chaque destinataire ouvre le lien, sélectionne une option et vote
5. Tout le monde peut consulter la page de résultats, mise à jour en direct

## 🚫 Hors périmètre
- Comptes utilisateurs et connexion
- Sondages à réponses multiples
- Application mobile native

## ✅ Définition de "terminé"
Le MVP est terminé quand : un utilisateur peut créer un sondage, partager le lien, voter, et voir les résultats s'afficher correctement avec le bon décompte des votes — le tout déployé sur la VM Debian et accessible.
