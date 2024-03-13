class KeyboardLanguage:

    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "RU":
            self.__language = "EN"
        else:
            self.__language = "RU"

