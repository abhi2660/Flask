from flask import Flask , render_template,request,redirect,url_for
app = Flask(__name__)



@app.route('/',methods=['GET'])
def hello_world():
    # return render_template('index.html')
    return 'Hello, World!'

@app.route('/veer',methods=['GET'])
def veera():
    return 'veer here'


# variable rule

# @app.route('/success')
@app.route('/success/<int:score>')
def veer(score):
    return 'veer here:'+str(score)

@app.route('/fail')
@app.route('/fail/<int:score>')
def fail(score):
    return 'veer here passed:'+str(score)


@app.route('/form',methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:

        # ["name"] same name as given to form input tag 
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average=(maths+science+history)/3
         
        res=""
        if average >= 50:
            res="veer"
        else:
            res="fail"
            
            
            # here in res we have to give the function of respective routing page 
        return redirect(url_for(res,score=average))

   
       
       
        #   share the average to form.html 
        # return render_template('form.html',score=average)



# to run this app
if __name__=="__main__":
    app.run(debug=True)