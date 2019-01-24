from flask import Flask , request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form =  """
 <!doctype html>
 <html>
    
       <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    
    <body>
        <form method="Post">
          
          <label>Rotate by:
          <input name= "rot" value = "0" type="text" />
          </label>
          <label>
          <textarea  name="text">{0}</textarea>
          </label>
          <input type="submit" value="Submit "/>
        </form>
    </body>
 </html>
"""            
 
  
@app.route("/")
def index():
    return form.format('')
@app.route("/" , methods=['POST'])
def encrypt():
    
    rots = int(request.form['rot'])
    test = request.form['text']
    
    return form.format(rotate_string(test, rots))


app.run()