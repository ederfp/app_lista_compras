from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de compras em memória (para simplificar, em um projeto real usaria um banco de dados)
shopping_list = []
item_id_counter = 0

@app.route('/')
def index():
    return render_template('index.html', shopping_list=shopping_list)

@app.route('/add', methods=['POST'])
def add_item():
    global item_id_counter
    item_name = request.form.get('item_name')
    if item_name:
        shopping_list.append({'id': item_id_counter, 'name': item_name})
        item_id_counter += 1
    return redirect(url_for('index'))

@app.route('/edit/<int:item_id>', methods=['POST'])
def edit_item(item_id):
    new_name = request.form.get('new_name')
    for item in shopping_list:
        if item['id'] == item_id:
            item['name'] = new_name
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    global shopping_list
    shopping_list = [item for item in shopping_list if item['id'] != item_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
