# This Python file uses the following encoding: utf-8
from flask import Flask, render_template, request, Markup
import watson_developer_cloud, time, os

# Aqui estamos criando um objeto da classe Flask e, em seguida, atribuindo-o à variável 'app'.
app = Flask(__name__)

# Criação de um Array para armazenar as mensagens do usuário e do Bot.
conversa = []


tamanhoAtual = 0

# Usamos o route para registrar a função webprint e carregar a página index.html para uma determinada regra de URL.
@app.route('/')
def webprint():
    return render_template('index.html')

# Configuração do Serviço de Assistente
service = watson_developer_cloud.AssistantV1(
version = '2018-07-10',
url = 'https://gateway.watsonplatform.net/assistant/api',
iam_apikey = 'BLiVAW-VPiFWoFBPItsKqbrON90JIjKnNrQc1ELL3mEK')
workspace_id = 'e3e2b796-7c3d-44d1-9016-b5fe3d7e83cb'

# Criação da Função de Conversa do Robô
def iniciaConversa():
    user_input = request.form['textField']
    context = {}
    current_action = ''
    response = service.message(workspace_id = workspace_id, input = {'text': user_input}, context = context)
    context = response.result['context']

    #global user_response
    #global bot_response
    conversa.append('> ' + request.form['textField'])

    i = 0
    while i < len(response.result['output']['text']) :
        conversa.append(response.result['output']['text'][i])
        i += 1

    global tamanhoAtual
    tamanhoAtual = len(conversa)


# Usamos o route para registrar a função my_form_post e carregar a página index.html com as respostas do diálogo.
@app.route('/', methods=['POST'])
def my_form_post():
    temp = tamanhoAtual
    iniciaConversa()
    difTamanho = tamanhoAtual - temp
    ultimaConversa = []
    i = difTamanho
    while i > 0 :
        ultimaConversa.append(conversa[tamanhoAtual - i])
        i -= 1

    return render_template('index.html', conversa = ultimaConversa)

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
