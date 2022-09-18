from PyPDF2 import PdfFileMerger, PdfFileReader
import os

class PdfManager:
    def __init__(self):
        self.__sourcePath = 'src/app_data/file_manager/pdf/'
        self.__destinationPath = 'src/app_infrastructure/persistence/pdf/'
        self.__current_path = os.path.realpath(__file__)

    def merge(self):
        name_final = 'PARTE_MERGE.pdf'
        merger = PdfFileMerger()
        files = os.listdir(self.__sourcePath)
        merger.append(self.__sourcePath + 'mocks/PARTE_I.pdf')
        merger.append(self.__sourcePath + 'mocks/PARTE_II.pdf')
        merger.write(self.__destinationPath + name_final)
        return name_final
