from PersianPad.core.path_handler import PathHandler


class QssLoader:
    @classmethod
    def load_qss(cls, file_name: str) -> str:
        if not file_name.endswith(".qss"):
            raise Exception("Not a 'qss' file")
        path = PathHandler.style(file_name)
        try:
            with open(path, "r") as f:
                qss = f.read()
        except FileNotFoundError:
            raise Exception("Not a 'qss' file")
        return qss
