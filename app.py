from flask import Flask, render_template
from forecast import simple_forecast
from analytics import get_dashboard_stats, get_ticket_trend
from datetime import datetime, timedelta

app = Flask(__name__)



@app.route("/")
def dashboard():

    stats = get_dashboard_stats()

    dates, counts = get_ticket_trend()
    predictions = simple_forecast(counts)
    today = datetime.today()

    future_dates = [
        (today + timedelta(days=i+1)).strftime("%d %b")
        for i in range(5)
    ]

    return render_template(
        "dashboard.html",
        stats=stats,
        dates=dates,
        counts=counts,
        predictions=predictions,
        future_dates=future_dates
    )

if __name__ == "__main__":
    app.run(debug=True)