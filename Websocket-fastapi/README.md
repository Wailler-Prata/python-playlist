<p>Esse é um exemplo de implementação de um WebSocket usando FASTAPI</p>
<p>A divisão do nosso código se encontra da seguinte forma.</p>

<ul>
   <li>Diretório "app"
        <ul>
            <li>__init__.py: Nele temos a instância do nosso aplicativo "app", montamos o diretório de onde irá conter nossos arquivos estáticos e incluímos as nossas rotas criadas no arquivo "routes".</li>  
            <li>routes.py: Nesse arquivo temos a definição de todas as rotas da nossa aplicação.</li>
        </ul>
    </li>
    <li>Diretório "portifolio_code": Este possui um único arquivo, nesse arquivo se encontra a definido e instanciado a classe que irá gerenciar nossas conexões websocket.</li>
    <li>Diretório "templates": Aqui temos um arquivo html que será o nosso template de chat em "tempo real".</li>
	<li>Diretório "static": temos os nossos arquivos estáticos.</li>
</ul>

<p>Para facilitar o entendimento, deixei as funções JavaScript que iremos utilizar para comunicação com o websocket no arquivo html do templante</p>

<h2>Explicando o fluxo</h2>
<p>Ao executar a aplicação, por padrão do FASTAPI, estaremos rodando em 127.0.0.1:8000. Como nossa rota que renderiza o templantedo html do chat é "/", ja visualizaremos a interface do chat no navegador ao acessar o endereço citado.</p>
<p>Ao inserir um nome de usuário e clicarmos em "Entrar", enviaremos o nome de usuário para nossa função JavaScript "websocket_connect", esta verificará se o nome de usuário possui ao menos duas letras. 
Caso possua, ela conectará em nosso websocket por meio da URL `ws://${window.location.host}/ws/${client_id}/${input.value}`.
<p>Perceba que não é http ou https, as conexões websocket possuem um protocolo próprio "ws".</p>

<p>A conexão criada é atribuída a variável "ws", e na sequencia adicionamos um "addEventListener", que escutará todas as mensagens recebidas do servidor, e a cada mensagem executará a função "writeMessage".</p>

<p>Ao conectar, você ja visualizará seu avatar e nome de usuário inserido, assim como todos os demais usuários conectados. A partir desse momento, será possível encaminhar mensagens</p>
<p>As mensagens são encaminhadas ao clicar em "Enviar mensagem", onde é utilizado a função JavaScript "sendMessage"</p>

<p>Para que possua outro usuário com quem conversar, você poderá abrir uma nova conexão no chat em outro navegador, outra aba, e se estiver hosteado poderá conectar até mesmo em outro aparelho.
 Ao conectar por meio de outra aba, navegador ou aparelho, o usuário será enviado para visualização de todos os usuários ja conectados, e também, será carregado todos os usuários ja logados.</p>

<h2>Mas o que acontece por debaixo dos panos ?</h2>
<p>Ao enviar o nome de usuário para o websocket, um usuário de chat é instanciado, e adicionado ao "poll de conexões" do websocket para que possam trocar mensagens.</p>
<p>Com a confirmação do armazenamento do usuário e sua conexão, é enviado ao front-end uma confirmação de que você foi conectado. E a partir desse momento o servidor ficará aguardando que você encaminhe uma mensagem que será transmitida para todos os usuários conectados por meio do método "broadcast"</p>
<p>Quando um dos usuários conectados fechar a aba do navegador ele irá automaticamente encerrar a conexão por meio de uma exception. Sendo assim, será removido do "poll de conexões" e da interface de todos os outros usuários conectados.</p>
