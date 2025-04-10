from flask import Flask, render_template, request, session, redirect  # Added redirect here
import pickle

app = Flask(__name__)
app.secret_key = 'your-secret-key-123'  # Change this to a random secret key

# Load model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tv.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'result' not in session:
        session['result'] = None
    
    if request.method == 'POST':
        input_text = request.form['text_input']
        # Vectorize and predict
        vectorized_text = vectorizer.transform([input_text])
        prediction = model.predict(vectorized_text)
        
        session['result'] = {
            'text': input_text,
            'is_plagiarized': bool(prediction[0]),
            'message': "⚠️ Plagiarism Detected!" if prediction[0] else "✅ Original Content"
        }
        return redirect('/')  # Redirect to avoid form resubmission
    
    return render_template('index.html', result=session.get('result'))

@app.route('/clear', methods=['POST'])
def clear_results():
    session.pop('result', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)