Cronograma de Estudos

Este projeto é um sistema simples de organização de estudos em Python. O objetivo é permitir que o usuário cadastre conteúdos, associe cada um a um dia da semana e gerencie a lista conforme necessário.

A ideia surgiu como uma forma prática de treinar lógica, manipulação de arquivos e construção de menus interativos.

📌 Funcionalidades

Adicionar matéria
O usuário informa o nome do conteúdo e o dia da semana. A matéria é salva tanto na memória quanto no arquivo Materias.txt.

Listar matérias cadastradas
Exibe todas as matérias armazenadas, organizadas com índice e dia correspondente.

Remover matéria
Permite remover uma matéria pelo nome. Após a remoção, o arquivo é atualizado para manter a lista consistente.

Persistência de dados
As matérias são carregadas automaticamente do arquivo dados/Materias.txt ao iniciar o programa.

Menu interativo
Navegação simples entre as ações disponíveis, com tratamento básico de erros para entradas inválidas.

▶️ Como Executar

Certifique-se de ter o Python 3 instalado.

Crie a pasta dados na raiz do projeto, caso ainda não exista.

Execute o script:

python nome_do_arquivo.py

📚 Aprendizados Envolvidos

Manipulação de listas e dicionários

Estruturas condicionais e funções

Tratamento simples de exceções

Leitura e escrita em arquivos de texto

Construção de menus interativos

Organização básica de um projeto Python

📝 Observação

Este projeto foi desenvolvido como prática pessoal para reforçar conceitos iniciais de lógica e persistência de dados. Pode servir como base para melhorias futuras, como interface gráfica, validação mais robusta, uso de JSON, etc.