from dataclasses import dataclass


@dataclass
class FindReplaceModel:
    search_text: str = ""     # متن جستجو
    replace_text: str = ""    # متن جایگزینی
    match_case: bool = False  # حساسیت به حروف کوچک و بزرگ انگلیسی
    whole_word: bool = False  # فقط کلمه کامل یا همون چیزی که توی جستجو است رو پیدا کن حتی اکه بقیه هم اون رو داشته باشه
    wrap_search: bool = False  # وقتی به آخر متن رسید از اول شروع کن
    regex: bool = False       #
    result_count: int = 0     # تعداد جستجور ها رو بشمار
    current_result: int = 0   # نتیجه فعلی