from pathlib import Path


class PathHandler:
    ROOT_DIR = Path(__file__).resolve().parent.parent
    RESOURCES_DIR = ROOT_DIR / "resources"

    ICON_DIR = RESOURCES_DIR / "icons"
    FONT_DIR = RESOURCES_DIR / "fonts"
    IMAGES_DIR = RESOURCES_DIR / "imageS"
    STYLES_DIR = RESOURCES_DIR / "styles"

    @classmethod
    def icon(cls, name: str) -> Path:
        return cls.ICON_DIR / name

    @classmethod
    def font(cls, name: str) -> Path:
        return cls.FONT_DIR / name

    @classmethod
    def image(cls, name: str) -> Path:
        return cls.IMAGES_DIR / name

    @classmethod
    def style(cls, name: str) -> Path:
        return cls.STYLES_DIR / name

    @classmethod
    def optimized_path(cls, path: str) -> Path:
        """it will make the path optimized"""
        if not path:
            pass
        path_object = Path(path)
        optimized_path = path_object.resolve()
        return optimized_path