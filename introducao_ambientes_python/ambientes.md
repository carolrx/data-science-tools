# Criação de Ambientes virtuais

## Aula 1

Tutorial Criação de Ambientes virtuais.

* Carlos Barbosa
- Tempo estimado: 40 minutos


## Introdução

Olá, vamos aprender com esse tutorial o básico sobre ambientes virtuais e como
criar um ambiente virtual com foco em data science utilizando o `anaconda`.

### Ambiente Virtual

Ambiente virtual é uma ferramenta que permite criar espaços autocontidos no qual as
dependências de cada projeto são mantidas isoladas.
Através desta ferramenta podemos ter projetos com requisitos conflitantes instalados
na mesma máquina sem correr o risco que ocorra um conflito de dependência.

### Por que utilizar?

Por meio desta tecnologia podemos ter ambientes totalmente isolados resultando em ganho de produtividade, reduzindo o risco de conflitos de dependências de um projeto.

Como exemplo prático podemos utilizar esta tecnologia para testar a compatibilidade do projeto com versões mais novas de Python.



Dependendo dos requisitos do seu projeto pode ser interessante ter um controle restrito quanto às dependências utilizadas, nem sempre utilizar a versão mais nova de determinada dependência é melhor.
Uma grande atualização pode resultar em quebra seu projeto, pode ocorrer problemas de retrocompatibilidade.

Com a utilização de ambientes virtuais cada projeto pode utilizar versões distintas de pacotes e versões do Python.

### Termos Importantes

* **Gerenciador de pacotes**: é uma coleção de ferramentas que permite automatizar o processo de instalação, atualização, configuração e remoção de aplicações.
Por exemplo (apt, aptitude, conda e pip).
* **Gerenciador de ambientes**: é uma ferramenta que permite criar e gerenciar ambientes virtuais.
* **Conda**: é um gerenciador de pacotes e de ambiente de código aberto, que permite instalar pacotes diversos.
* **Anaconda**: é um conjunto com milhares de pacotes (`1500` pacotes), incluindo conda, numpy, scipy, jupyter lab e outros.
* **Miniconda**: é um conjunto mínimo de pacotes no qual somente está incluindo o Python, conda e as suas dependências. A partir da instalação do miniconda é possível instalar o anaconda.
* **Venv**: é um utilitário para criação de ambientes virtuais leves.
O módulo venv fornece suporte para a criação de “ambientes virtuais” leves com seus próprios diretórios de site, opcionalmente isolados dos diretórios de site do sistema. Cada ambiente virtual possui seu próprio binário Python (que corresponde à versão do binário usado para criar esse ambiente) e pode ter seu próprio conjunto independente de pacotes Python instalados nos diretórios do site.
* **repositório** : é o local onde os pacotes estão armazenados, podendo ser instalados a partir desse local.
* **PyPI**: é o repositório oficial de aplicações Python.
* **pip**: é um gerenciador de pacotes comumente utilizado para instalação de aplicações Python hospedas no repositório PyPI.

### Utilizar Conda ou Venv

Ambas as ferramentas permitem criar e gerenciar ambientes virtuais, porém para ciência de dados o conda com o anaconda é o mais adequado.
Uma vez que ele já combina um gerenciador de pacotes de ambiente e uma coleção de aplicações adequada para ciência de dados.

<!-- Porém um resumo geral é o seguinte:

Se queremos instalar uma aplicação python que somente está disponível no PyPI utilizamos
direto do desenvolvedor utilizamos o PyPI. -->

