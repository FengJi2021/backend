import sys
sys.path.insert(0, 'root/.local')
from operator import methodcaller
from flask import Flask , render_template, url_for , request , redirect
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from datetime import datetime

from werkzeug.utils import redirect

app = Flask(__name__)

#db config
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200),nullable = False)
    data_created = db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self) -> str:
        return 'Test %r' % self.id


@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        print(request.form['content'])
        new_task = todo(content = task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
        except:
            pass
        #return redirect('/')
        return 'test response returned'
    else:
        return render_template('index.html')










if __name__ == '__main__':
    host = '0.0.0.0'
    port = 4999
    app.run(debug = True,host=host,port=port)