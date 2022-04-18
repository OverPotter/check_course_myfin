import os.path
import sqlite3

from config import DB_NAME


class DB:

    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(os.getcwd(), DB_NAME))
        self.cursor = self.conn.cursor()

    def _get_courses(self, bank_name: str) -> tuple:
        result = self.cursor.execute(
            "SELECT `buyUSD`, `saleUSD`, `buyEUR`, `saleEUR`, `buyRUB`, `saleRUB`"
            "FROM `MoneyCourse`"
            "WHERE `Bank` = (?)",
            (bank_name,))
        return result.fetchall()[0]

    def _update_courses(self, course: tuple, bank_name: str) -> None:
        self.cursor.execute(
            "UPDATE `MoneyCourse`"
            "SET `buyUSD` = (?), `saleUSD` = (?), `buyEUR` = (?), `saleEUR` = (?), `buyRUB` = (?), `saleRUB` = (?)"
            "WHERE `Bank` = (?)",
            (*course, bank_name,))
        return self.conn.commit()
