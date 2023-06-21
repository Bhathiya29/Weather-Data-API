from flask import Flask, render_template

# Creating a website object from Flask class
app = Flask('Website')


# The root directory (home in this case). @ is for a line decorator and it connects
@app.route('/')
def home():
    return render_template('index.html')


# The URL is dynamic for what the user enters
@app.route('/api/v1/<station>/<date>')
def about(station, date):
    # df = pandas.read_csv('')
    temperature = 24
    return {'Station': station,
            'Date': date,
            'Temperature': temperature}


# Running the app only when main.py is executed directly
if __name__ == "__main__":
    app.run(debug=True)
