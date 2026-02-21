# Projeto: Reconstrução de Imagem via Transformada de Fourier

Este projeto foi desenvolvido e apresentado como parte da disciplina de **Análise de Sinais e Sistemas**.

## 📝 Descrição do Projeto
O objetivo principal é a reconstrução e melhoria de imagens utilizando conceitos da **Transformada de Fourier**. Através do processamento no domínio da frequência, o algoritmo consegue tornar a imagem mais nítida e reduzir interferências (ruídos) presentes no arquivo original.

## ⚙️ Fluxo de Processamento
O algoritmo segue as etapas abaixo para o processamento do sinal visual:

1. **Conversão de Escala:** A imagem original é carregada e convertida para tons de cinza.
2. **Domínio da Frequência:** Aplicação da Transformada Rápida de Fourier (**FFT**).
3. **Deslocamento de Quadrantes:** Utilização da biblioteca `fftshift` (Python) para organizar os componentes de frequência.
4. **Centralização:** Operações matemáticas realizadas diretamente no domínio da frequência para focar nos componentes principais.
5. **Filtragem e Inversão:** - Aplicação de filtros para redução de ruído.
   - Realização do deslocamento inverso utilizando a função `ifftshift` (Inverse Shift).
6. **Reconstrução:** Aplicação da Transformada Inversa de Fourier (**IFFT**) para retornar ao domínio espacial, obtendo o módulo e realizando a devida normalização da imagem.

## 📊 Resultados
Ao final do processo, o algoritmo:
* Gera e baixa a nova imagem processada.
* Salva automaticamente um arquivo `.png` comparativo na pasta do projeto, facilitando a visualização das diferenças entre a imagem **Pré-processada** e a **Pós-processada**.

---
*Desenvolvido para fins acadêmicos.*
