import typing

from . import en_uk, en_us


class Locale(typing.NamedTuple):
    iso_code: str
    native_name: str
    english_name: str
    data: typing.Any


locales = [
    Locale("bg", "български", "Bulgarian", object()),
    Locale("es", "Español", "Spanish", object()),
    Locale("cs", "Čeština", "Czech", object()),
    Locale("da", "Dansk", "Danish", object()),
    Locale("de", "Deutsch", "German", object()),
    Locale("el", "Ελληνικά", "Greek", object()),
    Locale("en-US", "English (US)", "English (US)", en_us),
    Locale("en-UK", "English (UK)", "English (UK)", en_uk),
    Locale("fi", "Suomi", "Finnish", object()),
    Locale("fr", "Français", "French", object()),
    Locale("hi", "हिन्दी", "Hindi", object()),
    Locale("hr", "Hrvatski", "Croatian", object()),
    Locale("hu", "Magyar", "Hungarian", object()),
    Locale("it", "Italiano", "Italian", object()),
    Locale("ja", "日本語", "Japanese", object()),
    Locale("ko", "한국어", "Korean", object()),
    Locale("lt", "Lietuviškai", "Lithuanian", object()),
    Locale("nl", "Nederlands", "Dutch", object()),
    Locale("no", "Norsk", "Norwegian", object()),
    Locale("pl", "Polski", "Polish", object()),
    Locale("pt-BR", "Português do Brasil", "Portuguese, Brazilian", object()),
    Locale("ro", "Română", "Romanian", object()),
    Locale("ru", "Pусский", "Russian", object()),
    Locale("sv-SE", "Svenska", "Swedish", object()),
    Locale("th", "ไทย", "Thai", object()),
    Locale("tr", "Türkçe", "Turkish", object()),
    Locale("uk", "Українська", "Ukrainian", object()),
    Locale("vi", "Tiếng Việt", "Vietnamese", object()),
    Locale("zh-CN", "中文", "Chinese, China", object()),
    Locale("zh-TW", "繁體中文", "Chinese, Taiwan", object()),
]
localesd = {loc.iso_code: loc for loc in locales}
