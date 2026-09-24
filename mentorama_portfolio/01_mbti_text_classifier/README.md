# Classificação experimental de textos por rótulos MBTI

Implementação própria da proposta 1 do curso Pro da Mentorama. O programa aprende
associações entre textos e rótulos fornecidos no conjunto `mbti_1.csv`. Esses
rótulos são **autodeclarações**, não diagnósticos. O resultado não mede personalidade
e não serve para decisões de contratação, educação ou saúde.

## Dados e execução

O conjunto `mbti_1.csv` foi localizado na pasta do projeto do usuário no Drive.
Ele não integra o repositório. Coloque-o em `data/mbti_1.csv`, com as colunas
`type` (uma das 16 siglas) e `posts` (texto, com postagens separadas por `|||`).

```bash
cd mentorama_portfolio/01_mbti_text_classifier
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python train.py data/mbti_1.csv
python app.py "Um texto longo escrito voluntariamente para experimentar o classificador."
python -m unittest discover -s tests -v
```

No Windows, ative o ambiente com `.venv\\Scripts\\activate`. Os arquivos
`artifacts/model.joblib` e `artifacts/metrics.json` são gerados localmente.
Nunca carregue um arquivo `joblib` de origem desconhecida.

## Avaliação

O programa remove URLs e menções explícitas às siglas MBTI, elimina textos
duplicados e reserva 20% dos registros para teste antes de ajustar o TF-IDF.
Compara regressão logística a uma referência que sempre prevê a classe mais
frequente. Registra acurácia, F1 macro, resultados por classe, tamanhos e
distribuição das classes. A divisão aleatória **não mede generalização entre
plataformas, épocas ou comunidades**; uma avaliação externa seria necessária.

Os testes incluídos exercitam o pipeline com dados artificiais e verificam
preparação, ausência de textos iguais nos dois conjuntos, geração dos artefatos
e inferência. **Não há métrica medida na base completa neste repositório.**

## Fonte e autoria

O escopo deriva da proposta 1 do curso Mentorama, disponível na pasta privada
do aluno no Google Drive. Código desta pasta produzido para este portfólio;
nenhum notebook da plataforma foi reproduzido. Os dados originais e sua licença
devem ser conferidos antes de qualquer redistribuição.
