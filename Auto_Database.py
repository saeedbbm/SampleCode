
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def createTable(AutoConn,ReportConn):

    createAutoTableQuery = QSqlQuery(AutoConn)
    createAutoTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS AutoDbTable (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            picture INTEGER NOT NULL,
            video INTEGER NOT NULL,
            program VARCHAR(50) NOT NULL,
            position FLOAT NOT NULL,
            height FLOAT NOT NULL,
            angle FLOAT NOT NULL
        )
        """
    )
    # createTable1Query = QSqlQuery(QSqlDatabase.database('ReportConn_Name'))
    createTableQuery_Report = QSqlQuery(ReportConn)
    createTableQuery_Report.exec(
        """
        CREATE TABLE IF NOT EXISTS ReportDbTable (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            ID2 INTEGER NOT NULL,
            Alarm INTEGER NOT NULL,
            picture INTEGER NOT NULL,
            video INTEGER NOT NULL,
            program VARCHAR(50) NOT NULL,
            position FLOAT NOT NULL,
            height FLOAT NOT NULL,
            angle FLOAT NOT NULL,
            time VARCHAR(50) NOT NULL,
            o2 INTEGER NOT NULL,
            co2 INTEGER NOT NULL,
            ch4 INTEGER NOT NULL,
            humidity INTEGER NOT NULL,
            temperature INTEGER NOT NULL,
            battery INTEGER NOT NULL
        )
        """
    )

def createConnection(path):
    AutoConn = QSqlDatabase.addDatabase("QSQLITE",'AutoConnName')
    AutoConn.setDatabaseName(path+"/AutoDataBase.sqlite")
    if not AutoConn.open():
        QMessageBox.warning(
            None,
            "AutoDataBase",
            f"Database Error: {AutoConn.lastError().text()}",
        )
        return False

    ReportConn = QSqlDatabase.addDatabase("QSQLITE", 'ReportConnName')
    ReportConn.setDatabaseName(":memory:")
    if not ReportConn.open():
        QMessageBox.warning(
            None,
            "ReportDataBase",
            f"Database Error: {ReportConn.lastError().text()}",
        )
        return False

    createTable(AutoConn,ReportConn)
    return True