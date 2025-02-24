# CulinarIA

**CulinarIA** é um projeto de integração com IA desenvolvido para a disciplina de Desenvolvimento de Software do período 2024.2. Na aplicação, o usuário pode inserir suas preferências (Quanto a ingredientes, culinária, porções, etc.) e receber uma receita adequada gerada pela Inteligência Artificial.

## Sumário
1. Estrutura de Diretórios
1. Dependências
1. Execute o Aplicativo
1. Versionamento e Problemas Conhecidos
1. Créditos

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
O projeto atualmente está na versão de MVP (Mínimo Produto Viável), a equipe reconhece erros eventuais que possam ocorrer pela geração da receita.

### Créditos
---
O ícone do lado do nome do projeto foi adquirido através do site Font Awesome, utilizamos também as fontes Roboto e Playwrite HR Lijeva, ambas do Google Fontes.