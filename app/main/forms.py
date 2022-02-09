from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, SelectField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    category = SelectField('Select Category', choices=[('Business','Business'),('Product','Product'),('Events','Events'),('Job','Job'),('Promotion','Promotion')],validators=[InputRequired()])
    pitch = TextAreaField('Enter Your Pitch', validators=[InputRequired()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[InputRequired()])
    submit = SubmitField('Leave a Comment')