Saiba mais sobre isso no endereço [aqui](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html?#why-use-venv-based-virtual-environments)

### Anaconda ou Miniconda?

A instalação de um ambiente de `data science` utilizando o anaconda já resulta na instalação do ambiente completo (com mais 1500 pacotes de código aberto).
Caso tenha limitação de espaço (menos de 3 GB), ou prefira instalar somente os pacotes que você for utilizar use o miniconda.
Você pode conferir mais sobre este assunto [aqui](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html?#anaconda-or-miniconda)

## Instalando um ambiente completo de Ciência de dados

Agora vamos à parte prática.
Neste tópico, vamos aprender a realizar a instalação de um ambiente completo
de ciência de dados no Linux utilizando o Anaconda com Python na versão 3.8.
Este tutorial foi desenvolvido utilizando a distribuição Linux `Ubuntu` na sua versão 20.04.

Caso esteja em um ambiente Windows siga o tutorial no site do anaconda:

* [Instalador Windows](https://docs.anaconda.com/anaconda/install/windows/)

No ambiente Linux, o primeiro passo da criação do nosso ambiente de trabalho consiste no download do anaconda.

Abra o terminal e vamos realizar o download da versão mais recente utilizando o CURL.
Caso prefira, você também pode baixar a versão mais recentemente acessando
o site do [anaconda](https://www.anaconda.com/products/individual).

Após abrir o terminal se desloque para o diretório temporário (`/tmp`):

``` console
cd /tmp
```

Agora cole no terminal o seguinte endereço:

``` console
curl https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh --output anaconda.sh

```
Agora vamos conferir a integridade do pacote com o `SHA256`.

``` console
sha256sum anaconda.sh
```

Com isso vamos obter uma saída como a apresentada abaixo:

``` console
2751ab3d678ff0277ae80f9e8a74f218cfc70fe9a9cdc7bb1c137d7e47e33d53 anaconda.sh
```

Agora vamos executar o `shell script` para realizar a instalação do anaconda.
No terminal execute:

``` console
bash anaconda.sh
```

A saída no terminal será a tela abaixo:

``` console
    Welcome to Anaconda3 2021.05
    In order to continue the installation process, please review the license
    agreement.
    Please, press ENTER to continue
   >>>
```

Agora digite ENTER para ler a licença completa.

Após realizar a leitura completa você irá visualizar a seguinte saída

``` console
Do you accept the license terms? ``[yes|no]``
```

Concordando, digite ``yes``

Agora no terminal você pode digitar ENTER para confirmar o local de instalação:

``` console
   Anaconda3 will now be installed into this location:
   /home/carlosmagno/anaconda3

   - Press ENTER to confirm the location
   - Press CTRL-C to abort the installation
   - Or specify a different location below

   [/home/carlosmagno/anaconda3] >>>
```

Aguarde a instalação, ao final podemos ativar o ambiente, com a linha a seguir:

> Essa etapa pode ser demorada dependendo da sua conexão com a internet.

``` console
source $HOME/anaconda3/bin/activate
```

Após este processo, você vai estar dentro do ambiente virtual, como apresentado
a seguir:

``` console
(base) username@ubuntu: ~$
```

## Explorando o ambiente

Agora vamos explorar o ambiente.
Você pode desativar o ambiente digitando `conda deactivate`.

Para listar todas as aplicações instaladas execute:

``` console
conda list
```

Você receberá como saída uma lista com todas as aplicações que estão instaladas.
Veja o exemplo a seguir de saída:

``` console
# packages in environment at /home/carlosmagno/anaconda3:
#
# Name                    Version                   Build  Channel
_ipyw_jlab_nb_ext_conf    0.1.0                    py38_0
_libgcc_mutex             0.1                        main
alabaster                 0.7.12             pyhd3eb1b0_0
anaconda                  2021.05                  py38_0
anaconda-client           1.7.2                    py38_0

…..                              ……                      …...

```

Parabéns! Agora você tem um ambiente completo para trabalhar com `data science`.
Porém vamos continuar a nossa exploração do ambiente, apresentando como acessar a interface web do anaconda, criação de um novo ambiente, instalação de um novo pacote e distribuição.

## Acessando a interface web

O Anaconda possui uma interface web, que pode facilitar a instalação de novos pacotes, sendo uma alternativa a utilização do utilitário de linha de comando. Por meio desta interface podemos criar novos ambientes, instalar novos pacotes e acessar facilmente IDEs, JupyterLab e outras ferramentas de desenvolvimento.

Para abrir o `anaconda-navigator` digite no console:

```console
anaconda-navigator
```

## Criando um novo ambiente com Python 3.7

Agora explorando o utilitário de linha de comando, vamos criar um novo ambiente com uma versão específica do Python.
Vamos criar um novo ambiente com a versão do Python 3.7, por default instalamos o anaconda com o Python na sua versão 3.8.

Podemos verificar a versão padrão do Python com comando a seguir:

``` console
python --version
```

> Dica: Caso tenha dúvida em algum comando você pode executar o comando de ajuda ``conda --help``.

Antes de criar o novo ambiente vamos listar os ambientes que já estão criados com o comando a seguir:

``` console
conda env list
```

Como resultado, vamos obter uma lista como a apresentada a seguir:

``` console
# conda environments:
#
base                  *  /home/username/anaconda3

```

O * indica o ambiente que está ativo no momento.

Agora, que você já sabe como listar os ambientes que já foram criados, vamos criar um novo ambiente.
Para criar um novo ambiente utilizamos o comando ``create``, como apresentado a seguir:

``` console
conda create --name <ENVNAME> python=3.7
```

Como exemplo, vamos criar um ambiente chamado tutorial, substituindo o ENVNAME por tutorial, executando o comando create vamos encontrar uma tela como a seguir:

``` console
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/carlosmagno/anaconda3/envs/tutorial

  added / updated specs:
    - python=3.7


The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main
  ca-certificates    pkgs/main/linux-64::ca-certificates-2021.4.13-h06a4308_1
  certifi            pkgs/main/linux-64::certifi-2020.12.5-py37h06a4308_0
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.33.1-h53a641e_7
  libffi             pkgs/main/linux-64::libffi-3.3-he6710b0_2
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-9.1.0-hdf63c60_0
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-9.1.0-hdf63c60_0
  ncurses            pkgs/main/linux-64::ncurses-6.2-he6710b0_1
  openssl            pkgs/main/linux-64::openssl-1.1.1k-h27cfd23_0
  pip                pkgs/main/linux-64::pip-21.1.1-py37h06a4308_0
  python             pkgs/main/linux-64::python-3.7.10-hdb3f193_0
  readline           pkgs/main/linux-64::readline-8.1-h27cfd23_0
  setuptools         pkgs/main/linux-64::setuptools-52.0.0-py37h06a4308_0
  sqlite             pkgs/main/linux-64::sqlite-3.35.4-hdfb4753_0
  tk                 pkgs/main/linux-64::tk-8.6.10-hbc83047_0
  wheel              pkgs/main/noarch::wheel-0.36.2-pyhd3eb1b0_0
  xz                 pkgs/main/linux-64::xz-5.2.5-h7b6447c_0
  zlib               pkgs/main/linux-64::zlib-1.2.11-h7b6447c_3


Proceed ([y]/n)?

```

Agora vamos confirmar a criação do ambiente com [y]

``` console
Proceed ([y]/n)? y
```

Ao final do processo aparecerá uma tela como a seguir:

``` console
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
# $ conda activate tutorial
#
# To deactivate an active environment, use
#
# $ conda deactivate

```

Como apresentado podemos ativá lo usando o comando `conda activate`.
No terminal vamos ativar o ambiente `tutorial` com o comando a seguir:

``` console
conda activate tutorial
```

Podemos checar a versão do Python:

``` console
python --version
```

Vamos obter a sesguinte saída:

``` console
(tutorial) $ python --version
Python 3.7.10
```

Agora podemos listar os pacotes que estão instalados neste ambiente com o comando:

``` console
conda list
```

Agora vamos instalar um pacote para exemplificar como funciona o sistema de instalação de aplicações, podemos instalar o `IPython`.
No terminal digite:

```console
conda install ipython
```

Ao final da instalação podemos abrir o interpretador com o comando `ipython`:

``` python
ipython
```

Obtendo uma tela como apresenta a seguir:

``` python
Python 3.7.10 (default, Feb 26 2021, 18:47:35)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.22.0 -- An enhanced Interactive Python. Type '?' for help.
In[1]:
```

Como um exemplo simples, podemos escrever a linha de código `Alô mundo`:

``` python
In [1]: print(“Alo mundo”)
Alo mundo
In [2]:
```

No momento não vamos apresentar mais pontos sobre esse interpretador, mas não se preocupe ele será apresentado novamente na introdução a Python. Porém, tenha em mente que o interpretador interativo IPython é um recurso rico para se explorar a linguagem Python.

Para sair do interpretador podemos digitar ```quit```

Agora vamos continuar a nossa exploração, conhecend brevemente o comando de canais.
## Canais

> Dica: Antes de começar essa seção do tutorial você deve estar com um ambiente ativo.

> Dica: Pode ser interessante você criar um novo ambiente ou utilizar um ambiente diferente do ambiente `base`.

Um recurso interessante disponível no conda é chamado de `conda channel`, que são os locais
onde os pacotes do conda estão armazenados. Por padrão o repositório do anaconda é utilizado
como fonte principal destes pacotes. Mas podemos requisitar pacotes de outras fontes
através do comando ``channel``. Como exemplo vamos definir como fonte dos pacotes o repositório `conda-forge`.
Vamos especificar um canal para realizar o download do pacote `pandas`.

> (Conda-forge)[https://conda-forge.org/] é um canal mantido pela comunidade que possui milhares de pacotes.

``` console
conda install pandas --channel conda-forge
```
Como resultado vammos encontrar uma tela similar a seguinte:

```
## Package Plan ##

  environment location: /home/carlosmagno/anaconda3/envs/teste2

  added / updated specs:
    - pandas


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2020.12.5  |       ha878542_0         137 KB  conda-forge
    certifi-2020.12.5          |   py37h89c1867_1         143 KB  conda-forge
    libblas-3.9.0              |       8_openblas          11 KB  conda-forge
    libcblas-3.9.0             |       8_openblas          11 KB  conda-forge
    libgfortran-ng-7.5.0       |      h14aa051_19          22 KB  conda-forge
    libgfortran4-7.5.0         |      h14aa051_19         1.3 MB  conda-forge
    liblapack-3.9.0            |       8_openblas          11 KB  conda-forge
    libopenblas-0.3.12         |pthreads_hb3c22a3_1         8.2 MB  conda-forge
    numpy-1.19.4               |   py37h7e9df27_1         5.2 MB  conda-forge
    pandas-1.1.4               |   py37h10a2094_0        10.5 MB  conda-forge
    python-dateutil-2.8.1      |             py_0         220 KB  conda-forge
    python_abi-3.7             |          1_cp37m           4 KB  conda-forge
    pytz-2021.1                |     pyhd8ed1ab_0         239 KB  conda-forge
    six-1.16.0                 |     pyh6c4a22f_0          14 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        25.9 MB

The following NEW packages will be INSTALLED:

  libblas            conda-forge/linux-64::libblas-3.9.0-8_openblas
  libcblas           conda-forge/linux-64::libcblas-3.9.0-8_openblas
  libgfortran-ng     conda-forge/linux-64::libgfortran-ng-7.5.0-h14aa051_19
  libgfortran4       conda-forge/linux-64::libgfortran4-7.5.0-h14aa051_19
  liblapack          conda-forge/linux-64::liblapack-3.9.0-8_openblas
  libopenblas        conda-forge/linux-64::libopenblas-0.3.12-pthreads_hb3c22a3_1
  numpy              conda-forge/linux-64::numpy-1.19.4-py37h7e9df27_1
  pandas             conda-forge/linux-64::pandas-1.1.4-py37h10a2094_0
  python-dateutil    conda-forge/noarch::python-dateutil-2.8.1-py_0
  python_abi         conda-forge/linux-64::python_abi-3.7-1_cp37m
  pytz               conda-forge/noarch::pytz-2021.1-pyhd8ed1ab_0
  six                conda-forge/noarch::six-1.16.0-pyh6c4a22f_0

The following packages will be UPDATED:

  certifi            pkgs/main::certifi-2020.12.5-py37h06a~ --> conda-forge::certifi-2020.12.5-py37h89c1867_1

The following packages will be SUPERSEDED by a higher-priority channel:

  ca-certificates    pkgs/main::ca-certificates-2021.4.13-~ --> conda-forge::ca-certificates-2020.12.5-ha878542_0


Proceed ([y]/n)?

```

Observe que a fonte do programa a ser instalado é o `conda-forge`.
Agora, você pode confirmar ou cancelar a instalação.

Pronto, com isso aprendemos o básico sobre canais de distribuição de aplicações
no conda, para saber mais sobre isso você pode acessar o endereço a seguir:

* <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html>

> Outro repositório interessante é o (bioconda)[https://bioconda.github.io/], focado em ferramentas de bioinformática.

## Distribuição

Um recurso interessante a ser explorado quando desenvolvemos uma aplicação e a sua possibilidade de distribuição.
Caso queira portar as dependências do seu projeto para distribuição podemos utilizar a seguinte estratégia:

Dentro de um ambiente virtual execute o comando abaixo.

``` console
conda env export --file requirements.yml
```

## Criando um ambiente a partir do *.yml

Agora para criar um ambiente a partir de um arquivo podemos utilizar o comando
a seguir:

``` console
conda env create -f requirements.yml
```

Agora você pode ativar o ambiente utilizando o comando `conda activate` como apresentado
a seguir:

``` console
conda activate env_name
```

Parabéns, com isso concluímos o nosso tutorial sobre ambientes virtuais.

### Comandos úteis e guias

Consulte uma lista com os principais comandos do conda e anaconda.

* [Conda_cheatsheet](guias/conda-cheatsheet.pdf)
* [Anaconda_starter_guide](guias/Anaconda-Starter-Guide.pdf)

Por hoje é isso, sem mais delongas divirta-se e explore.

Fontes:

* <https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-conda>
* <https://docs.python.org/pt-br/3/library/venv.html?highlight=venv>
* <https://docs.python.org/pt-br/3/>
* <https://www.anaconda.com/>
* <https://docs.conda.io/projects/conda/en/latest/user-guide/index.html>
* <https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-20-04-pt>
