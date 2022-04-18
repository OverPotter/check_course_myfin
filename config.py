import os

URL = "https://myfin.by/currency/minsk"

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
TEMP_PATH = os.path.join(BASE_PATH, "TEMP")
DB_NAME = "DataBase\myfin.db"

BANKS_DICT = {'Абсолютбанк': 'Absolutbank', 'Альфа-Банк': 'Alfa-Bank', 'Банк БелВЭБ': 'BelVEB Bank',
              'Банк ВТБ (Беларусь)': 'VTB Bank (Belarus)', 'Банк Дабрабыт': 'Dabrabyt Bank',
              'Банк Решение': 'Bank Solution',
              'Белагропромбанк': 'Belagroprombank', 'Беларусбанк': 'Belarusbank', 'Белгазпромбанк': 'Belgazprombank',
              'Белинвестбанк': 'Belinvestbank', 'БНБ-Банк': 'BNB-Bank', 'БСБ Банк': 'PSB Bank', 'БТА Банк': 'BTA Bank',
              'МТБанк': 'MTBank', 'Паритетбанк': 'Paritetbank', 'Приорбанк': 'Priorbank', 'РРБ-Банк': 'RRB-Bank',
              'Сбер Банк': 'Sber Bank', 'СтатусБанк': 'StatusBank', 'Технобанк': 'Technobank', 'ТК Банк': 'TC Bank',
              'Франсабанк': 'Fransabank', 'Цептер Банк': 'Zepter Bank'}
