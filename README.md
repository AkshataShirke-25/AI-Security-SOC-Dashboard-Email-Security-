# AI Email SOC

## Overview
This project simulates an AI-powered Security Operations Center (SOC) for monitoring email threats.

## Features
- Email log analysis
- Risk scoring system
- Anomaly detection (Isolation Forest)
- Real-time alerting (Telegram)
- REST API endpoints

## APIs
- /analyze → Full analysis
- /summary → Risk summary
- /high-risk → Critical threats

## Tech Stack
- Python
- Flask
- Pandas
- Scikit-learn

## How to Run
pip install -r requirements.txt
python src/app.py