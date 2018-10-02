from flask import Flask, redirect, request, render_template
import os
autoescape= True

app = Flask(__name__)
app.config['DEBUG'] = True 




@app.route("/")
def user_signup():

    return render_template('index.html')


@app.route("/", methods=['POST'])
def valid_user():

    user= request.form['username']
    passcode= request.form['password']
    recode= request.form['re_password']
    mail= request.form['email']

    if not user:
        return render_template('index.html', username_error="Please enter a valid username", email= mail)
    
    if ' ' in  user:
        return render_template('index.html', username_error="No spaces in username please", email= mail)

    if len(user) < 3 or len(user) > 20:
        return render_template('index.html', username_error="Username must be between 3 and 20 characters", username= user, email= mail)

    if not passcode:
        return render_template('index.html', password_error="Please enter password", username= user, email= mail)

    if len(passcode) < 3 or len(passcode) > 20:
        return render_template('index.html', password_error="Password must be between 3 and 20 characters", username= user, email= mail)


    if not recode:
        return render_template('index.html', re_password_error="Please re-enter password", username= user, email= mail)
    
    if ' ' in passcode or ' ' in recode:
        return render_template('index.html', password_error="Passwords have no spaces please", username= user, email= mail)
        

    if recode != passcode:
        return render_template('index.html', re_password_error="Passwords do not match", username= user, email= mail)

    if len(recode) < 3 or len(recode) > 20:
        return render_template('index.html', re_password_error="Passwords must be between 3 and 20 characters", username= user, email= mail)

    
    
    if len(mail) >= 1:
        if ' ' in mail:
            return render_template('index.html', email_error="Not a valid email address", username= user, email= mail)

        if len(mail) < 3 or len(mail) > 20:
            return render_template('index.html', email_error="Email address must be between 3 and 20 characters", username= user, email= mail)

        if '.' not in mail or '@' not in mail:
            return render_template('index.html', email_error="Not a valid email address", username= user, email= mail)

        else:

            return redirect('/validated?user={}'.format(user))

    else:

        return redirect('/validated?user={}'.format(user))




@app.route('/validated')
def validated():
    user= request.args.get('user')
    return render_template('welcome.html', name=user)




#, username_error= "Not a valid username", password_error= "Not a valid password", re_password_error="Password does not match", email_error="Not a valid email address"




app.run()