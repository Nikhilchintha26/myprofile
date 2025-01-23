from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download-resume', methods=['GET'])
def download_resume():
    resume_path = r"resume.pdf"
    return send_file(resume_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
