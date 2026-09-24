# Classificador experimental de notícias

Implementação própria da proposta 3 do curso Pro. Aprende rótulos `fake` e
`real` de uma base rotulada; **não verifica fatos**. Padrões de estilo e origem
das notícias podem influenciar o resultado. Não use a saída isoladamente para
moderação ou avaliação de pessoas.

## Dados

O enunciado descreve um conjunto com identificador, título, texto e rótulo.
A base original não foi localizada entre os arquivos disponíveis no Drive.
Prepare um CSV em `data/news.csv` com `title`, `text`, `label` e, opcionalmente,
`id`. Rótulos aceitos: `fake`/`real`, `false`/`true`, `falsa`/`verdadeira`.
Se a base usar números, converta-os só depois de conferir sua codificação na
documentação original.

```bash
cd mentorama_portfolio/03_news_classifier
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python train.py data/news.csv
python app.py "Título da notícia" "Texto completo da notícia para análise."
python -m unittest discover -s tests -v
```

O programa remove textos duplicados antes da divisão, separa 20% para teste,
ajusta o TF-IDF somente no treino e compara regressão logística a uma previsão
majoritária. Salva `artifacts/metrics.json` com acurácia, F1 macro, métricas
por classe e tamanhos. Uma divisão aleatória não testa mudança de período,
fonte jornalística ou tema. Seria preciso reservar grupos ou tempo para isso
quando tais campos estivessem disponíveis.

Os testes locais usam dados artificiais para verificar o fluxo e as validações.
**Não há resultado de desempenho na base do enunciado.** Dados e modelos ficam
fora do repositório; carregue somente modelos `joblib` de sua autoria.
