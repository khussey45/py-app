from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_prompt', methods=['POST'])
def check_prompt():
    prompt = request.json['prompt']
    if 'code' in prompt:  # Simplified condition
        return jsonify({'show_vscode': True})
    return jsonify({'show_vscode': False})

if __name__ == '__main__':
    app.run(debug=True)
