# SOAR Lite - AI-Powered Security Automation

> 🛡️ Lightweight SOAR (Security Orchestration, Automation, and Response) tool for SMBs using FastAPI + Slack alerts + AI-based threat scoring.

![SOAR Lite Banner](https://via.placeholder.com/1000x200?text=SOAR+Lite+-+AI-Powered+Security+Automation)

---

## 🚀 Features

* ✅ Real-time log ingestion API
* 🤖 AI-based threat scoring engine
* 📲 Slack alert integration for high-risk threats
* 🌱 Built with FastAPI, Python, and dotenv

---

## 📦 Project Structure

```bash
ai-access-manager/
├── api/
│   ├── main.py          # FastAPI app entry
│   └── routes/
│       └── logs.py      # Log analysis route
├── engine/
│   ├── analyzer.py      # Threat scoring + Slack alert
│   ├── scorer.py        # Legacy scoring logic
│   └── responder.py     # Async Slack alert sender (optional)
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
└── README.md            # You are here 🚀
```

---

## 🧪 How to Run Locally

```bash
# 1. Clone the repo
$ git clone https://github.com/<your-username>/ai-access-manager.git
$ cd ai-access-manager

# 2. Create virtual environment
$ python -m venv venv
$ venv\Scripts\activate    # On Windows

# 3. Install dependencies
(venv) $ pip install -r requirements.txt

# 4. Add your .env file
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/xxx/yyy/zzz

# 5. Run the server
(venv) $ uvicorn api.main:app --reload
```

---

## 🧪 API Usage (Swagger UI)

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### POST /logs/analyze

#### Request Body

```json
{
  "log": "unauthorized access to admin panel"
}
```

##Response

```json
{
  "log": "unauthorized access to admin panel",
  "score": 0.9,
  "action": "🚨 Alert sent to Slack"
}
```

##Example Slack Alert:

[![Slack Alert](./slack_alert.png)](https://github.com/suri10/soar-lite/blob/main/SOAR-LITE%20Alerts.PNG)

--

##📄 License

##MIT License
