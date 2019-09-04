from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField,SubmitField
from wtforms.validators import DataRequired

class Prediction(FlaskForm):
    bedrooms =IntegerField('Number of Bedrooms', validators=[DataRequired()])
    bathrooms=IntegerField('Number of Bathrooms', validators=[DataRequired()])
    sqft_living = DecimalField('Sqft_Living', validators=[DataRequired()])
    sqft_lot = DecimalField('Sqft lot', validators=[DataRequired()])
    floors = IntegerField('Floors', validators=[DataRequired()])
    sqft_above = DecimalField('Sqft above', validators=[DataRequired()])
    sqft_lot15 = DecimalField('Sqft_lot15', validators=[DataRequired()])
    yr_built = IntegerField('Year built', validators=[DataRequired()])
    condition = IntegerField('Condition', validators=[DataRequired()])
    zipcode = IntegerField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Submit')

