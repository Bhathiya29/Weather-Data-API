from flask import Flask, render_template
import pandas as pd

# Creating a website object from Flask class
app = Flask('Website')

stations = pd.read_csv('Data/stations.txt', skiprows=17)
stations = stations[['STAID', 'STANAME                                 ']]

# The root directory (home in this case). @ is for a line decorator and it connects
@app.route('/')
def home():
    return render_template('index.html', data=stations.to_html())


# The URL is dynamic for what the user enters
@app.route('/api/v1/<station>/<date>')
def about(station, date):
    print(station)

    # Taking the URL data and formatting it to the txt names using zfill
    filename = 'Data/TG_STAID' + str(station).zfill(6)+'.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    # setting the condition to retrieve data and formatting the temperature
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10

    # Returning the data according to the URL endpoint
    return {'Station': station,
            'Date': date,
            'Temperature': temperature}


@app.route('/api/v1/<station>')
def all_data(station):
    filename = 'Data/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict()
    return result


@app.route('/api/v1/yearly/<station>/<year>')
def year(station, year):
    filename = 'Data/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict()
    return result


# Running the app only when main.py is executed directly
if __name__ == "__main__":
    app.run(debug=True)
