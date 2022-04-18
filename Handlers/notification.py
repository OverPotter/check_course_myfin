import win10toast
import emoji


class Notification:

    def __init__(self):
        self.__title_high = None
        self.__massage_high = None
        self.__title_low = None
        self.__massage_low = None
        # self.__title_just = None
        # self.__massage_just = None

    def __construct_text(self, best_buy: dict, best_sell: dict):
        if best_buy:
            self.__title_high = "Exchange rates have increased. " + emoji.emojize(":face_screaming_in_fear:")
            self.__massage_high = f"buy USD in {best_buy[0][0]}: {best_buy[0][1]}\n" \
                                  f"buy EUR in {best_buy[2][0]}: {best_buy[2][1]}\n" \
                                  f"buy RUB in {best_buy[4][0]}: {best_buy[4][1]}\n"
        # else:
        #     self.__title_just = "The buy course has not changed"
        #     self.__massage_just = "Try later. " + emoji.emojize(":face_with_rolling_eyes:")

        if best_sell:
            self.__title_low = "Exchange rates have decreased. " + emoji.emojize(":face_with_monocle:")
            self.__massage_low = f"sell USD in {best_sell[1][0]}: {best_sell[1][1]}\n" \
                                 f"sell EUR in {best_sell[3][0]}: {best_sell[3][1]}\n" \
                                 f"sell RUB in {best_sell[5][0]}: {best_sell[5][1]}\n"
        # else:
        #     self.__title_just = "The sell course has not changed"
        #     self.__massage_just = "Try later. " + emoji.emojize(":face_with_rolling_eyes:")

    @staticmethod
    def __call_notification(title: str, msg: str):
        notification = win10toast.ToastNotifier()
        notification.show_toast(title=title, msg=msg, duration=10)

    @staticmethod
    def _call_error_server_connection_notification(error: str):
        notification = win10toast.ToastNotifier()
        notification.show_toast(title="The server is lying." + emoji.emojize(":face_with_head-bandage:"),
                                msg="Error type: " + error, duration=5)

    @staticmethod
    def _call_response_error(response: str):
        notification = win10toast.ToastNotifier()
        notification.show_toast(title="Response not ok." + emoji.emojize(":face_with_medical_mask:"),
                                msg="Response is: " + response, duration=5)

    def run_notification(self, best_buy: dict, best_sell: dict):
        self.__construct_text(best_buy, best_sell)
        if self.__title_high:
            self.__call_notification(self.__title_high, self.__massage_high)
        if self.__title_low:
            self.__call_notification(self.__title_low, self.__massage_low)
        # if self.__title_just:
        #     self.__call_notification(self.__title_just, self.__massage_just)
