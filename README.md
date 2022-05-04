Sistema de monitoramento client-servidor

Este é um projeto realizado na disciplina Laboratório de Redes do curso Bacharelado em Engenharia Elétrica do Instituto Federal do Espírito Santo. Este projeto consiste em 2 programas, um rodará na máquina client que realizará omonitoramento da conexão de certos endereços com a internet, a resposta HTTP e o estado do DNS. Estas informações serão transmitidas para a máquina servidor através de um socket, este receberá os dados e irá exibi-los em uma página Web com o auxílio de um servidor local utilizando o Apache.


COMO RODAR A APLICAÇÃO

1 - Para rodar a aplicação, deve-se ter o Docker instalado, caso não tenha poderá obter informações sobre a instalação em: https://docs.docker.com/get-docker/

2 - Baixe a imagem Docker do cliente na máquina cliente utilizando o seguinte comando:  

    docker pull vinihernech/client_and_server_monitoring:client_image
    
3 - Baixe a imagem Docker do servidor na máquina servidor utilizando o seguinte comando:

    docker pull vinihernech/client_and_server_monitoring:server_image
        
4 - Baixe a imagem do Apache na máquina servidor utilizando o seguinte comando:

    docker pull httpd
 
4 - Verifique se as imagens foram baixadas utilizando o comando:

    docker images ls

5 - O primeiro container a ser inicializado é o do servidor Apache, este deve ser iniciado dentro da pasta "Html"

    docker run -it --rm --name myapache-app -p 8080:80 -v "$PWD":/usr/local/apache2/httpd
    
6 - O próximo container a ser inicializado é o do servidor, este também deverá ser iniciado dentro da pasta "Html"
    
    docker run -it --rm --network=host -v "$(pwd):/var/www/html" --name=server server-image
    
Perceba que o container roda no modo iterativo, esta aplicação requisitará do usuário o número de IP e porta para realizar a conexão com o client através do socket, o IP a ser informado é o IP local da máquina que está rodando o servidor, e a porta fica a escolha do usuário, recomenda-se portas como: 50000, 60000.

7 - Após subir os containers anteriores é hora de subir o último container, o do client, antes disso é necessário editar o arquivo config.txt que se encontra dentro da pasta config. Este arquivo deverá conter o número de IP e porta (os mesmos informados no servidor). As próximas 3 linhas do arquivo são respectivamente um IP qualquer no qual deseja-se realizar o monitoramento, um endereço eletrônico qualquer e por último o IP do access point.

8 - O container do client deverá ser inicializado no diretório que contém a pasta "config":
 
    docker run --rm --network=host -v "$(pwd):/config" --name-client client_image python3 teste.py
    
9 - Após a inicialização dos 3 containers a aplicação deverá estar funcionado, você pode verificar o monitoramento através do servidor WEB inicializado pelo Apache, você pode acessá-lo através de qualquer navegador pelo endereço: SEU_IP_LOCAL:8080 .
