# pucpr-devops
Repositório utilizado na matéria de devops da pucpr

# TaskCLI

Um gerenciador de tarefas simples via linha de comando, feito em Python.
Projeto criado para praticar CI/CD com GitHub Actions.

## Funcionalidades

- Adicionar tarefas
- Listar tarefas
- Marcar tarefas como concluídas
- Remover tarefas

Os dados são salvos localmente em `tasks.json`.

## Como usar

```bash
pip install -r requirements.txt

python cli.py add "Estudar CI/CD"
python cli.py list
python cli.py done 1
python cli.py remove 1
```

## Rodando os testes

```bash
pytest -v
```

## CI/CD

Este repositório possui um workflow do GitHub Actions (`.github/workflows/ci.yml`)
que roda automaticamente os testes a cada `push` e `pull request` para a branch `main`.