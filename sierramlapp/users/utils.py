import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from sierramlapp import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    #file_name, file_ext = os.path.splitext(form_picture.filename)
    # '_' we are throwing variable file_name because we dont need it, we just need the extension of the uploaded image
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + file_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_filename


def send_reset_email(user):
    token = user.get_password_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f''' To reset your password, visit the following link
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then ignore this email..!
'''
    mail.send(msg)
