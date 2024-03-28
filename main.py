from flask import Flask, render_template, request, redirect
import os


app = Flask(__name__)

@app.route('/')
def index():
    dir_list = os.listdir("static/music") 
    return render_template('home.html', the_title='Music Player App', music = dir_list)

@app.route('/createfolder', methods=['POST'])
def createfolder():
    name = request.form['collection_name']
    cover_image = request.files['cover_image']
    audio_files = request.files.getlist('files[]')
    collection_folder = os.path.join('static/music', name) 
    os.makedirs(collection_folder, exist_ok=True) 

    cover_image_path = os.path.join(collection_folder, cover_image.filename) 
    cover_image.save(cover_image_path)

    audio_folder = os.path.join(collection_folder, 'audio') 
    os.makedirs(audio_folder, exist_ok=True)

    for audio_file in audio_files: 
        audio_file_path = os.path.join(audio_folder, audio_file.filename) 
        audio_file.save(audio_file_path)
    dir_list = os.listdir("static/music") 

    return redirect('/')

@app.route('/folder')
def folder():
    folderid = request.args.get("foldername")
    folder = os.listdir(f"static/music/{folderid}") 

    audiofiles = os.listdir(f"static/music/{folderid}/audio")

    for path in os.scandir(f'static/music/{folderid}'):
        if path.is_file():
            coverimage = path

    
    return render_template('yourlib.html', the_title='Your Library', audiofiles = audiofiles, name = folderid, coverimg = coverimage.name)


if __name__ == '__main__':
    app.run(debug=True)    
