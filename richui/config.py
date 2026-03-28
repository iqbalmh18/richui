from dataclasses import dataclass
from typing import Tuple

@dataclass
class Config:
    cursor: str = '➜'
    bracket: str = '('
    padding: Tuple[int, int] = (0, 0)
    newline: bool = False
    checkmark: str = '✔'
    key_style: str = 'white'
    value_style: str = 'yellow'
    text_style: str = 'white'
    text_width: int = 50
    text_ljust: int = 20
    title_style: str = 'bold italic green'
    guide_style: str = '#666666'
    title_justify: str = 'left'
    cursor_style: str = 'green'
    prompt_style: str = 'white'
    option_style: str = 'white'
    footer_style: str = 'italic #666666'
    bracket_style: str = 'white'
    selected_style: str = 'green'
    selection_style: str = 'yellow'
    checkmark_style: str = 'green'
    completion_style: str = 'green on #666666'
    completion_second_style: str = 'white on #666666'
    completion_select_style: str = 'bold reverse'