from dataclasses import dataclass


@dataclass(frozen=True)
class Color:
    """Color for the file"""
    class LightColor:
        @dataclass
        class MainWindowColors:
            pass

        @dataclass
        class NavigationBarColors:
            BACKGROUND_COLOR: str = "#F8FAFC"
            BORDER: str = "transparent"

            BACKGROUND_COLOR_BTN: str = BACKGROUND_COLOR
            TEXT_COLOR_PRIMARY: str = "#000000"
            TEXT_COLOR_SECONDARY: str = "#FFFFFF"
            SELECTED_BTN: str = "#DBEAFE"
            HOVER: str = "#F3F4F6"

            # SETTING BUTTON
            SETTING_BACKGROUND: str = "transparent"
            SETTING_BORDER: str = "transparent"
            SETTING_HOVER: str = "#F3F4F6"
            SETTING_PRESSED: str = "#E5E7E8"

        @dataclass
        class ListWidgetColors:
            background_color: str = "#FFFFFF"
            border: str = "#7975E3"
            hover: str = "#d6d6ff"
            pressed: str = "#EBEBFF"

            text_color: str = "#000000"



    class DarkColor:
        @dataclass
        class MainWindowColors:
            pass

        @dataclass
        class NavigationBarColors:
            BACKGROUND_COLOR: str = "#F8FAFC"
            BORDER: str = "transparent"

            BACKGROUND_COLOR_BTN: str = BACKGROUND_COLOR
            TEXT_COLOR_PRIMARY: str = "#000000"
            TEXT_COLOR_SECONDARY: str = "#FFFFFF"
            SELECTED_BTN: str = "#DBEAFE"
            HOVER: str = "#F3F4F6"

            # SETTING BUTTON
            SETTING_BACKGROUND: str = "transparent"
            SETTING_BORDER: str = "transparent"
            SETTING_HOVER: str = "#F3F4F6"
            SETTING_PRESSED: str = "#E5E7E8"

        @dataclass
        class ListWidgetColors:
            background_color: str = "#000000"
            border: str = "transparent"
            hover: str = "#F3F4F6"
            pressed: str = "#E5E7E8"




