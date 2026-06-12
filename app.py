from flask import Flask, render_template, request
import numpy as np
import joblib
import os


# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret'  # Simple development secret key

# Load models
MODEL_PATH = os.path.join('models', 'ridge.joblib')
SCALER_PATH = os.path.join('models', 'scaler.joblib')

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except Exception as e:
    model = None
    scaler = None
    load_error = str(e)

from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect

class DummyForm(FlaskForm):
    pass

csrf = CSRFProtect(app)

@app.route('/')
def index():
    form = DummyForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return render_template('home.html', 
                             fwi_value="Model Error",
                             error_message=f"Model not available: {load_error}")
    
    try:
        # Read and validate inputs
        validation_rules = {
            'Temperature': (-50, 60),
            'RH': (0, 100),
            'Ws': (0, 200),
            'Rain': (0, 1000),
            'FFMC': (0, 101),
            'DMC': (0, 500),
            'DC': (0, 1000),
            'ISI': (0, 100),
            'BUI': (0, 500)
        }

        # Default values for date and region
        input_values = [1, 1, 2024]  # Default date
        
        for feature in ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'DC', 'ISI', 'BUI']:
            value = request.form.get(feature)
            if not value or value.strip() == '':
                raise ValueError(f'Missing required input: {feature}')
            
            value = float(value)
            min_val, max_val = validation_rules[feature]
            
            if not (min_val <= value <= max_val):
                raise ValueError(
                    f'Invalid value for {feature}: {value}. '
                    f'Must be between {min_val} and {max_val}.'
                )
            
            input_values.append(value)
        
        input_values.append(0)  # Default region

        # Scale and predict
        input_array = np.array(input_values).reshape(1, -1)
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)[0]
        prediction = round(float(prediction), 2)

        # Calculate risk level
        risk_level = "low"
        if prediction > 32:
            risk_level = "extreme"
        elif prediction > 22:
            risk_level = "high"
        elif prediction > 12:
            risk_level = "moderate"

        return render_template('home.html', fwi_value=prediction, risk_level=risk_level)

    except ValueError as ve:
        return render_template('home.html', 
                             fwi_value="Input Error", 
                             error_message=str(ve))
    except Exception as e:
        return render_template('home.html', 
                             fwi_value="Server Error", 
                             error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)