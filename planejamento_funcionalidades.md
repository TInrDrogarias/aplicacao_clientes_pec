## Sistema de Usuário e Login
- fontes:
	[] https://realpython.com/python-gui-tkinter/
- algoritmos:
1. Abrir uma página de Login.
2. Se o usuário ou senha digitado for errado, ele não deixa o usuário entrar.
3. Se sim, ele deixa.

## configurar o envio
1. importar contatos e guardar em algum lugar.
- fontes:
	[x]https://www.geeksforgeeks.org/reading-csv-files-in-python/
	[x]https://pythonspot.com/reading-csv-files-in-python/

- algoritmo:
	1. importar um csv pra dentro da página. 
	2. armazenar os nomes num array.
	3. armazenar os números num array (os dois precisam estar associados).
	4. Mudar o ícone do botão de A para B.

- algoritmo dentro do programa:
	1. itera sobre as linhas usando a biblioteca do csv.
	2. separa os caracteres pelo ponto e vírgula.
	3. armazena nas variáveis.

2. importar uma imagem e guardar em algum lugar.
- fontes:
	[]https://www.geeksforgeeks.org/pyqt5-input-dialog-python/
- algoritmo:
	1. receber uma imagem via input.
	2. guardar o endereço
	3. armazenar o endereço da imagem numa variável.
	4. Mudar o ícone do botão de C para D.

3. receber um texto e guardar em algum lugar.
- fontes:
	[]https://www.geeksforgeeks.org/pyqt5-input-dialog-python/
- algoritmo:
	1. receber um input no formulário
	2. guardar o texto numa variável ao apertar o botão.

4. exibir o código QR do What's APP.
- fontes:
	[] https://www.selenium.dev/pt-br/documentation/overview/
- algoritmo:
	1. Abrir a página do What's APP.
	2. Copiar a imagem do QR Code.
	3. Atualizar ela a cada 10s.
	4. Quando o login for um sucesso, ele deixa de carregar e muda o ícone.

- Especificidades técnicas:
1. Um lugar para guardar informações: variáveis e arquivos?

## enviar em massa essas mensagens
- fontes:
	[] https://www.selenium.dev/pt-br/documentation/overview/
- algoritmo:
1. reunir todas as variáveis com informações relevantes (nome, contato, mensagem, imagem).
2. iniciar o ciclo de envio das mensagens (início, feitura e fechamento).
3. passar para o próximo nome e contato e reiniciar o ciclo
4. fazer o passo 3 até o fim.