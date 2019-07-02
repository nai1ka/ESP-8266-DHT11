from flask import Flask
from flask import request
from flask import render_template
import datetime


app = Flask(__name__)
temperature_values=[]
humidity_values=[]
line_labels=[]
i=0
@app.route('/')
def temperature():
    global i
    Temperature = request.args.get('temperature', default = 0)
    Humidity = request.args.get('humidity', default = 0)
    if(Temperature!=0):
        temperature_values.append(Temperature)
        
    if(Humidity!=0):
        now = datetime.datetime.now()
        humidity_values.append(Humidity)
        line_labels.append(str(now.hour)+":"+str(now.minute)+":"+str(now.second))
        i+=1
        
    return render_template('line_chart.html', max=50, labels=line_labels, temp_values=temperature_values,hum_values=humidity_values)


	


if __name__ == "__main__":
    app.run(host='0.0.0.0')