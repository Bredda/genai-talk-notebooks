# IA générative en action : intégrez les LLM dans vos applications !

Ce repository accompagne le talk [Younup](https://www.younup.fr/) intitulé [IA générative en action : intégrez les LLM dans vos applications !](https://www.youtube.com/watch?v=KputAxjl7J4&t=12s).

Il contient l'ensemble des démos abordées ainsi que d'autres exemples plus avancés sous forme de [notebook Jupyter](https://jupyter.org/).

Ces démos illusrent l'orchestration de LLM via différentes librairies, type [Langchain](https://www.langchain.com/), [Langgraph](https://langchain-ai.github.io/langgraph/) ou encore [SmolaAgent](https://huggingface.co/docs/smolagents/index)

## Usage

Les démos Langchain utilisent des modèles issus d'OpenAI. Langchain étant model-agnostic il est donc très facile de switcher sur un modèle ou provider différentes si besoin.

Les démos SmolAgent utilsient le modèle Qwen/Qwen2.5-Coder-32B-Instruct d'HuggingFace. Ce modèle est gratuit et nécessite seulement un compte avec clé d'api (à rensigner dans le fichier `.env`)

Certaines démos s'appuyent sur des services tiers (Redis, Langfuse etc.). Pour facliter les choses, un fichier `docker-compose.yaml` est disponible à la racine du dépôt mettant à disposition en local:

- Redis - vector store rag et mémoire - Dashboard sur http://localhost:8001/
- Langfuse (+ db psotgres) - Observabilité - Dashbaord sur http://localhost:3000

Pour exécuter les notebooks

0. Prérequis: utilisation de python >= 3.11 (certaines démos ne fonctionneront pas correctement avec une version inférieure)
1. Dupliquer .env.example et renommer en .env
2. Renseigner les clé nécessaires dans ce fichier .env
3. Installer les dépendences python: `pip install -r requirements.txt`
4. Lancer les services tiers: `docker-compose up -d`

## Note

Le dossier `99-Apps` a pour objectif de fournir à terme des tentatives de reproduction d'outils intéressants: type [Perplexity](https://www.perplexity.ai/), la fonctionnlaité de Podcast de [NotbookLm](https://notebooklm.google.com/?), etc.

C'est pour le moment une partie Work in progress.
