# EconoVision-Server

![Flask](https://img.shields.io/badge/Flask-20232A?style=flat&logo=flask&logoColor=white&labelColor=black&color=grey)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/WoongyuChoi/EconoVision-Server/blob/main/LICENSE)
![Platform](https://img.shields.io/badge/platform-server-green)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/WoongyuChoi/EconoVision-Server)

<figure align="center">
    <img src="https://github.com/user-attachments/assets/de75d318-85f0-4225-976b-7ee8da3fa5b3" width="50%"/>
</figure>

## Overview

**EconoVision-Server** is a backend service built using Flask. The project fetches financial and economic data from external APIs and integrates machine learning models to predict future trends, such as foreign exchange rates. By analyzing historical patterns and generating predictions, EconoVision aims to provide actionable insights.

## Features

- **Flask Framework**: Lightweight and powerful Python web framework.
- **External API Integration**: Fetches financial data (e.g., foreign exchange rates) from trusted sources.
- **Dynamic Machine Learning Models**: Predicts future trends based on historical data.
- **Modular Architecture**: Clean and maintainable codebase.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/WoongyuChoi/EconoVision-Server.git
    ```

2. Navigate into the project directory:
    ```bash
    cd EconoVision-Server
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the server locally:
    ```bash
    python run.py
    ```

6. Deploy to Vercel:
    ```bash
    vercel --prod
    ```

## Usage

The server fetches historical data and uses machine learning algorithms to predict future trends. For example, given a sequence of foreign exchange rates (1300, 1350, 1400), the system might predict future values like 1410 by identifying unique patterns in the data.

#### **Health Check**
```bash
GET / HTTP/1.1
```

Response:
```json
{
  "status": "UP"
}
```

#### **Exchange Rate Prediction**
```bash
GET /api/exchange-rate?start_date=20240101&end_date=20241231
```

Response:
```json
{
  "predicted_rate": 1410.50,
  "confidence": 95.0
}
```

## License

This project is licensed under the MIT License.
