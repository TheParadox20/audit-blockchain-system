import os
from flask import Flask, send_from_directory, request
from flask_cors import CORS
from persistence.explorer import Explorer
from block_chain.operation import Operation
from block_chain.account import Account

app = Flask(__name__, static_folder='UI/frontend/dist')

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)

CORS(app)

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

#Initialize account
user = Account()

@app.route('/tx')
def enterTx():
    Operation()

@app.route('/login')
def login():
    pass

@app.route('/recover')
def recover():
    mnemonic = ''
    user.genAccount(mnemonic)
