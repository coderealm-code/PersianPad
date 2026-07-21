


class SearchReplaceModel:
    def __init__(self):
        self.__search_text = ""
        self.__replace_text = ""


    @property
    def get_search_text(self) -> str:
        """ متن سرچ رو میگیره تا بده به کنترلر"""
        return self.__search_text
    
    @property
    def get_replace_text(self) -> str:
        """متن تبدیل رو میگیره ال بده به کنترلر"""
        return self.__replace_text
    

    
    def set_search_text(self, text: str) -> None:
        """ text متن سرچ را عوض میکند با پارمتر"""
        if not isinstance(text, str):
            raise TypeError("search text must be string!")
        
        self.__search_text = text.strip()
        return None
    

    def set_replace_text(self, text: str) -> None:
        """ text متن تبدیل را عوض میکند با پارمتر"""
        if not isinstance(text, str):
            raise TypeError("replace text must be string!")
        
        self.__replace_text = text.strip()
        return None