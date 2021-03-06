from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, IntegerField, RadioField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from flask_babel import _, lazy_gettext as _l
from app.models import User, Sensor


class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different email address.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

class AddSensorForm(FlaskForm):
    sensorID = IntegerField(_l('Input a SensorID'), validators=[DataRequired()])
    sensorName = StringField(_l('Input a Sensor Name'),
                           validators=[DataRequired()])
    sensorAlarmValue = IntegerField(_l('Input a Sensor Value'))
    sensorClass = SelectField(
        'Sensor Type',
        choices=[('','Select which type of sensor this is'),('1','Smoke'),('2','Monoxide'),('3','Static'),('4','Heat')]
    )
    submit = SubmitField(_l('Add Sensor'))

    def validate_sensorID(self, sensorID):
        sensor = Sensor.query.filter_by(sensorID=sensorID.data).first()
        if sensor is not None:
            raise ValidationError(_('Please choose a different sensorID'))

    def validate_sensor(self, sensorName):
        sensor = Sensor.query.filter_by(sensorName=sensorName.data).first()
        if sensor is not None:
            raise ValidationError(_('Please choose a different sensorName'))


class EditSensorForm(FlaskForm):
    sensorID = IntegerField(_l('Input a Sensor ID'), validators=[DataRequired()])
    sensorName = StringField(_l('Input a Sensor Name'),
                           validators=[DataRequired()])
    sensorAlarmValue = IntegerField(_l('Input a Sensor Value'))
    sensorClass = SelectField(
        'Sensor Type',
        choices=[('','Select which type of sensor this is'),('1','Smoke'),('2','Monoxide'),('3','Static'),('4','Heat')]
    )
    submit = SubmitField(_l('Update Sensor'))

   