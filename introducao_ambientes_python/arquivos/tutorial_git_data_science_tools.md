# Tutorial Git

## Caso não tenha o git instalado execute:

* sudo apt update
* sudo apt install libz-dev libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext cmake gcc
* sudo apt install git

``` console
git config --global user.name "seu nome"
git config --global user.email email@exemplo.br
```

## Resumo geral:

* Criei um diretorio local com `mkdir data-science-tools`
* Entre dentro da pasta ``data-science-tools``
* echo "# README data-science-tools " >> README.md
* git init
* git add README.md
* git commit -m "first commit"
* git branch -M main
* git remote add origin git@github.com:carolx/data-science-tools.git
* git push -u origin main


> Caso ocorra algum erro de username ou email execute o passo a seguir:

``` console
git config --global user.email fulanodetal@exemplo.br
git config --global user.email email@exemplo.br
```

## Detalhado:

* Criei um diretorio local com `mkdir data-science-tools`
* Agora entre dentro da pasta `data-science-tools`
* Agora criei um arquivo de `README.md`
* Adicione no `README.md` com algum texto que será exibido na pagina principal do seu repositório.
* Agora vamos fazer um init do nosso repositório com `git init`
* Agora adicione o `README.md` para a lista de envio para o github:
    * Vamos fazer isso com o `git add README.md`
* Agora adicionamos um comentário com `git commit -m "Add README.md"
* Agora execute o três passos a seguir:
    * `git branch -M main`
    * Agora adicionamos o nosso repositorio remoto
        * `git remote add origin git@github.com:carolx/data-science-tools.git`
    * Agora enviamos a nossa modificação para o github:
        * `git push -u origin main`

* Com isso o repositorio no github poderá ser clonado por outros usuários e receber contribuições por meio de Pull Request
