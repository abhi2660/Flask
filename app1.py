
# from flask import Flask , render_template
# from datetime import datetime
# app = Flask(__name__)

# # to create a database

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# db=SQLAlchemy(app)


# class Todo(db.Model):
#     sno=db.Column(db.Integer,primary_key=True)
#     title=db.Column(db.String(200),nullable=False)
#     desc=db.Column(db.String(500),nullable=False)
#     date=db.Column(db.DateTime,default=datetime.utcnow)

#     def __repr__(self)->str:
#         return f"{self.sno}-{self.title}"

# @app.route('/')
# def hello_world():
#     return render_template('index.html')
#     # return 'Hello, World!'

# @app.route('/veer')
# def veera():
#     return 'veer here'


# # to run this app
# if __name__=="__main__":
#     app.run(debug=True)