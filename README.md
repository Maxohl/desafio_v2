# Desafio aula de Python

## Sistema bancário versão 2

Nesse desafio foi atualizado o sistema bancário do primeiro desafio.

## Objetivo do desafio

O objetivo geral do desafio é separar as funções existentes de saque, depósito e extrato em funções python, além de, criar duas novas funções para o cadastramento
de usuários e contas correntes.

Alguns detalhes do desafio:
 - A função saque deve receber os argumentos somente por nome.
 - A função depósito deve receber os argumentos somente por posição.
 - A função extrato receve os argumentos por nome e posição.
 - O programa deve armazenar os usuários numa lista, composto por : nome, data de nascimento, CPF, e endereço.
 - O endereço é uma String com o formato : Logradouro, nro - bairro - cidade/sigla estado.
 - Deve ser armazenado somente os números do CPF.
 - Não pode ser possível o cadastro de 2 usuários com o mesmo CPF.
 - O programa dever armazenar contas correntes em uma lista, composta por : agência, número da conta.
 - O número da agência é fixo "0001".
 - O número da conta é sequencial iniciando em 1.

## Funções extras

Funções que não fazem parte do desafio, mas que eu decidi que melhoram o programa.

- Menu inicial para criação de usuários e contas.
- Menu principal, pode ser acessado a partir do menu inicial desde que o usuário já tenha criado uma conta para acessar.
- Menu principal é onde o usuário pode : Verificar saldo, realizar saques e depósitos e visualizar o extrato.

Ao contrário do desafio original, o usuário não pode fazer saques, depósitos ou ver extrato sem primeiro criar uma conta.
O programa também impede o usuário de registrar um CPF que não seja apenas números.

Com a presença de 2 menus, o usuário pode sair do menu principal, criar um novo usuário e conta, e voltar ao menu principal com esse novo usuário sem 
alterar o saldo já salvo do usuário anterior. Isso também reseta o limite de saques por dia.

Assim como o desafio anterior, eu adicionei paradas em algumas telas para facilitar a visualização do sucesso ou erro de operações de saque e depósito.
