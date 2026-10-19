from flask import Flask, jsonify
from datetime import datetime, timezone
import os

application = Flask(__name__)

@application.get("/")
def home():
    return """
    <h1>WebApp CI/CD Demo</h1>
    <p>Your application is running on AWS Elastic Beanstalk.</p>
    <p>Starter source code for the AWS assignment.</p>
    """

@application.get("/health")
def health():
    return jsonify(
        status="healthy",
        service="webapp-cicd-demo",
        time=datetime.now(timezone.utc).isoformat()
    )

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
