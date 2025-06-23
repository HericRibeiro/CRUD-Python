# 🐍 CRUD de Clientes em Python + SQLite 🚀

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)

---

## 📌 Sobre o Projeto

Projeto de estudo desenvolvido para praticar **Programação Orientada a Objetos (POO)** em Python, com um **CRUD completo** utilizando **SQLite** como banco de dados local.

O sistema permite:

* ✅ Adicionar clientes
* ✅ Listar clientes
* ✅ Atualizar clientes
* ✅ Deletar clientes
* ✅ Buscar cliente por ID

---

## 📂 Estrutura do Projeto

```
meu_crud/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── database.py
├── cliente.py
├── main.py
├── requirements.txt
├── tests/
│   └── test_dummy.py
└── README.md
```

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO_GITHUB/SEU_REPOSITORIO.git
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv

# Ative:
# No Windows CMD:
venv\Scripts\activate

# Ou no PowerShell:
venv\Scripts\Activate.ps1

# Ou no Linux/Mac:
source venv/bin/activate
```

3. Instale as dependências (se tiver):

```bash
pip install -r requirements.txt
```

4. Execute o projeto:

```bash
python main.py
```

---

## ✅ Tecnologias Utilizadas

* Python 3.11
* SQLite3
* GitHub Actions (CI simples)
* unittest (para testes)

---

## ⚙️ CI - GitHub Actions

Este projeto inclui um workflow simples com **GitHub Actions** para:

* Validar o build
* Rodar testes unitários

Arquivo do workflow:

```
.github/workflows/python-app.yml
```

---

## 👨‍💻 Autor

Feito com dedicação por **Heric Ribeiro**

[LinkedIn](https://www.linkedin.com/in/heric-willian-5b78722a3/) | [GitHub](https://github.com/HericRibeiro)

---

## 📄 Licença

Este projeto está sob licença **MIT**.

---
