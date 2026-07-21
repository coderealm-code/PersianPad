from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget, QApplication, QPushButton, QFrame, QComboBox, QLineEdit, QSpinBox
from PySide6.QtCore import Qt, Signal
import sys
from app.sizes.metrics import EditWidgetMetrics
from app.models.font_format import FontFormatModel
from app.models.search_part_model import SearchReplaceModel
from app.services.search_part_controller import SearchReplaceController
from app.widgets.text_place_widget import TextEdit


class EditWidget(QWidget):

    request_bold = Signal()
    request_italic = Signal()
    request_underLine = Signal()
    request_font_family = Signal(str)
    request_font_size = Signal(int)
    request_align_right = Signal()
    request_align_left = Signal()
    request_align_center = Signal()
    request_align_justify = Signal()
    request_copy = Signal()
    request_cut = Signal()
    request_paste = Signal()
    request_undo = Signal()
    request_redo = Signal()
    request_select_all = Signal()
    

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setLayoutDirection(Qt.RightToLeft)
        self.setFixedSize(EditWidgetMetrics.width, EditWidgetMetrics.height)

        self.font_size_cbx = QComboBox()
        self.font_choice_cbx = QComboBox()
        self.font_size_cbx.setEditable(True)
        self.font_choice_cbx.setEditable(True)

        self.editor = TextEdit(self)
        self.search_model = SearchReplaceModel()
        self.search_controller = SearchReplaceController(model=self.search_model, editor=self.editor)

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 0, 10)
        layout.setSpacing(10)
        
        # add the layout parts you made to the main layout
        layout.addLayout(self.title_label())
        layout.addLayout(self.first_part_layout())
        layout.addStretch()
        layout.addLayout(self.frameVline())
        layout.addStretch()
        layout.addLayout(self.second_part_layout())
        layout.addStretch()
        layout.addLayout(self.frameVline())
        layout.addStretch()
        layout.addLayout(self.third_part_layout())
        layout.addStretch()
        layout.addLayout(self.frameVline())
        layout.addStretch()
        layout.addLayout(self.fourth_part())
        self.setLayout(layout)


    def title_label(self) -> QHBoxLayout:
        #------------- لایوت لیبل سبز ویرایش -------------------
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(0, 0, 0, 0)

        title_lbl = QLabel("ویرایش")
        title_lbl.setAlignment(Qt.AlignCenter)
        title_lbl.setFixedSize(EditWidgetMetrics.lbl_width, EditWidgetMetrics.lbl_height)
        title_lbl.setStyleSheet("""font-size: 16px; font-weight: bold; background-color: #437753; color: white;""")

        title_layout.addWidget(title_lbl)
        return title_layout

    def first_part_layout(self) -> QVBoxLayout:
        #------------- مجموعه لایوت دکمه ها ---------------------
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(10)

        # ---- عنوان اصلی وسط ----
        upper_layout = QHBoxLayout()
        upper_layout.setContentsMargins(0, 0, 0, 0)
        upper_layout.setAlignment(Qt.AlignCenter)

        part_title_lbl = QLabel("عملیات پایه")
        upper_layout.addWidget(part_title_lbl)

        # ---- دکمه‌ها ----
        lower_layout = QHBoxLayout()
        lower_layout.setContentsMargins(0, 0, 0, 0)
        lower_layout.setSpacing(10)

        undo_btn = QPushButton("عقب گرد")
        redo_btn = QPushButton("جلو گرد")
        select_all_btn = QPushButton("انتخاب همه")
        cut_btn = QPushButton("برش")
        copy_btn = QPushButton("کپی")
        paste_btn = QPushButton("چسباندن")

        btn_list = [undo_btn, redo_btn, select_all_btn, cut_btn, copy_btn, paste_btn]
        func_list = [self.request_undo.emit, self.request_redo.emit, self.request_select_all.emit
                     , self.request_cut.emit, self.request_copy.emit, self.request_paste.emit]


        for btn, func in zip(btn_list, func_list):
            btn.setFixedSize(EditWidgetMetrics.f_btn_width, EditWidgetMetrics.f_btn_height)
            lower_layout.addWidget(btn)
            btn.clicked.connect(func)
        lower_layout.addStretch()

        
        content_layout.addLayout(upper_layout)
        content_layout.addLayout(lower_layout)
        
        return content_layout


    def second_part_layout(self) -> QVBoxLayout:
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(10)
        
        part_title_lay = QHBoxLayout()
        part_title_lay.setAlignment(Qt.AlignCenter)

        upper_lay = QHBoxLayout()
        upper_lay.setContentsMargins(0, 0, 0, 0)
        upper_lay.setSpacing(10)

        lower_lay = QHBoxLayout()
        lower_lay.setContentsMargins(0, 0, 0, 0)
        lower_lay.setSpacing(10)

        
        part_title_lbl = QLabel("فونت")
        part_title_lay.addWidget(part_title_lbl)
        # Add your widgets for the second part here
        # For example:
        # some_widget = SomeWidget()
        # layout.addWidget(some_widget)

        font_model = FontFormatModel()
        for font in font_model.get_fonts():
            self.font_choice_cbx.addItem(font.title, font.family)

        sizes = [4, 6, 8, 9, 10, 11, 12, 14, 16, 18, 20, 24, 28, 32, 36, 48, 72]
        
        for size in sizes:
            self.font_size_cbx.addItem(str(size))
        self.font_size_cbx.setCurrentText("12")
        
        self.font_choice_cbx.currentIndexChanged.connect(self._emit_font_family)
        self.font_size_cbx.currentIndexChanged.connect(self._emit_font_size)

        self.font_choice_cbx.setFixedSize(EditWidgetMetrics.s_cbx_width*60/100, EditWidgetMetrics.s_cbx_height)
        self.font_size_cbx.setFixedSize(EditWidgetMetrics.s_cbx_width*40/100, EditWidgetMetrics.s_cbx_height)

        upper_lay.addWidget(self.font_choice_cbx)
        upper_lay.addWidget(self.font_size_cbx)

        bold_btn = QPushButton("Bold")
        italic_btn = QPushButton("Italic")
        underLine_btn = QPushButton("UnderLine")

        list_btn = [bold_btn, italic_btn, underLine_btn]
        func_list = [self.request_bold.emit, self.request_italic.emit, self.request_underLine.emit]

        for btn, func in zip(list_btn, func_list):
            btn.setFixedSize(EditWidgetMetrics.s_btn_width, EditWidgetMetrics.s_btn_height)
            lower_lay.addWidget(btn)
            btn.clicked.connect(func)

        main_layout.addLayout(part_title_lay)
        main_layout.addStretch()
        main_layout.addLayout(upper_lay)
        main_layout.addStretch()
        main_layout.addLayout(lower_lay)
        return main_layout

    def third_part_layout(self) -> QVBoxLayout:
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(10)

        lower_lay = QHBoxLayout()
        lower_lay.setContentsMargins(0, 0, 0, 0)
        lower_lay.setSpacing(10)

        right_lay = QVBoxLayout()
        right_lay.setContentsMargins(0, 0, 0, 0)
        right_lay.setSpacing(10)

        left_lay = QVBoxLayout()
        left_lay.setContentsMargins(0, 0, 0, 0)
        left_lay.setSpacing(10)

        part_title_lay = QHBoxLayout()
        part_title_lay.setAlignment(Qt.AlignCenter)
        part_title_lbl = QLabel("جستجو و جایگزینی")
        part_title_lbl.setAlignment(Qt.AlignCenter)
        part_title_lay.addWidget(part_title_lbl)

        # Add your widgets for the second part here
        # For example:
        # some_widget = SomeWidget()
        # layout.addWidget(some_widget)

        find_button = QPushButton("پیدا کردن")
        replace_btn = QPushButton("جایگزین کردن")
        replace_all_btn = QPushButton("جایگزین همه")

        btn_list  = [find_button, replace_btn, replace_all_btn]
        func_list = [self.search_controller.search, self.search_controller.replace, self.search_controller.replace_all]

        for btn, func in zip(btn_list, func_list):
            btn.setFixedSize(EditWidgetMetrics.t_btn_width, EditWidgetMetrics.t_btn_height)
            btn.clicked.connect(func)
            right_lay.addWidget(btn)

        search_entry = QLineEdit()
        search_entry.setPlaceholderText("متن مورد نظر...")
        search_entry.setFixedSize(EditWidgetMetrics.t_entry_width, EditWidgetMetrics.t_entry_height)
        search_entry.textChanged.connect(self.search_model.set_search_text)

        replace_entry= QLineEdit()
        replace_entry.setPlaceholderText("جایگزین با")
        replace_entry.setFixedSize(EditWidgetMetrics.t_entry_width, EditWidgetMetrics.t_entry_height)
        replace_entry.textChanged.connect(self.search_model.set_replace_text)

        left_lay.addWidget(search_entry)
        left_lay.addWidget(replace_entry)

        lower_lay.addLayout(right_lay)
        lower_lay.addLayout(left_lay)

        main_layout.addLayout(part_title_lay)
        main_layout.addStretch()
        main_layout.addLayout(lower_lay)

        return main_layout
    
    def fourth_part(self) -> QVBoxLayout:
        main_lay = QVBoxLayout()

        part_title_lay = QHBoxLayout()
        part_title_lay.setAlignment(Qt.AlignCenter)

        part_title_lbl = QLabel("تراز متن")
        part_title_lay.addWidget(part_title_lbl)

        btn_lay = QHBoxLayout()

        justify_btn = QPushButton("منظم")
        rightWing_btn = QPushButton("راستچین")
        leftWing_btn = QPushButton("چپ چین")
        middleWing_btn = QPushButton("وسط چین")

        btn_list = [justify_btn, rightWing_btn, leftWing_btn, middleWing_btn]
        func_list = [self.request_align_justify.emit, self.request_align_right.emit, self.request_align_left.emit, self.request_align_center.emit]

        for btn, func in zip(btn_list, func_list):
            btn.setFixedSize(EditWidgetMetrics.fo_btn_width, EditWidgetMetrics.fo_btn_height)
            btn.clicked.connect(func)
            btn_lay.addWidget(btn)
        btn_lay.addStretch()

        main_lay.addLayout(part_title_lay)
        main_lay.addStretch()
        main_lay.addLayout(btn_lay)
        return main_lay


    def frameVline(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        # Add your widgets for the second part here
        # For example:
        # some_widget = SomeWidget()
        # layout.addWidget(some_widget)

        line_frame = QFrame()
        line_frame.setFrameShape(QFrame.VLine)
        line_frame.setFrameShadow(QFrame.Sunken)
        line_frame.setStyleSheet("background-color: lightgray;")
        line_frame.setFixedHeight(EditWidgetMetrics.height - 16)  # Adjust the height as needed
        layout.addWidget(line_frame)

        return layout

    def _emit_font_family(self):
        family = self.font_choice_cbx.currentData()
        if family:
            self.request_font_family.emit(family)
        return
    
    def _emit_font_size(self):
        text = self.font_size_cbx.currentText().strip()
        try:
            size = int(text)

        except  ValueError:
            return
        self.request_font_size.emit(size)
        

    def undo(self):
        print("Undo button clicked")

    def redo(self):
        print("Redo button clicked")

    def select_all(self):
        print("Select All button clicked")

    def cut(self):
        print("Cut button clicked")

    def copy(self):
        print("Copy button clicked")

    def paste(self):
        print("Paste button clicked")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditWidget()
    window.show()
    sys.exit(app.exec())
