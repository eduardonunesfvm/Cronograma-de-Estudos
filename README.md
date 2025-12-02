# Cronograma-de-Estudos 📅

## 🔎 O que é  
Um sistema simples em Python que organiza seu cronograma de estudos. Permite cadastrar “matérias/assuntos”, associá-los a dias da semana, listar, remover e persistir os dados em arquivo. Feito pra praticar lógica, manipulação de arquivos, menus interativos e organização de código.  

## ✅ Funcionalidades  

- Adicionar matéria com dia da semana correspondente.  
- Listar todas as matérias cadastradas (com índice e dia).  
- Remover matéria pelo nome.  
- Persistência: ao iniciar, carrega todas as matérias salvas; ao modificar, atualiza o arquivo.  
- Menu interativo no terminal com navegação clara e tratamento básico de erros.  

## 🧰 Tecnologias / Conceitos utilizados  

- Linguagem: Python (3.x)  
- Manipulação de arquivos de texto para persistência  
- Estruturas de dados nativas (listas, dicionários) para armazenamento em memória  
- Controle de fluxo, condicionais, funções  
- Interface de terminal (CLI) simples — sem GUI  

## 🚀 Como rodar  

1. Clone o repositório:

   ```bash
   git clone https://github.com/eduardonunesfvm/Cronograma-de-Estudos.git
   cd Cronograma-de-Estudos
Certifique-se de ter o Python 3 instalado.

Crie a pasta dados/ na raiz do projeto, caso ainda não exista.

Execute:

bash
Copiar código
python src/main.py
# ou substitua `main.py` pelo nome correto do arquivo principal, se for diferente
Use o menu no terminal para adicionar, listar ou remover matérias.

📂 Estrutura do projeto
bash
Copiar código
/Cronograma-de-Estudos  
 ├── src/           # código-fonte  
 │    └── main.py   # arquivo principal (ou equivalente)  
 ├── dados/         # pasta para arquivos de dados (listas de matérias, histórico etc.)  
 ├── README.md  
⚠️ Limitações e observações
Interface via terminal — não há interface gráfica.

Persistência básica com arquivos .txt; não há banco de dados nem tratamento avançado de erros (validações, concorrência etc.).

Código simples, ideal para estudo/personal use — não robusto para uso em produção ou multiusuário.

💡 Possíveis melhorias / Próximos passos
Migrar para persistência com JSON ou banco de dados leve (SQLite) — facilita leitura/escrita e mantém estrutura.

Criar interface gráfica (GUI) ou versão web para tornar mais amigável.

Adicionar validação mais robusta nas entradas (campos vazios, caracteres especiais, duplicidade).

Permitir múltiplos “cronogramas” (ex: para diferentes semanas/períodos).

Adicionar opção de backup ou exportação de dados.

👨‍💻 Autor
Eduardo Nunes — GitHub: @eduardonunesfvm
