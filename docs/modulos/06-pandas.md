# 🏗️ Bibliotecas & Módulos: Pandas

O **Pandas** é a biblioteca de manipulação de dados mais popular do ecossistema Python. Esta página demonstra os conceitos básicos de Dataframes e Series utilizando o Jupyter Notebook como ferramenta de visualização.

---

## 📊 O Dataset Analisado

Para os estudos práticos, utilizamos o arquivo `dataset.csv` contendo registros demográficos e financeiros.

| Variável | Descrição |
| :--- | :--- |
| **AGE** | Idade do paciente (0 a 17 anos) |
| **FEMALE** | Gênero (1 = Feminino, 0 = Masculino) |
| **LOS** | Tempo de internação em dias |
| **RACE** | Identificador racial (1 a 6) |
| **TOTCHG** | Custo total da internação |

---

## 🛠️ Comandos Essenciais

=== "📂 Carregamento & Inspeção"
    ```python
    import pandas as pd
    df = pd.read_csv('dataset.csv')
    df.head() # Primeiras 5 linhas
    df.info() # Estrutura de dados e nulos
    df.describe() # Estatística descritiva básica
    ```

=== "🔍 Filtros & Seleção"
    ```python
    # Filtrando pacientes com idade superior a 10 anos
    pacientes_maiores = df[df['AGE'] > 10]
    
    # Selecionando colunas específicas
    selecao = df[['AGE', 'TOTCHG']]
    ```

=== "📈 Agrupamentos (Group By)"
    ```python
    # Gasto médio por raça
    media_raca = df.groupby('RACE')['TOTCHG'].mean()
    ```

---

## 📓 Notebook de Estudo

Para acessar o código completo e as visualizações geradas com Pandas, clique no link abaixo:

👉 **[Abrir Notebook: 10-Pandas.ipynb](https://github.com/NandesLima/python-codigos/blob/master/codigos/modulos/10-Pandas.ipynb)**

---
*Este estudo faz parte da **Python Masterclass** de Ariel Shlomoh.*
