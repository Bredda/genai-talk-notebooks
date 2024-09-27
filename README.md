# IA générative en action : intégrez les LLM dans vos applications !

Ce repository accompagne le talk [Younup](https://www.younup.fr/) intitulé [IA générative en action : intégrez les LLM dans vos applications !](https://www.youtube.com/watch?v=KputAxjl7J4&t=12s).

Il contient l'ensemble des démos abordées ainsi que d'autres exemples plus avancés sous forme de [notebook Jupyter](https://jupyter.org/).

Ces démos utilisent la librairie [Langchain](https://www.langchain.com/)

## Contenu

- **01-Basics**
  - 01-Simple QA chat with memory
- **02-Retrieval Augmented Generation**
  - 02.01-RAG Basics
  - 02.02-RAG youtube
- **03-Agents**
  - 03.02-Simple Agent with Langchain
- **04-Advanced RAG**
  - 04.01-RAG knowledge graph
- **05-LangGraph**
  - 05.01-Multi agent collaboration
- **06-Observabilitty**
  - 06.01-Langfuse
- **07-Classification**
  - 07.01-Document tagging

### Usage

L'ensemble des démos utilise des modèles OpenAI. Se reporter à la documentation `Langchain` pour utiliser d'autres fournisseurs ou des modèles locaux.

Certaines démos s'appuyent sur des services tierces (Redis, Neo4j etc.). Pour facliter les choses, un fichier `docker-compose.yaml` est disponible à la racine du dépôt mettant à disposition:

- Redis - vector store rag et mémoire - Dashboard sur http://localhost:8001/
- Neo4j - outil de graphe de connaissance - Dashboard sur http://localhost:7474/browser/
- Langfuse (+ db psotgres) - Observabilité - Dashbaord sur http://localhost:3000

Pour exécuter les notebooks (prérequis: python et Jupyter):

1. Dupliquer .env.example et renommer en .env
2. Renseigner les clé nécessaires dans ce fichier .env
3. Installer les dépendences python: `pip install -r requirements.txt`
4. Lancer les services tiers: `docker-compose up -d`
