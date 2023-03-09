<!-- Shodan CLI -->
<h1>Shodan CLI</h1>

<p>Este script de Python utiliza la librería Shodan para realizar búsquedas en internet y devolver información sobre los dispositivos y servicios encontrados.</p>

<h2>Requisitos</h2>

<p>Antes de ejecutar este script, asegúrese de tener instaladas las siguientes dependencias:</p>

<ul>
  <li>shodan</li>
  <li>argparse</li>
</ul>

<p>Puede instalar estas dependencias utilizando el siguiente comando:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<h2>Uso</h2>

<p>Para utilizar este script, ejecute el siguiente comando en la línea de comandos de Python:</p>

<pre><code>python SHODAN_CLI.py -q consulta</code></pre>

<p>Donde <code>buscador_shodan.py</code> es el nombre del archivo del script que se va a ejecutar y <code>consulta</code> es la consulta que se desea realizar en el motor de búsqueda de Shodan.</p>

<p>Por ejemplo, si se desea buscar información sobre dispositivos que tengan la palabra "webcam" en su descripción, se puede ejecutar el siguiente comando:</p>

<pre><code>python SHODAN_CLI.py -q webcam</code></pre>

<p>El script buscará en la base de datos de Shodan todos los dispositivos que contengan la palabra "webcam" en su descripción y mostrará información sobre los dispositivos encontrados, incluyendo su dirección IP y los puertos abiertos.</p>

<h2>Notas</h2>

<p>Es importante tener en cuenta que el web scraping puede no ser legal en algunos casos y que algunas páginas web pueden tener medidas de seguridad para evitar la extracción de datos. Es importante asegurarse de tener permiso para extraer datos de una página web y de no infringir ninguna ley o regulación en el proceso.</p>
