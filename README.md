<p id="start" align="center">
<h1 align="center"><a href="https://www.tansoftware.com">TANSOFTWARE</a></h1>
<p align="center">
<a href="#english">English</a>  | <a href="#french">French</a> 
</p>
<hr>
<!-- ENGLISH VERSION -->
<h3 id="english">Automatic publication on LinkedIn.</h3>
</p>
<table>
<tr>
<td>
<h3>Legal contribution :</h3>
<ul>
    <li>This is a public repository.</li>
    <li>You can freely copy this folder.</li>
    <li>You can also <strong>participate</strong> by issuing pull requests.</li>
</ul>
<img width="1000" height="0">
</td>
</tr>
</table>
</p>
<p align="center">
<a href="#prerequisites_eng">Prerequisites</a> | <a href="#use_eng">Use</a>  | <a href="#version">Version</a> 
</p>

<h2 id="prerequisites_eng">Prerequisites</h2>

<ol>
    <li>Install python 3 </li>
    <li>Install pip </li>
    <li>Modify the "<strong>access_token</strong>" and "<strong>urn</strong>" variables, found in the "<strong>.env</strong>" file</li>
    <li>Enter the following command
    <span></span>

```python
pip install -r requirements.txt
 ```

</li>
</ol>

<h2 id="use_eng">Use</h2>

<ul>
    <span>Enter the following command</span>
    <span></span>

```python
python main.py
 ```
</ul>
<ul>
You have three choices:

```bash
1 - To generate a "docx" in which you write your post.
During its generation, you will be asked what date and 
time you want it to be posted.
You can generate as many as you want.
```
   
```bash
2 - Launch the program in the background, so that it looks
every hour at the documents you have generated.
And that they send them to your LinkedIn account, as a post.
```

```bash
3 - Launch a connection test to verify that the "access_token"
and "urn" elements entered are the correct ones.
```
</ul>
<hr>
<!-- FRENCH VERSION -->
<h3 id="french">Publication automatique sur LinkedIn.</h3>
</p>
<table>
<tr>
<td>
<h3>Contribution légale :</h3>
<ul>
    <li>Ceci est un dépôt public.</li>
    <li>Vous pouvez copier librement ce dossier.</li>
    <li>Vous pouvez aussi y <strong>participer</strong> en émettant des pull requests.</li>
</ul>
<img width="1000" height="0">
</td>
</tr>
</table>
</p>
<p align="center">
<a href="#prerequisites_french">Prérequis</a> | <a href="#use_french">Utilisation</a>  | <a href="#version">Version</a> 
</p>

<h2 id="prerequisites_french">Prérequis</h2>

<ol>
    <li>Installez python 3 </li>
    <li>Installez pip </li>
    <li>Modifiez les variables "<strong>access_token</strong>" et "<strong>urn</strong>" présentes dans le fichier "<strong>.env</strong>"</li>
    <li>Entrez la commande suivante
    <span></span>

```python
pip install -r requirements.txt
 ```

</li>
</ol>

<h2 id="use_french">Utilisation</h2>

<ul>
    <span>Entrez la commande suivante</span>
    <span></span>

```python
python main.py
 ```
</ul>
<ul>
Trois choix s'offrent à vous:

```bash
1 - De générer un "docx" dans lequel vous écrivez votre post.
Durant sa génération, il vous sera demandé à quelle date et 
à quelle heure, vous souhaitez qu'il soit posté.
Vous pouvez en générer autant que vous le désirez.
```
   
```bash
2 - De lancer le programme en tache de fond, afin qu'il regarde 
toutes les heures, les documents que vous avez générés.
Et qu'ils les envoient sur votre compte LinkedIn, sous forme de post.
```

```bash
3 - De lancer un test de connexion afin de vérifier que les éléments 
renseignés "access_token" et "urn", soit les bons.
```
</ul>

<h2>Version</h2>

```
0.0.1
```


