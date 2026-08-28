# Launcher

Programinha desktop feito em Python que resolve um problema bem chato:
todo dia eu abria os mesmos programas na mão, um por um, dependendo se
ia estudar ou jogar. Agora é um clique.

- 📚 **Estudo** → abre VS Code, terminal e Firefox
- 🎮 **Jogos** → abre Steam, Discord, Firefox e WhatsApp

## Tecnologias

- Python
- customtkinter (interface)
- subprocess / os (automação de abertura de programas)

## Como rodar

Este repositório contém apenas o código-fonte. O executável (.exe)
não é versionado para gerá-lo você mesmo.

**1. Clone o repositório**

**2. Crie um ambiente virtual e instale as dependências**

pip install customtkinter pyinstaller

**3. Rode direto com Python**

python main.py

**4. Ou gere o executável**

pyinstaller --onefile --windowed main.py

O `.exe` vai ser criado na pasta `dist/`.
