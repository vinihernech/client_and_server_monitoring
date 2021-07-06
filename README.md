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

5 - O primeiro container a ser inicializado é o do servidor Apache, este deve ser iniciado dentro da pasta

    docker run -it --rm --name myapache-app -p 8080:80 -v "$PWD":/usr/local/apache2/httpd
