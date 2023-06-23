from flask import Flask, request, jsonify

app = Flask(__name__)

data = [
    {'id': 0, 'input': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
     'output': 'Lorem ipsum dolor sit amet, deserunt mollit anim id est laborum.'},
     {'id': 1, 'input': 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
      'output': 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium fugiat quo voluptas nulla pariatur?'},
      {'id': 2, 'input': 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.',
       'output': 'At vero eos et accusamus et iusto aut perferendis doloribus asperiores repellat.'}
]

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/conversions', methods=['GET', 'POST'])
def conversions():
    if request.method == 'GET':
        if len(data) > 0:
            return jsonify(data), 200
        return {}, 404
    
    if request.method == 'POST':
        input = request.form['input']
        output = input[:20]
        id = data[-1]['id'] + 1

        new_instance = {
            'id': id,
            'input': input,
            'output': output
        }

        data.append(new_instance)
        return jsonify(data), 201
    
@app.route('/conversions/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def conversionByID(id):
    if request.method == 'GET':
        for entry in data:
            if entry['id'] == int(id):
                return jsonify(entry), 200
        return 'Not Found', 404

empty = []

@app.route('/test')
def test():
    return jsonify(empty)

if __name__ == '__main__':
    app.run(debug=True)
