# BongoCatPy!
<br>
<br>
<p align="center">
  <img width="272" height="322" src="https://raw.githubusercontent.com/josalesmj/pyCatKeyboard/master/bongocat.gif">
</p>
<br>

# 1. Descrição do Projeto
O projeto consiste em um "listener" monitorando, em segundo plano, o pressionamento das teclas e então realizamos a troca da imagem que é exibida na janela. 
<br>
<br>
Para a construção da janela foi utilizadas as bibliotecas "tkinter" e "PIL".
<br>
<br>
Para a construção do listener, utilizamos a biblioteca pynput.
<br>
<br>
Utilizamos a biblioteca "threading" para que o monitoramento do pressionamento de teclas rodasse em paralelo com a thread da janela. Também utilizamos um timer da biblioteca "threading" para alterar a imagem da janela para a inicial, caso nenhuma tecla for pressionada após um pequeno tempo.
<br>
<br>
No menu do topo, podemos configurar o redinmensionamento da janela; selecionar se estará sempre ou não no topo e a exibição da quantidade de teclas digitadas. Também foi adicionado a criação de um arquivo 'config' para manter as configurações da tela para não ser necessário redimensionar e posicionar sempre que abrir novamente. 
<br>
<br>
<p align="center">
  <img width="272" height="322" src="https://raw.githubusercontent.com/josalesmj/BongoCatPy/master/bongocat1.gif">
</p>
<br>
Para utilização, mantenha o executável e a pasta "image" no mesmo diretório.
<br>
<br>
Caso prefira gerar o próprio executável, após instalar o pyinstaller, rode o comando a seguir:
<br>
<br>

```
pyinstaller.exe --noconsole --onefile class.py
```

## Inspiração
<br>
A inspiração para o projeto se deu a partir de um vídeo semelhante ao apresentado a seguir:

<br>
<br>
<p align="center">
  <a href="https://www.youtube.com/watch?v=tvg6vvs0WbM" target="_blank">
  <img width="400" height="400" src="https://img.youtube.com/vi/tvg6vvs0WbM/0.jpg">
</p>
<br>

## Contato ou sugestões
<br>
Qualquer sugestão de melhoramento de código, ou correção, pode entrar em contato comigo por aqui ou através das minhas redes:<br>
E-mail: jo.salesmj@gmail.com<br>
Linkedin: <a href="linkedin.com/in/jó-salesmj/">https://www.linkedin.com/in/jó-salesmj/</a>
  <br>
Instagram: @jo.salesmj
