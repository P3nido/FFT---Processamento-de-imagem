Esse foi um projeto apresentado em sala de aula na matéria de Análise de Sinais e Sistemas.

O projeto consiste em uma reconstrução de uma imagem utilizando os cálculos presentes na transformada de Fourrier, no qual após o processamento do mesmo, a imagem se torna mais nítida e com menas interferências presentes. Os passos são os seguintes:
1 - Primeiramente a imagem é carregada e é convertida para tods de cinza
2 - Realiza o pré processamento aplicando a transformada rápida de Fourrier
3 - Realiza o deslocamento de quadrantes utilizando a biblioteca FFT Shift em Python
4 - Realiza a centralização com operações utilizando o domínio da frequência
5 - Filtragem é aplicada promovendo o deslocamento inverso dos quadrantes da imagem processada, utilizando a função Inverse Shift em Python
6 - Após todo o processamento aplica a transformada inversa de Fourrier para que a imagem consiga ser transformada inversamente até obter o módulo com a sua devida normalização

Após todo esse processo a nova imagem é baixada e junto a ele, um novo png é instalado na mesma pasta do arquivo no qual realiza um comparativo entre as imagens pré processadas, com pós processadas.
