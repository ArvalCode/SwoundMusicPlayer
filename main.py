from flask import Flask, render_template, request, redirect
import os
import random

# calculate audio file length

app = Flask(__name__)


@app.route('/')
def index():
    dir_list = os.listdir("static/music") 

    coverimgs = []
    for path in os.scandir(f'static/music/'):
        if not path.is_file():
            for i in os.scandir(f'static/music/{path.name}'):
                if i.is_file():
                    coverimgs.append(i.name)

    sdir_list = os.listdir("static/suggested") 

    scoverimgs = []
    for path in os.scandir(f'static/suggested/'):
        if not path.is_file():
            for i in os.scandir(f'static/suggested/{path.name}'):
                if i.is_file():
                    scoverimgs.append(i.name)

    return render_template('home.html', the_title='Music Player App', music = dir_list, coverimglist = coverimgs, sdir_list = sdir_list, scoverimgs = scoverimgs )

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

    return redirect(f'/folder?foldername={name}')
@app.route('/folder')
def folder():
    folderid = request.args.get("foldername")
    folder = os.listdir(f"static/music/{folderid}") 

    audiofiles = os.listdir(f"static/music/{folderid}/audio")

    for path in os.scandir(f'static/music/{folderid}'):
        if path.is_file():
            coverimage = path

    
    return render_template('yourlib.html', s="music", the_title='Your Library', audiofiles = sorted(audiofiles, key=lambda x: random.random()), name = folderid, coverimg = coverimage.name)

@app.route('/sfolder')
def sfolder():
    folderid = request.args.get("foldername")
    folder = os.listdir(f"static/suggested/{folderid}") 

    audiofiles = os.listdir(f"static/suggested/{folderid}/audio")

    for path in os.scandir(f'static/suggested/{folderid}'):
        if path.is_file():
            coverimage = path

    
    return render_template('yourlib.html',s="suggested", the_title='Your Library', audiofiles = sorted(audiofiles, key=lambda x: random.random()), name = folderid, coverimg = coverimage.name)


if __name__ == '__main__':
    app.run(debug=True)