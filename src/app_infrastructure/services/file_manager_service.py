from .app import app, jsonify
from src.app_data.file_manager.pdf.pdf_manager import PdfManager

@app.route("/api/files/pdf/merge")
def pdfMerge():
    return jsonify(PdfManager().merge())
