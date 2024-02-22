from flask import render_template, request
import pyrebase

def login_page():
    firebaseConfig = {
        "apiKey": "AIzaSyAy0cMkzM7bxGFQLiufO6KfrNsiS6aaaSc",
        "authDomain": "earthquake-e0bc5.firebaseapp.com",
        "projectId": "earthquake-e0bc5",
        "storageBucket": "earthquake-e0bc5.appspot.com",
        "messagingSenderId": "465375470663",
        "appId": "1:465375470663:web:9029d6b92c06f9a4e37d62",
        "measurementId": "G-SXN8KJJFFG",
        "databaseURL": ""
    }
    if request.method == 'POST':
        firebase = pyrebase.initialize_app(firebaseConfig)

        auth = firebase.auth()

        email = request.form.get("email")
        password = request.form.get("password")

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            return render_template("login.html", user=user)
        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("login.html")
