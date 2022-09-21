# Nome do Projeto 
BongoCatPy!
<br>
## Descrição do Projeto
O projeto consiste em um "listener" monitorando, em segundo plano, o pressionamento das teclas e então realizamos a troca da imagem que é exibida na janela. 
<br>
Para a construção da janela foi utilizadas as bibliotecas "tkinter" e "PIL".
Para a construção do listener, utilizamos a biblioteca pynput.
Utilizamos a biblioteca "threading" para que o monitoramento do pressionamento de teclas rodasse em paralelo com a thread da janela. Também utilizamos um timer da biblioteca "threading" para alterar a imagem da janela para a inicial, caso nenhuma tecla for pressionada após um pequeno tempo.
<br>
No menu do topo, podemos configurar o redinmensionamento da janela; selecionar se estará sempre ou não no topo e a exibição da quantidade de teclas digitadas. Também foi adicionado a criação de um arquivo 'config' para manter as configurações da tela para não ser necessário redimensionar e posicionar sempre que abrir novamente. 
<br>
Para utilização, mantenha o executável e a pasta "image" no mesmo diretório.
<br>
Caso prefira gerar o próprio executável, após instalar o pyinstaller, rode o comando a seguir:

```
pyinstaller.exe --noconsole
```
<br>
A inspiração para o projeto se deu a partir de um vídeo semelhante ao apresentado a seguir: 
<br>
<p align="center">
  <img width="272" height="322" src="https://raw.githubusercontent.com/josalesmj/pyCatKeyboard/master/bongocat.gif">
</p>

[![youtube video showing bongo cat on keyboard display](https://img.youtube.com/vi/tvg6vvs0WbM/0.jpg)](https://www.youtube.com/watch?v=tvg6vvs0WbM)
<br>
Qualquer sugestão de melhoramento de código, ou correção, pode entrar em contato comigo por aqui ou através das minhas redes:<br>
E-mail: jo.salesmj@gmail.com<br>
Linkedin: linkedin.com/in/jó-salesmj/<br>
Instagram: @jo.salesmj
