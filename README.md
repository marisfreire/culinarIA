# CulinarIA

**CulinarIA** é um projeto de integração com IA desenvolvido para a disciplina de Desenvolvimento de Software do período 2024.2. Na aplicação, o usuário pode inserir suas preferências (Quanto a ingredientes, culinária, porções, etc.) e receber uma receita adequada gerada por Inteligência Artifical, o nosso modelo escolhido é o gpt-3.5-turbo. Utilizamos de Python com a framework Flask, além de Javascript, HTML e CSS (com Tailwind CSS) para o desenvolvimento do projeto.

## Sumário
1. Estrutura de Diretórios
1. Dependências
1. Execute o Aplicativo
1. Imagens
1. Versionamento e Problemas Conhecidos
1. Créditos

### 🗂️ Estrutura de Diretórios

A seguir segue a estrutura de diretórios do projeto
```
.
├── app/
│   ├── blueprints/       # Módulos organizados como Blueprints do Flask
│   │   ├── auth/         # Autenticação
│   │   ├── menu/         # Menu do aplicativo
│   │   └── recipe/       # Gerenciamento de receitas
│   ├── models/           # Modelos de dados (usuários, receitas)
│   ├── src/              # Arquivos estáticos e templates
│   │   ├── assets/       # Elementos visuais (ícones, imagens)
│   │   ├── login/        # Página de login
│   │   ├── menu/         # Página do menu
│   │   ├── nova-receita/ # Página de criação de receitas
│   │   ├── profile/      # Perfil do usuário
│   │   ├── signup/       # Cadastro de usuário
│   │   ├── layout.html   # Layout base
│   │   └── style.css     # Estilos gerais
│   ├── __init__.py
│   └── extensions.py     # Configuração de extensões
├── tests/                # Testes do projeto
├── main.py               # Arquivo principal do projeto
├── README.md             # Documentação do projeto
└── requirements.txt      # Dependências necessárias
```
### ⚙️ Dependências
---

Instale as dependências com os seguintes comandos:

```bash
pip install -r requirements.txt
```
### 💾 Habilitar o mongoDB:
---

```bash
mongod
```

### 💻 Execute o aplicativo:
---

```bash
python main.py
```

O aplicativo estará disponível em `http://localhost:5000`.

### 📷 Imagens da aplicação
---
Imagens de algumas telas da aplicação

![./screenshots/login.png]()
![./screenshots/menu-logged.png]()
![./screenshots/menu.png]()
![./screenshots/new-recipe.png]()
![./screenshots/recipe-favorite.png]()
![./screenshots/recipe.png]()
![./screenshots/singup.png]()

### Versionamento e Problemas Conhecidos
---
O projeto atualmente está na versão final, a equipe reconhece erros na geração da receita, na geração da lista de compras, na alteração de senha ou de informações do perfil e na feature de favoritos.

### Créditos
---
O ícone do lado do nome do projeto foi adquirido através do site Font Awesome, utilizamos também as fontes Roboto e Playwrite HR Lijeva, ambas do Google Fontes. As imagens foram tiradas do site Unsplash e são grátis para uso. 
