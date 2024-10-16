from flask import Flask, render_template, request, redirect, url_for
from freeGPT import Client
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

# Home route to display the form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle image generation and display on the same page
@app.route('/generate', methods=['POST'])
def generate_image():
    try:
        prompt = request.form['prompt']
        # Call the image generation API
        resp = Client.create_generation("prodia", prompt)
        image = Image.open(BytesIO(resp))

        # Convert image to base64 so we can embed it in HTML
        img_io = BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

        return render_template('index.html', img_data=img_base64)

    except Exception as e:
        return render_template('index.html', error=f"Error generating image: {e}")

if __name__ == '__main__':
    app.run(debug=True)
