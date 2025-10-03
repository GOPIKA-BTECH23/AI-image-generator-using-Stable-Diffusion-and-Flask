from flask import Flask, request, render_template
import requests
import base64

app = Flask(__name__)

def send_prompt_to_colab(prompt):
    url = "your-ngrok-url-here/generate_image"
    data = {"prompt": prompt}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()['image']
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    image_data = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        image_data = send_prompt_to_colab(prompt)
    return render_template('index.html', image_data=image_data)

if __name__ == '__main__':
    app.run()
