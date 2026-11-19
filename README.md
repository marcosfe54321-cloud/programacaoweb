# API de chamados de suporte

**Estudante:** Marcos Felipe Ferreira Duarte

## Objetivo

Criar a estrutura inicial de uma API de chamados de suporte com Flask. Nesta
etapa, a aplicação disponibiliza somente a rota inicial; não há cadastro de
chamados nem banco de dados.

## Instalação

Com o [uv](https://docs.astral.sh/uv/) instalado, sincronize o ambiente e as
dependências travadas no `uv.lock`:

```bash
uv sync --locked
```

## Execução

Inicie a aplicação com:

```bash
uv run flask --app app run --host=0.0.0.0 --port=5000
```

## Rota inicial

Acesse `http://localhost:5000/` com uma requisição `GET`. A resposta esperada
tem status HTTP `200`, conteúdo JSON e o corpo:

```json
{
  "mensagem": "API de chamados em funcionamento"
}
```
