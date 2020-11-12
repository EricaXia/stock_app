from wtforms import Form, StringField

class SymSearchForm(Form):
    symbol = StringField('Symbol')

class DateSearchForm(Form):
    date = StringField('Date')