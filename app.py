from flask import Flask, render_template
from dotenv import load_dotenv
import os
import shutil
from shuffle_list import shuffle_list

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def main():
    shuff_img_list = shuffle_list(img_list)
    return render_template("index.html.j2", img_list=shuff_img_list)

if __name__ == '__main__':
    
    # load images
    load_dotenv()
    IMG_PATH = os.getenv('IMG_PATH')
    os.mkdir('./static/images')
    for img in os.listdir(IMG_PATH):
        shutil.copy2(IMG_PATH + '/' + img, './static/images')
    img_list = os.listdir("./static/images")

    app.run(host='0.0.0.0', port=12345)
    
    print("server is finished")
    shutil.rmtree('./static/images')


