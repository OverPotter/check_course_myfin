from DataBase.db_client import DB


class Comparison(DB):

    def __init__(self):
        super().__init__()
        self.__course_rate_has_increased = []
        self.__course_rate_has_decreased = []

        self._max_course_dict = {}
        self._min_course_dict = {}

    def _comparison_of_courses(self, current_bank: str, current_course: tuple):
        UPDATE = False
        db = DB()
        last_course = db._get_courses(current_bank)
        for i in range(6):
            if current_course[i] != last_course[i]:
                UPDATE = True

            if current_course[i] >= last_course[i]:
                self.__course_rate_has_increased.append([i, current_bank, current_course[i]])

            if current_course[i] <= last_course[i]:
                self.__course_rate_has_decreased.append([i, current_bank, current_course[i]])

        if UPDATE:
            db._update_courses(current_course, current_bank)

    def _search_max_courses(self):
        for info in self.__course_rate_has_increased:
            operation = info[0]
            bank = info[1]
            course = info[2]
            if operation in self._max_course_dict.keys():
                if self._max_course_dict[operation][1] < course:
                    self._max_course_dict[operation] = [bank, course]
            else:
                self._max_course_dict.update({operation: [bank, course]})

    """
        operation == 0  ->  buyUSD 
        operation == 1  ->  sellUSD
        operation == 2  ->  buyEUR
        operation == 3  ->  sellEUR
        operation == 4  ->  buyRUB
        operation == 5  ->  sellRUB
    """

    def _search_min_courses(self):
        for info in self.__course_rate_has_decreased:
            operation = info[0]
            bank = info[1]
            course = info[2]
            if operation in self._min_course_dict.keys():
                if self._min_course_dict[operation][1] > course:
                    self._min_course_dict[operation] = [bank, course]
            else:
                self._min_course_dict.update({operation: [bank, course]})
