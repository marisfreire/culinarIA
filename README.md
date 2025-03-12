# CulinarIA

**CulinarIA** é um projeto de integração com IA desenvolvido para a disciplina de Desenvolvimento de Software do período 2024.2. Na aplicação, o usuário pode inserir suas preferências (Quanto a ingredientes, culinária, porções, etc.) e receber uma receita adequada gerada por Inteligência Artifical, o nosso modelo escolhido é o gpt-4o-mini. Utilizamos de Python com a framework Flask, além de Javascript, HTML e CSS (Com Tailwind CSS) para o desenvolvimento do projeto.

## Sumário
1. Estrutura de Diretórios
1. Dependências
1. Execute o Aplicativo
1. Versionamento e Problemas Conhecidos
1. Créditos

### Estrutura de Diretórios

A seguir segue a estrutura de diretórios do projeto
.
├── app/
│   ├── blueprints/
│   │   ├── auth/
│   │   │   ├── _init_.py
│   │   │   └── auth.py
│   │   ├── menu/
│   │   │   ├── _init_.py
│   │   │   └── menu.py
│   │   └── recipe/
│   │       ├── _init_.py
│   │       └── recipe.py
│   ├── models/
│   │   ├── _init_.py
│   │   ├── recipes.py
│   │   └── users.py
│   ├── src/
│   │   ├── assets/ // Aqui guardamos todos os elementos visuais do projeto
│   │   │   ├── barrinhas.png
│   │   │   ├── clock.png
│   │   │   ├── favorite.svg
│   │   │   ├── logo.png
│   │   │   ├── padlock.svg
│   │   │   ├── profile-icon.svg
│   │   │   ├── utensils.svg
│   │   │   └── vector.png
│   │   ├── login/ 
│   │   │   ├── login.css
│   │   │   ├── login.html
│   │   │   └── login.js
│   │   ├── menu/
│   │   │   └── menu.html
│   │   ├── nova-receita/
│   │   │   ├── nova-receita.html
│   │   │   └── nova-receita.js
│   │   ├── profile/
│   │   │   └── profile.html
│   │   ├── signup/
│   │   │   ├── signup.css
│   │   │   ├── signup.html
│   │   │   └── signup.js
│   │   ├── exemplo.html
│   │   ├── layout.html
│   │   └── style.css
│   ├── _init_.py
│   └── extensions.py
├── tests/
│   ├── _init_.py
│   └── test_sample.py
├── main.py // A partir daqui se inicia o projeto
├── README.md
└── requirements.txt // Pacotes necessários para a execução

### ⚙️ Dependências
---

Instale as dependências com os seguintes comandos:

```bash
pip install -r requirements.txt
```
### Habilitar o mongoDB:
---
```bash
mongod
```
Caso esteja criando o banco pela primeria vez abra o shell para criar o banco e suas coleções:
```bash
mongosh
```
Crie o banco de dados `culinaria`
```bash
use culinaria
```
As coleções são criadas automáticamente quando se insere um documento, mas podem ser criadas assim:
```bash
db.createCollection("users")
db.createCollection("recipes")
```

### 💻 Execute o aplicativo:
---

```bash
python main.py
```

O aplicativo estará disponível em `http://localhost:5000`.

### Versionamento e Problemas Conhecidos
---
O projeto atualmente está na versão final, a equipe reconhece erros na geração da receita, na geração da lista de compras, na alteração de senha ou de informações do perfil e na feature de favoritos.

### Créditos
---
O ícone do lado do nome do projeto foi adquirido através do site Font Awesome, utilizamos também as fontes Roboto e Playwrite HR Lijeva, ambas do Google Fontes.
