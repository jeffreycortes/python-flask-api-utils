from flask import jsonify, request
from .app import app, jsonify
from src.app_data.media.youtube_dl_manager import YoutubeDLManager

@app.route("/api/media/video/youtube-dl/download", methods=['GET'])
def downloadYoutubeDLVideo():
    url = request.args.get('url')
    media = YoutubeDLManager()
    return jsonify(media.downloadBestAudio(url))

def print_shape():
  fullPrintRowIndex = [0 , 3 ,6]
  for row in range(0, 7):
    print_row(row in fullPrintRowIndex)

def print_row(full_print):
  indexPrint = (0, 5, 10)
  out = ''
  ch = '*'
  for col in range(0, 11):
    if full_print:
      out += ch
    else:
      out += ch if (col in indexPrint) else ' '
  print(out)

@app.route("/api/media/video/youtube-dl/version", methods=['GET'])
def version():
    media = YoutubeDLManager()
    print(vars(media.version()))
    return jsonify(vars(media.version))
