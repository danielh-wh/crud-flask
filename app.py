from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
books = []
editoriales = ['Crossbooks', 'GeoPlaneta', 'Zenith']

# Página de inicio, muestra la lista de libros
@app.route('/')
def index():
    context = {
        'books': books
    }
    return render_template('index.html', **context)


# Ruta para agregar un nuevo libro
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        author = request.form['author']
        release_date = request.form['release-date']
        editorial = request.form['editorial']
        new_book = { 'id': len(books) + 1, 'title': title, 'description': description, 'author': author, 'release_date': release_date, 'editorial': editorial }
        books.append(new_book)
        return redirect(url_for('index'))
    context = {
        'editoriales': editoriales
    }
    return render_template('add.html', **context)


# Ruta para editar un libro existente
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    book = next((book for book in books if book['id'] == id), None)
    if request.method == 'POST':
        book['title'] = request.form['title']
        book['description'] = request.form['description']
        book['author'] = request.form['author']
        book['release_date'] = request.form['release_date']
        book['editorial'] = request.form['editorial']
        return redirect(url_for('index'))
    context = {
        'book': book,
        'editoriales': editoriales
    }
    return render_template('edit.html', **context)


# Ruta para eliminar un libro
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        books.remove(book)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
