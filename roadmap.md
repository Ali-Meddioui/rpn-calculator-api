# Feuille de Route pour l'API RPN

## Backlog de Fonctionnalités Potentielles
1. **Stockage Persistant** : Intégrer une base de données pour persister les piles et les opérations à travers les redémarrages de l'application.
2. **Authentification Utilisateur** : Ajouter la connexion et l'inscription des utilisateurs pour permettre des piles privées par utilisateur.
3. **Opérateurs Avancés** : Supporter des opérations mathématiques supplémentaires comme l'exponentiation (^), le modulo (%), les fonctions trigonométriques, etc.
4. **Historique des Opérations** : Implémenter un journal d'historique pour chaque pile pour suivre les opérations et permettre les fonctionnalités undo/redo.
5. **Versioning API** : Introduire le versioning API pour supporter la compatibilité ascendante pour les changements futurs.
6. **Limitation de Taux** : Ajouter une limitation de taux pour prévenir l'abus de l'API.
7. **Support WebSocket** : Activer les mises à jour en temps réel pour les changements de pile via WebSockets.
8. **Améliorations de la Documentation** : Générer une documentation API plus détaillée et des exemples d'utilisation.
9. **Automatisation du Déploiement** : Mettre en place des pipelines CI/CD pour les tests automatisés et le déploiement sur des plateformes cloud comme Heroku ou AWS.
10. **Optimisation des Performances** : Profiler et optimiser l'API pour des scénarios de haute charge. 