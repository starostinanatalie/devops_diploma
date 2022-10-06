from frontend import app_frontend

@app_frontend.route('/')
@app_frontend.route('/index')
def index():
    return "Hello, world!"