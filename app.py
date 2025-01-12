import telebot
from telebot import types
from flask import Flask, render_template , request, session, redirect
import requests

app = Flask(__name__, template_folder='.site', static_folder='.site', static_url_path='/')
app.secret_key = 'xxx'

tokken = "7525871760:AAGj7NTUIxNTDq_JpBqQF3E7PvGnk8MtgT8"

bot = telebot.TeleBot(tokken)
#channel_id = '@hackerpdfbotlog'
link = 'https://t.me/hackerfilesxx'
user_id = "@hackerfilesxx"



def upload(doc, file_name):
   try : 
    bot.send_document(user_id , doc , timeout=100, caption=file_name, )
   except Exception as e :
       print("error filr ", e)
       
def get_file_path(file_id):
    url = f"https://api.telegram.org/bot{tokken}/getFile?file_id={file_id}"
    response = requests.get(url)
    data = response.json()
    return data['result']['file_path']


@app.route("/")
def hello():
    file = "not fund"
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def file():
    if request.method == 'POST':
       try : 
        file = request.files['file']
        file.filename
        msg = bot.send_document(user_id , file.read() ,caption=file.filename, timeout=100 ) 
        id = msg.document.file_id
        print(file.name)
        file_path = get_file_path(id)
        file_link = f"https://api.telegram.org/file/bot{tokken}/{file_path}?filename={file.filename}"
        return render_template("index.html", file=file_link)
       except Exception as e:
           print(e) 
           
    else:
        print("upload error ")
        
@app.route('/download/<files>')
def files(files):
     return files

    
    




if __name__ == '__main__':
      app.run(port=8080, debug=True)