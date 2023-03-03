from wtforms import Form, StringField, PasswordField, validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password1 = PasswordField('Password', [
        validators.Length(min=4, max=25)
    ])

