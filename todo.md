# Liste de Tâches pour l'API RPN

## Raccourcis Pris en Raison du Temps Imparti
- Utilisation d'un stockage en mémoire (dictionnaire) pour les piles, ce qui signifie que les données sont perdues au redémarrage ; aucune base de données persistante implémentée.
- Pas d'authentification ou de gestion des utilisateurs ; toutes les piles sont accessibles sans restrictions.
- Gestion des erreurs basique seulement ; aucune validation complète ou journalisation.
- Pas de tests unitaires ou d'intégration écrits.
- Limité aux opérateurs arithmétiques basiques (+, -, *, /) ; pas d'opérations avancées.
- Fonctionne en mode développement avec rechargement uvicorn ; non optimisé pour la production.

## Améliorations
- Implémenter un stockage persistant en utilisant une base de données comme SQLite ou PostgreSQL pour sauvegarder les piles à travers les sessions.
- Ajouter l'authentification et l'autorisation pour sécuriser l'accès aux piles.
- Améliorer la gestion des erreurs avec des messages plus détaillés et une journalisation.
- Écrire des tests complets pour les endpoints et les opérations.
- Étendre les opérateurs supportés (ex. : exponentiation, racine carrée).
- Optimiser pour un déploiement en production, incluant des variables d'environnement et une configuration.

