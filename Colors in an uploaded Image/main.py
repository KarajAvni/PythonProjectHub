from flask import Flask, render_template, request
from PIL import Image
from collections import Counter
import io

app = Flask(__name__)


def get_most_common_colors(image_path, num_colors=5):
    image = Image.open(image_path)
    image = image.convert("RGB")
    colors = image.getdata()
    color_count = Counter(colors)
    most_common_colors = color_count.most_common(num_colors)
    return most_common_colors


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    img = Image.open(io.BytesIO(file.read()))
    img.save('uploaded_image.jpg')

    most_common_colors = get_most_common_colors('uploaded_image.jpg')

    return render_template('result.html', colors=most_common_colors)


if __name__ == '__main__':
    app.run(debug=True)
