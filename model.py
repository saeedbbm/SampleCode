
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase

class DbModel:
    def __init__(self):
        self.modelAuto = self.createModelAuto()
        self.modelReport = self.createModelReport()

    def createModelAuto(self):
        tableModel = QSqlTableModel(None,QSqlDatabase.database('AutoConnName'))
        tableModel.setTable("AutoDbTable")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("id","Picture", "Video", "Program","Position","Height","Angle")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def createModelReport(self):
        tableModel = QSqlTableModel(None,QSqlDatabase.database('ReportConnName'))
        tableModel.setTable("ReportDbTable")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("id","ID","Alarm","Picture", "Video", "Program","Position","Height","Angle","Time",
                   "O2","Co2", "CH4", "Humidity", "Temperature","Battery")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def addData(self, data):
        rows = self.modelAuto.rowCount()
        self.modelAuto.insertRows(rows, 1)
        for column_index, field in enumerate(data):
            self.modelAuto.setData(self.modelAuto.index(rows, column_index + 1), field)
        self.modelAuto.submitAll()
        self.modelAuto.select()
        self.modelAuto.sort(4, Qt.AscendingOrder)

    def addDataReport(self, data):
        rows = self.modelReport.rowCount()
        self.modelReport.insertRows(rows, 1)
        for column_index, field in enumerate(data):
            self.modelReport.setData(self.modelReport.index(rows, column_index + 1), field)
        self.modelReport.submitAll()
        self.modelReport.select()
        self.modelReport.sort(5, Qt.AscendingOrder)

    def deleteData(self, row):
        self.modelAuto.removeRow(row)
        self.modelAuto.submitAll()
        self.modelAuto.select()