from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/')
def index():
    requested_file = request.args.get('file', 'Textdokument')
    
    if not requested_file:
        return 'Geben Sie den Dateinamen in der URL an, z.B.: ?file=example.txt'

    if os.path.isfile(requested_file):
        with open(requested_file, 'r') as file:
            file_content = file.read()
        return file_content
    else:
        return 'Die angegebene Datei existiert nicht.'

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
