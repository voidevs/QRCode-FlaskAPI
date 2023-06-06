from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import qrcode, io


app = Flask(__name__)
CORS(app)
# application = app

# http://127.0.0.1/api/qrcode?text=Hello%20World!


@app.route('/api/qrcode', methods=['GET','POST'])
def qrcodee():
    if request.method == "POST":
        qrcode_text = request.json.get('text')
        if qrcode_text:
            img = qrcode.make(qrcode_text)
        else:
            data = {
                'result': False
            }
            return jsonify(data)
    else:
        qrcode_text = request.args.get('text')
        if qrcode_text:
            img = qrcode.make(qrcode_text)
        else:
            data = {
                'result': False
            }
            return jsonify(data)

    img_bytes = io.BytesIO()
    img.save(img_bytes)
    img_bytes = img_bytes.getvalue()

    return Response(img_bytes, mimetype='image/jpeg')





app.run(host="0.0.0.0", port=80, debug=False)