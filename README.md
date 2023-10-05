<h1 align="center">Projeto Login System</h1>

<h2>Descrição 📃</h2>
<p>Esse código é responsável por criar uma tela de login e registro de usuários utilizando a biblioteca PySimpleGui.</p>

<p>O sistema utiliza um algoritmo que reconhece novos usuário e os já cadastrados, comparando senhas e nomes de usuário.<br>
  Além disso o código utiliza a biblioteca Bcrypt para encriptar as senhas com salt e hash. Os dados de novos usuários<br>
  são armazenados em um arquivo txt, o registro de login de usuários já existentes também.<br>
  Após fazer o registro, o usuário recebe um email confirmando o cadastro através da biblioteca Smtplib, utilizando<br>
  a porta 587, específica do Gmail.</p>

<p>A senha do email do remetente está à mostra, mas é indicado utilizar uma variável de ambiente ou arquivo de configuração<br>
  mantendo a integridade do email e do sistema.<br>
  Os arquivos txt podem ser substituídos por um banco de dados, basta integrar o DB ao código, alterando algumas linhas.</p>

<h2>Status do Projeto ⌛</h2>
   
 ![Static Badge](https://img.shields.io/badge/status-finished-green)

<h2>Como usar 👣</h2>
<p>Para utilizar, você deve configurar o email e a senha de remetente na função "send_mail" nas variáveis "msg[From]" e "password"<br>
  e startar o código. Aparecerá a tela de login, após isso, clique em registrar e registre sua conta. Você receberá um email.<br>
  Ao final a tela de login será chamada, basta colocar seu usuário e senha, se o login for validado, será encerrado a experiência.</p>
  
<h2>Tecnologias usadas ⌨</h2>
  
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

<h2>Autores</h2>

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/128868356?s=400&u=e46a4a066ab7c8789bb2ba1d68758a5471565aec&v=4" width=115><br><sub>Lucas Bezerra</sub>](https://github.com/lucaslfb)


  
