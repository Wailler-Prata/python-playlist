<p>Esse é um exemplo de como podemos utilizar assincronismo para aumentarmos a performance do nosso código.</p> 
<p>Esse exemplo é dividido entre três arquivos:</p>

<ul>
<li>pokedex_not_optimized</li>
<li>pokedex_optimized</li>
<li>comparative_class</li>
</ul>


<p>No arquivo <b>pokedex_not_optimized</b>, para capturarmos nossos pokemons, iremos usar a biblioteca padrão do python <b>requests<b/>. 
Perceba que é um código síncrono, onde requisitamos um pokemon, instanciarmos um objeto com os atributos desse pokemnon e o salvamos em uma lista.</p>

<p>Toda a execução se encontra dentro da função <b>main_class_not_optmized</b>. Somente requisitamos outro pokemon após retorno da requisição atual e salvamento do pokemon requisitado em uma lista de objetos.</p>


<p>O problema disso, é que, em uma consulta a uma API externa, como é o nosso caso, certamente teremos vários fatores que podem comprometer a performance do nosso software em função de software terceiro. Os motivos podem ser diversos, como disponibilidade do servidor, latência e etc.</p>

<p>Para otimizar essas requisições, elaborei o código do exemplo <b>pokedex_optimized</b>, neste utilizaremos as bibliotecas <b>asyncio</b> e <b>httpx</b> para realizar nossas requisições.</p>

<p>Para facilitar nosso código, construi uma interface com a biblioteca <b>asyncio</b>. Essa interface foi definida por meio da função <b>execute_async</b>. Essa função recebe como atributo uma lista de funções. Em python, funções são cidadãos de primeira classe, então conseguimos armazena-las em uma variável, objeto, lista e etc.</p>

<p>Na execução do programa por meio da função <b>main_optmized</b> encaminhamos todas as requisições para a função <b>execute_async</b> por meio de um list comprehension. A diferença aqui é que a biblioteca <b>httpx</b> irá fazer todos os requests "ao mesmo tempo" e recebe o retorno da API na conforme o tempo de retorno da mesma.</p>
