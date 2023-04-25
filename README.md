# Como foi feito
Olá Mestre Kame, dê uma olhadinha em como minha atividade foi feita:

1) Primeiramente realizei a instalação de todos os programas necessários para o setup do ambiente Linux, como WSL, Ubuntu e RO2.

2) Após isso conectei o VScode com o ambiente Linux

3) Descrevendo o código: 

  Fiz as importações de bibliotecas necessárias  
  
  Utilizei a classe TurtleController para iniciar o projeto
  
  utilizei a função create publisher para criar uma publicação no tópico que será subscrita no nodo.
  
  Criei variáveis de controle para conseguir controlar tanto as funções que serão utilizadas quanto também o tempo.
  
  Criei uma função que irá controlar qual função será utilizada no momento e em qual momento
  
  Criei as funções que irão controlar a angulação e  a direção de movimento do turtle, para isso utilizei o Node e o Twist. A classe node é utilizada para realizar a movimentação da tartaruga e a função Twist é usada para girar a tartaruga em torno do seu próprio eixo, não só isso como também a velocidade. 
  
  Para conseguir testar o projeto, foi preciso abrir alguns terminais e utilizar cada um respectivamente para: o publisher que irá publicar as mensagens para outro nó por meio do Ros2, um comando para inicializar o nó do gráfico da tartaruga e por fim rodar o script donatelo.py :)
  Todas essas interações são publicadas no tópico cmd/vel.
  
  Link para o video mostrando o funcionamento: https://drive.google.com/file/d/10vYIRANHpp3QIPO2lHv9-i_icKuHITe9/view?usp=sharing
  
  
