from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

cafes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_cafe = request.form['new_cafe']
        cafes.append(new_cafe)
        return redirect(url_for('index'))
    else:
        return render_template('index.html', cafes=cafes)


if __name__ == '__main__':
    app.run(debug=True)