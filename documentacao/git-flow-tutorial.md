# Git Flow VegaDesp Backend

O presente documento descreve o fluxo de desenvolvimento adotado no projeto, baseado no modelo Git Flow.

## Branches Principais

### Main

- Contem apenas o código estável, representa versões prontas para produção.

### Develop

- Branch principal de desenvolvimento, todo novo código entra primeiro aqui.
- Sempre deve estar funcional, porém não necessariamente em produção.

### Feature (brach com nome decidido pelo dev)

- Usada para novas funcionalidades, sempre criada a partir da develop

## Fluxo de trabalho

- Ao iniciar o desenvolvimento de uma nova funcionalidade o seguinte procedimento deve ser seguido.

1. Criar a feature sempre baseada na develop

```bash
git checkout develop
git pull origin develop
git checkout -b feature/nome-da-feature
```

2. Realizar o desenvolvimento e fazer o commit normalmente com base no nome da feature `git push origin nome-da-feature`.

3. Finalizar a feature

```bash
git checkout develop
git merge feature/nome-da-feature
git push origin develop
```

4. Nesse momento as alterações desenvolvidas estão juntas a develop.

5. Para juntar o conteudo da develop com a main

```bash
git checkout main
git merge develop
git push origin main
```

6. Apagar a feature criada 

```bash
git branch -d feature/nome-da-feature 
git push origin --delete feature/nome-da-feature
```