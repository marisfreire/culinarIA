# ChefeAI

**ChefeAI** é um projeto de integração com IA desenvolvido para a disciplina de Desenvolvimento de Software do período 2024.2. Na aplicação, o usuário pode inserir suas preferências (Quanto a ingredientes, culinária, porções, etc.) e receber uma receita adequada gerada pela Inteligência Artificial.

## Sumário
1. Estrutura de Diretórios
1. Dependências
1. Execute o Aplicativo
1. Versionamento e Problemas Conhecidos
1. Créditos

### 🗂️ Estrutura de Diretórios
---

A estrutura de arquivos do projeto esta da seguinte forma:

```
ChefeAI/
├── app/
│   ├── __init__.py           # Inicialização de app como módulo
│   ├── routes.py             # Definição das rotas do servidor
│   ├── models.py             # Definição dos modelos de dados
│   ├── templates/            # Arquivos de template (HTML)
│   │   ├── index.html        # Página principal do aplicativo
│   │   └── nova_receita.html # Página para gerar novas receitas
│   └── static/               # Arquivos estáticos (JS, CSS)
│       ├── main.js           # Código JavaScript para interatividade
│       └── style.css         # Estilos do site
└── main.py                   # Arquivo principal para execução do aplicativo
```

### ⚙️ Dependências
---

instale as dependências com os seguintes comandos:

```bash
pip install -r requirements.txt
```

### 💻 Execute o aplicativo:
---

```bash
python main.py
```

O aplicativo estará disponível em `http://localhost:5000`.

### Versionamento e Problemas Conhecidos
---
O projeto atualmente está na versão de MVP (Mínimo Produto Viável), a equipe reconhece erros eventuais que possam ocorrer pela geração da receita.

### Créditos
---
O ícone do lado do nome do projeto foi adquirido através do site Font Awesome.