from flask import (
    Blueprint,
    request,
    session,
    g,
    redirect,
    url_for,
    abort,
    render_template,
    flash
)
from werkzeug.contrib.cache import SimpleCache
from app import app
from model.model import (
    db,
    GamerTester
)

cache = SimpleCache()
# rv = cache.get(key)
# cache.set(key, rv, timeout=5*60)

user = Blueprint(
    'user',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/user'
)


@user.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('user.show_entries'))
    return render_template('login.html', error=error)


@user.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('user.show_entries'))


@user.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('user.show_entries'))


@user.route('/')
def show_entries():
    entries = GamerTester.query.all()
    return render_template('show_entries.html', entries=entries)
