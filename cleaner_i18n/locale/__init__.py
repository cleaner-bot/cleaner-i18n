import typing

from . import en_uk, en_us


class Locale(typing.NamedTuple):
    iso_code: str
    native_name: str
    english_name: str
    data: typing.Any


locales = [
    Locale("en-US", "English (US)", "English (US)", en_us),
    Locale("en-UK", "English (UK)", "English (UK)", en_uk),
]
localesd = {loc.iso_code: loc for loc in locales}
