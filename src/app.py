from flask import Flask, jsonify
from risk_model import process_logs
from alert import send_alert

app = Flask(__name__)

# ✅ HOME API
@app.route('/')
def home():

    return "AI Email SOC Backend Running 🚀"


# ✅ FULL ANALYSIS
@app.route('/analyze')
def analyze():

    data = process_logs()

    # Filter high risk logs
    high_risk = data[data['risk_level'] == "HIGH"]

    # Send alerts
    if not high_risk.empty:

        for _, row in high_risk.iterrows():

            message = f"""
🚨 HIGH RISK EMAIL DETECTED

Sender: {row['sender']}
Receiver: {row['receiver']}
Risk Score: {row['risk_score']}
Risk Level: {row['risk_level']}
IP Address: {row['ip']}
"""

            send_alert(message)

    return jsonify(data.to_dict(orient='records'))


# ✅ SUMMARY API
@app.route('/summary')
def summary():

    data = process_logs()

    return jsonify({

        "total_emails": len(data),

        "high_risk":
        len(data[data['risk_level'] == "HIGH"]),

        "medium_risk":
        len(data[data['risk_level'] == "MEDIUM"]),

        "low_risk":
        len(data[data['risk_level'] == "LOW"])

    })


# ✅ HIGH RISK ONLY
@app.route('/high-risk')
def high_risk():

    data = process_logs()

    high = data[data['risk_level'] == "HIGH"]

    return jsonify(high.to_dict(orient='records'))


if __name__ == '__main__':

    app.run(debug=True)
