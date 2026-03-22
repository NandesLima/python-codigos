# 🌱 Fundamentos: Variáveis & Constantes

A base de qualquer linguagem de programação é a forma como armazenamos e manipulamos informações na memória do computador. Em Python, as variáveis e constantes seguem padrões específicos de nomenclatura e tipagem dinâmica.

---

## 🏗️ O Conceito de Variáveis

Em Python, as variáveis são nomes que apontam para objetos na memória. A atribuição é feita utilizando o operador `=`.

=== "📝 Nomenclatura (Snake Case)"
    ```python
    # Nomes descritivos e em minúsculas
    nome_usuario = "Ariel Shlomoh"
    idade_paciente = 25
    total_compras = 450.90
    ```

=== "🔒 Constantes"
    Embora o Python não possua constantes imutáveis nativas (como o `const` em outras linguagens), a convenção é utilizar nomes em **MAIÚSCULAS** para sinalizar que o valor não deve ser alterado.
    
    ```python
    PI = 3.14159
    DATABASE_URL = "https://github.com/NandesLima"
    ESTADO_PADRAO = "Fortaleza-CE"
    ```

---

## 🛠️ Atribuição Múltipla

O Python permite a atribuição de múltiplos valores a múltiplas variáveis em uma única linha, facilitando a legibilidade.

```python
x, y, z = 10, 20, 30
a = b = c = 0 # Todas recebem o mesmo valor
```

---

## 📓 Notebook de Estudo

Para acessar os exemplos práticos, testes de tipagem e exercícios de variáveis, clique no link abaixo:

👉 **[Abrir Notebook: 01-variaveis-e-constantes.ipynb](https://github.com/NandesLima/python-codigos/blob/master/codigos/01-variaveis-e-constantes.ipynb)**

---
*Este estudo faz parte da **Python Masterclass** de Ariel Shlomoh.*
