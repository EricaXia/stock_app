from wtforms import Form, StringField, validators, DateField

class SymSearchForm(Form):
    symbol = StringField('Symbol')

class DateSearchForm(Form):
    date = DateField('Date')