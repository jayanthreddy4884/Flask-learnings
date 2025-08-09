from flask import Flask, request,render_template, redirect, url_for, session, flash, make_response
 
app = Flask(__name__, template_folder= 'template')
app.secret_key = "hello"

@app.route( "/", methods = ['GET' , 'POST'])
def index():
    if request.method == 'GET':
        return  render_template("index.html",  message = 'Index' )
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'jayanth' and password == '4884':
            return "Success"
        else:
            return 'Failure'


@app.route('/file_upload', methods = ['POST'])
def file_upload():
    file = request.files['File']
    
    if file.content_type == 'text/plain':
        return file.read().decode()
    else:
        return "dummy"
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        user  = request.form["nm"]
        session["user"] = user
        flash("you have been logged in")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Login  ")
            return redirect(url_for("user"))
        return render_template('login.html')

@app.route("/user")
def user():
    if 'user' in session:
        user = session["user"]
        
        return "<p>Welcome </p>"
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    flash("you have been logged out")
    session.pop("user",None)
    
    return redirect(url_for("login"))


@app.route("/set_data")
def set_data():
    session['name'] = "Jayanth"
    return render_template("index.html", message = 'Session data set')


@app.route("/get_data")
def get_data():
    if 'name' in session.keys():
        name = session['name']  
        return render_template("index.html", message = f'Name : {name}')
    else:
        return render_template("index.html", message = "No session found")


@app.route("/clear_session")
def clear_session():
    session.clear()
    return render_template("index.html", message = 'session cleared')


@app.route("/set_cookies")
def set_cookies():
    response = make_response(render_template("index.html", message = 'cookie set'))
    response.set_cookie('cookie_name', 'cookie_value')
    return response



@app.route("/get_cookies")
def get_cookies():
    cookie_value = request.cookies['cookie_name']
    return render_template("index.html", message = f'Cookie value : {cookie_value}')

@app.route("/remove_cookies")
def remove_cookies():
    response = make_response(render_template("index.html", message = " Cookie Removed"))
    response.set_cookie('cookie_name', expires=0)
    return response 

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port = '5555', debug=True)
