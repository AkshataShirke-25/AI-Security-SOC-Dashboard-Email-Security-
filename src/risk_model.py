import pandas as pd
from sklearn.ensemble import IsolationForest

def process_logs(file_path):
    data = pd.read_csv(file_path)

    # Convert time
    data['time'] = pd.to_datetime(data['time'])
    data['hour'] = data['time'].dt.hour

    # 🔥 UPDATED RISK FUNCTION
    def calculate_risk(row):
        score = 0

        # Failed login
        score += row['failed_login'] * 10

        # Attachments risk
        score += row['attachments'] * 15

        # Suspicious sender
        if "unknown" in row['sender'] or "spam" in row['sender']:
            score += 30

        # Domain check (extra security logic)
        if not row['sender'].endswith("@gmail.com"):
            score += 10

        # Night activity
        if row['hour'] < 6 or row['hour'] > 22:
            score += 20

        return min(score, 100)

    # Apply risk scoring
    data['risk_score'] = data.apply(calculate_risk, axis=1)

    # AI anomaly detection
    model = IsolationForest(contamination=0.3)
    data['anomaly'] = model.fit_predict(data[['failed_login', 'attachments']])
    data['anomaly'] = data['anomaly'].map({1: "Normal", -1: "Suspicious"})

    # Risk level classification
    def risk_level(score):
        if score > 70:
            return "HIGH"
        elif score > 40:
            return "MEDIUM"
        return "LOW"

    data['risk_level'] = data['risk_score'].apply(risk_level)

    return data