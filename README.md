# Suit de testes da steam

O site da steam foi utilizado como meio de estudo sobre automatização de casos de testes utilizando *python, pytest, unittest*.

## Casos de Testes

Os casos de teste escritos foram baseados nas seguintes ferrramentas do site da **steam**:

- Busca de jogos
- Adicinar filtros
- Remover filtros
- Selecionar diferentes formas de ordenação da página
- Trocar idioma

## Execução dos Testes

- Os testes podem ser executados no terminal.
- Primeiramente é necessário instalar os pacotes necessários (requirements.txt)

        pip install -r requirements.txt

- Executar os casos de testes

        python -m pytest src/tests/test_home_page.py
