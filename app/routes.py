from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from flask_babel import _, get_locale
from guess_language import guess_language
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm, \
    ResetPasswordRequestForm, ResetPasswordForm, AddSensorForm, EditSensorForm
from app.models import User, Post, Sensor
from app.email import send_password_reset_email, send_sensor_trigger_email
from app.translate import translate
from flask_table import table


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())


@app.route('/', methods=['GET', 'POST'])
@app.route('/monitor')
def monitor():
    sensors = Sensor.query.all()
    for s in sensors:
        if s.sensorAlarmValue > 0:
            s.sensorAlarmValue = "Alarm"
        else:
            s.sensorAlarmValue = "Ready"
    return render_template('monitor.html', title=_('Monitor'), sensors = sensors)



@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        language = guess_language(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, author=current_user,
                    language=language)
        db.session.add(post)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title=_('Home'), form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_('Invalid username or password'))
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title=_('Sign In'), form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_('Congratulations, you are now a registered user!'))
        return redirect(url_for('login'))
    return render_template('register.html', title=_('Register'), form=form)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash(
            _('Check your email for the instructions to reset your password'))
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title=_('Reset Password'), form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash(_('Your password has been reset.'))
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=_('Edit Profile'),
                           form=form)

@app.route('/configuration', methods=['GET', 'POST'])
@login_required
def configuration():
    sensors = Sensor.query.all()
    return render_template('mainConfig.html', title=_('Sensor Configuration'), sensors = sensors)
  
@app.route('/edit_Sensor/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_Sensor(id):

    sensor = Sensor.query.filter_by(sensorID = id).first()
    form = EditSensorForm()
    
    
    #PrePopulate Edit form fields
    form.sensorID.data = sensor.sensorID
    form.sensorName.data = sensor.sensorName
    form.sensorAlarmValue.data = sensor.sensorAlarmValue
    form.sensorClass.process_data(sensor.sensorClass)

    if form.validate_on_submit(): 
        #Update sensor
        sensor = Sensor.query.filter_by(sensorID = id).first()
        sensor.sensorID = request.form['sensorID']
        sensor.sensorName = request.form['sensorName']
        sensor.sensorAlarmValue = request.form['sensorAlarmValue']
        sensor.sensorClass = request.form['sensorClass']
        db.session.commit()
        user = User.query.filter_by(username=current_user.username).first()
        if sensor.sensorAlarmValue > 0:
            send_sensor_trigger_email(user, sensor)
        flash(_('Sensor has been updated successfully!'))
        return redirect(url_for('configuration'))
    return render_template('edit_sensor.html', form=form)

@app.route('/delete_sensor/<int:id>', methods=['POST'])
@login_required
def delete_sensor(id):
    #Deleting Sensor
    sensor = Sensor.query.filter_by(sensorID = id).first()
    db.session.delete(sensor)
    db.session.commit()
    flash('Sensor has been deleted successfully!', 'success')
    return redirect(url_for('configuration'))


@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('index'))
    if user == current_user:
        flash(_('You cannot follow yourself!'))
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash(_('You are following %(username)s!', username=username))
    return redirect(url_for('user', username=username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('index'))
    if user == current_user:
        flash(_('You cannot unfollow yourself!'))
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash(_('You are not following %(username)s.', username=username))
    return redirect(url_for('user', username=username))

@app.route('/addSensor', methods = ['GET', 'POST'])
@login_required
def addSensor():
    form = AddSensorForm()
    if form.validate_on_submit():
        sensor = Sensor(sensorID=form.sensorID.data, sensorName=form.sensorName.data,
        sensorAlarmValue=form.sensorAlarmValue.data, sensorClass=form.sensorClass.data)
        db.session.add(sensor)
        db.session.commit()
        user = User.query.filter_by(username=current_user.username).first()
        if sensor.sensorAlarmValue > 0:
            send_sensor_trigger_email(user, sensor)
        flash(_('Your sensor has been added!'))
        return redirect(url_for('monitor'))
    return render_template('addSensor.html', title=_('Add Sensor'), form=form)


@app.route('/translate', methods=['POST'])
@login_required
def translate_text():
    return jsonify({'text': translate(request.form['text'],
                                      request.form['source_language'],
                                      request.form['dest_language'])})



