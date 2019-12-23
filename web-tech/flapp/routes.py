from flapp import app

@app.route('/config')
def show_config():
    return {'SECRET_KEY': str(app.config['SECRET_KEY']), 
    'CSRF_ENABLED': str(app.config['CSRF_ENABLED'])}

# @app.before_request
# def before_request():
#     g.user = current_user


@app.route('/')
@app.route('/index')
# @login_required
def index():
    user = {'nickname': 'Nick'}
    posts = [
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]

    return render_template('index.html',
        title = 'Home',
        user = user,
        posts = posts)

        
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/user/add/<username>')
def introduce_user(username):
    u = models.User(username=username, email=f'{username}@somemail.ru')
    db.session.add(u)
    db.session.commit()

    return f'<pre>{str(u)}</pre>'


@app.route('/users')
def show_users():
    users = models.User.query.all()
    users_str = ''
    for u in users:
        users_str += str(u.id) + ":" + str(u.username) + ":" + str(u.email)+ " "
    return users_str


@app.route('/posts')
def show_posts():
    posts = models.Post.query.all()
    posts_str = ''
    for p in posts:
        posts_str += str(p.id) + ":" + str(p.author.username) + " " 
    return posts_str


@app.route('/post/add/<user_id>')
def new_post(user_id):
    u = models.User.query.get(int(user_id))
    current_db_sessions = db.session.object_session(u)
    
    p = models.Post(body='some-text', author=u)

    current_db_sessions.add(p)
    current_db_sessions.commit()

    return f'<pre>{str(u)}</pre>'


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))