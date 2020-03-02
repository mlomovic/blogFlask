from flask import render_template, url_for, redirect, flash
from blogflask import app
from blogflask.forms import RegistrationForm, LoginForm
from blogflask.models import User, Post



posts = [
    {
        'author' : 'petar petrovic',
        'title' : 'blog 1',
        'content' : 'Prvi post',
        'date_posted' : 'April 4, 2018'
    },
    {
        'author' : 'mika mikic',
        'title' : 'blog 2',
        'content' : 'Drugi post',
        'date_posted' : 'June 18, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html', posts=posts)


@app.route('/about')
def about():

    return render_template('about.html', title='about')


@app.route("/register", methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        #flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please try again', 'danger')
    
    return render_template('login.html', title="Register", form=form)


