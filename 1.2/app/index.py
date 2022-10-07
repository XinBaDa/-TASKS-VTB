from flask import abort, Flask, jsonify, render_template, request
import os
import storage

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
storage.startup_check()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all', methods=['GET'])
def all():
    json_dict = storage.load_json()
    return jsonify(json_dict)

@app.route('/read', methods=['GET'])
def read():
    json_dict = storage.load_json()
    if request.args.get('key') and len(request.args) == 1:
        return jsonify({request.args['key']: json_dict.get(request.args['key'])})
    else:
        abort(400)

@app.route('/write', methods=['POST'])
def write():
    if (not request.json) or (isinstance(request.get_json(), dict) is False):
        abort(400)
    json_dict = storage.load_json()
    for key, val in request.get_json().items():
        storage.set_key(json_dict, key, val)
    storage.save_json(json_dict)
    return 'Success add data %s' % (str(request.get_json()))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)