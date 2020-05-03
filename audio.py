from flask import Flask, render_template, request
app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/')
def upload_file():
   return render_template('index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['audio_data']
      f.save(f.filename + '.wav')
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)