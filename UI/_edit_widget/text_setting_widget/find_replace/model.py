from dataclasses import dataclass


@dataclass
class FindReplaceModel:
    search_text: str
    replace_text: str
    match_case: bool
    whole_word: bool
    wrap_search: bool
    regex: bool
    result_count: int