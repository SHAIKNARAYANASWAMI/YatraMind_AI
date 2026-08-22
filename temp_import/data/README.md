# YatraMind AI Starter Dataset

This is a synthetic development dataset for an AI-based tourism recommendation web application.

## Dataset size
- Users: 500
- Destinations: 60
- Interactions: 15000
- Reviews: 2352
- Context snapshots: 4000
- Graph edges: 16120

## Model usage
- LightGCN / GCN / GAT: graph_edges.csv and interactions.csv
- BERT / Sentence-BERT: destinations.csv and reviews.csv
- Context-aware ranking: context_snapshots.csv
- Cold-start recommendations: user_preferences.csv

## Important limitation
All users, interactions, reviews, costs, popularity values, and context records are synthetic.
Destination names are recognisable, but the numeric values are not factual live travel information.
Use official APIs or verified datasets before production deployment.
