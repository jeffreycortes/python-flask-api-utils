from src.app_data.file_manager.json.json_manager import JsonManager
from src.app_data.persistance.sqlite import Sqlite

class ReportManager:
    def getUsersReportData(self):
        pathFile = 'mocks/reports/users.json'
        return JsonManager().readJson(pathFile)
