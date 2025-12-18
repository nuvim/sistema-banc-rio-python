# 🏦 Sistema Bancário Otimizado - Python

Este repositório contém a solução para o desafio de projeto de **Otimização de Sistema Bancário**, proposto em bootcamp de Python.

O objetivo inicial era refatorar um código monolítico em funções modulares (`sacar`, `depositar`, `criar_usuario`, etc). No entanto, **fui além do desafio proposto** e implementei correções lógicas e novas funcionalidades para tornar o sistema mais robusto e realista.

## 🚀 Melhorias e Diferenciais Implementados

Além da modularização solicitada, realizei as seguintes implementações:

* **Correção de Lógica de Contas:** O código original mantinha um saldo global para todas as contas. Refatorei para que cada conta tenha seu próprio saldo, extrato e histórico de saques.
* **Validação de CPF:** Implementei um filtro que limpa caracteres especiais (pontos e traços) e verifica se o CPF possui 11 dígitos antes de cadastrar.
* **Controle de Saques:** Correção do bug onde o contador de saques diários não era atualizado corretamente entre as chamadas de função.
* **Busca de Clientes:** Adição da funcionalidade `[cc] Consultar Cliente` para verificar dados cadastrais sem precisar criar uma nova conta.
* **Busca de Contas:** Antes de realizar operações (saque/depósito), o sistema valida se a conta informada existe na lista.

## 🛠️ Funcionalidades

O sistema oferece as seguintes operações através de um menu interativo:

* **[d] Depositar:** Adiciona valores a uma conta específica.
* **[s] Sacar:** Retira valores respeitando o saldo, limite por saque (R$ 500,00) e limite diário (3 saques).
* **[e] Extrato:** Exibe a movimentação financeira e o saldo atual da conta.
* **[nc] Nova Conta:** Cria uma conta bancária vinculada a um usuário existente.
* **[nu] Novo Usuário:** Cadastra um cliente (com validação de CPF único).
* **[cc] Consultar Cliente:** Busca e exibe os dados de um cliente pelo CPF.
* **[lc] Listar Contas:** Exibe todas as contas cadastradas no sistema.
