from app import app


app.config['SECRET_KEY'] = 'a-hardcoded-string'

if __name__ == '__main__':
    app.run()

