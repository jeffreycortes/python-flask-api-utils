from .app import app, jsonify
from src.app_data.reports.report_manager import ReportManager

@app.route("/api/reports/users")
def usersReport():
    report = ReportManager()
    return jsonify(report.getUsersReportData())
