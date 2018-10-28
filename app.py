from flask import Flask, render_template, request, Markup
import watson_developer_cloud
import time

app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)


user_response = []
bot_response = []

@app.route('/')
def webprint():
    return render_template('index.html')

# Set up Assistant service.
service = watson_developer_cloud.AssistantV1( username = '41fc5432-d6e8-4bd2-8ea0-4367c642bcd0', password = 'xMvynkPPQFwX', version = '2018-02-16' )
workspace_id = '31dd6267-459f-4df8-a135-575731dc5f0a'

def iniciaConversa():
    entradaUsuario = request.form['textField']
    user_input = entradaUsuario
    context = {}
    current_action = ''
    response = service.message(workspace_id = workspace_id, input = {'text': user_input}, context = context)
    context = response.result['context']

    if user_input != '':
        response = service.message(workspace_id = workspace_id, input = {'text': user_input}, context = context)
        print(entradaUsuario)
        print(response.result['output']['text'][0])


    global user_response
    global bot_response
    user_response.append(request.form['textField'])
    bot_response.append(response.result['output']['text'][0])

@app.route('/', methods=['POST'])
def my_form_post():
    iniciaConversa()
    return render_template('index.html', user_response=user_response, bot_response=bot_response)
app.run()
