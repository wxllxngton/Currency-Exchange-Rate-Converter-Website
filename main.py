from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from requests import URLRequired
from wtforms import StringField, SubmitField, URLField
# The validators parameter accepts a List of validator Objects. DataRequired makes the two fields required fields, so the user must type something, otherwise an error will be generated.
from wtforms.validators import DataRequired
from converter import Converter

class ConverterForm(FlaskForm):
    source = StringField(label='Source currency three-digit code (ISO 4217), e.g. USD', validators=[DataRequired()])
    destination = StringField(label='Destination currency three-digit code (ISO 4217), e.g. EUR', validators=[DataRequired()])
    submit = SubmitField(label='Convert')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a random string'
Bootstrap(app)

@app.route('/', methods=['GET','POST'])
def home():
    form = ConverterForm()
    if form.validate_on_submit():
        exchange = Converter(source=form.source.data, destination=form.destination.data)
        result = exchange.convert()
        return render_template('conversion.html', result=result, source=form.source.data, destination=form.destination.data)
    return render_template('index.html', form=form)


@app.route('/conversion')
def conversion():
    return render_template('conversion.html')


if __name__ == '__main__':
    app.run(debug=True)
