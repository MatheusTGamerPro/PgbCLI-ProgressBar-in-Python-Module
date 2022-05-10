# PGB-CLI Module Python
PGBCLI é? uma biblioteca python, construida para que você? tenha uma bela e rapida barra de progresso
em seus codigos, você? podera personaliza-la do modo que voce desejar, adicionando cores, temas, textos e algumas outras variaç?õ?es de argumentos, a funç?ã?o que executa a barra de progreso **pgb.progressBar()** executara a barra de progresso em seu codigo.

# Como utilizar a bíblioteca?
1. a utilização do barra de progresso é rapida e simples, com a função `pgb.progressBar()`, você automaticamente chama a barra de progresso, se você nao passar argumentos para a funçãoo ela tera como padrao parametros pré definidos, mais abaixo mostrarei como utilizar os argumentos.
2. os parametros que contem na barra de progresso sao:
    - `text`
    - `color`
    - `theme`
    - `speed`
    - `total`
    - `max_upload`
3. Agora que voce sabe quais são os parametros que voce podera configurar, vamos aprender a utilizar-los!
- `text`:
    1. o parametro **text** server para que você possa definir o titulo ou descricao da sua barra de progresso, por exemplo, voce pode descer mais abaixo e ver algumas imagems de como funciona esse parametro, mas agora vamos mostrar um exemplo de uso;

        `pgbcli.progressBar(text="Baixando Python")`

    2. Fazendo isso voce configura o titulo da barra de progresso para "Baixando Python", fica mais ou menos assim: **Baixando Python: [...] 3%**, com isso voce ja sabe como configurar seu titulo!
- `color`:
    1. o parametro **color** define a cor do carregamento de sua barra, porem o parametro de cor só funciona para terminais que contem suporte a cores ASCII, então é preciso que voce tenha um terminal que funcione coloracao para utilizar esse parametro, o uso dele é assim:

        `pgbcli.progressBar(color="green")`

    2. Fazendo isso voce define a cor da barra de progresso para **verde**, as cores disponiveis são; **green, yellow, blue, red, magenta, cyan, white, none**, a cor **none** é a padrão.
- `theme`:
    1. o parametro **theme** define o tema de sua barra de carregamento, o tema padrao é ".", para utizar voce pode fazer:

        `pgbcli.progressBar(theme="=")`

    2. o tema de carregamento ficara assim: **Baixando Python [====] 4%**, voce pode deixar o tema que desejar em sua barra.
- `speed`:
    1. o parametro **speed** define a velocidade de carregamento da barra, ou seja, é o tempo que a barra avançara, sendo assim, se voce colocar *1* sera igual a cada 1 segundo, o padrão é 0.500, para alterar voce adiciona:

        `pgbcli.progressBar(speed=2)`
    2. a barra de progresso carregara a cada 2 segundo se voce definir igual acima.
- `total`:
    1. o parametro **total** configura o total final de quando o carregamento ou "download" de sua barra de progresso pode chegar, voce pode definir outra adicionando:

        `pgbcli.progressBar(total=130)`

    2. ou seja, o maximo da porcentagem sera até? 130%, igual acima.
- `max_upload`:
    1. este ultimo parametro ainda esta em testes, mas ja esta funcionando, com ele voce define a velocidade de upload de sua barra de progresso, o padrãoo é 5 (5Mbps), para definir o seu, voce usa:

        `pgbcli.progressBar(max_upload=10)`

    2. ou seja, a velocidade de "upload" da barra sera igual a 10Mbps, é literalmente a velocidade de download.

    3. voce pode configurar todos de uma vez tambem, assim:

        `pgbcli.progressBar(text="Baixando", theme="=", color="red", total=100, speed=0.500, max_upload=5)`

Beleza, com isso voce ja deve saber utilizar a biblioteca PgbCLI em seus programas. Ah, e só pra falar mesmo... as funçoes que contem o modulo são:
- `pgbcli.progressBar()`
- `pgbcli.pgb_version()`

essa ultima função server para voce ver a versão atual da biblioteca!

# Exemplos
aqui em baixo tem algums exemplos em imagems, de como é a barra de progresso em execução!

# Como baixar e importar
Por enquanto, é necessário que você instale manualmente o script da Bíblioteca. Sendo assim.. você pode pegar o repositório,
Utilizando **git clone** ou coletando o arquivo no Modo Raw.

# Dependências
Nada de mais, as únicas bibliotecas que o pgbcli utiliza são as bibliotecas padrões do Python:
- `random`
- `time`

Essas Bibliotecas são as utilizadas para o funcionamento da barra de Progresso, fica tranquilo que elas já ficam importadas!

# Recursos
- Você pode alterar a cor da barra de progresso
- A barra de Progresso fica carregando em somente 1 linha (sem fazer vários prints!).
- Você pode trocar o tema da barra de carregamento
- você pode controlar o total e velocidade da barra.
- você não precisa importar as bibliotecas **os, time** no seu código. (O modulo pgbcli já importa)
- você pode utilizar em todas as versões do Python 3+
- você pode utilizar o modulo pgbcli junto com a bíblioteca Threading

# Notas Finais
Essa biblioteca foi construída para ajudar outros desenvolvedores que utilizam a CLI (Command Line), 
Principalmente em programas que utilizem o Terminal.
