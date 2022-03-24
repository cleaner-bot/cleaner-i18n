import typing

from . import de, en_uk, en_us


class Locale(typing.NamedTuple):
    iso_code: str
    english_name: str
    native_name: str
    data: typing.Any


locales = [
    Locale("da", "Danish", "Dansk", object()),
    Locale("de", "German", "Deutsch", de),
    Locale("en-GB", "English, UK", "English, UK", en_uk),
    Locale("en-US", "English, US", "English, US", en_us),
    Locale("es-ES", "Spanish", "Español", object()),
    Locale("fr", "French", "Français", object()),
    Locale("hr", "Croatian", "Hrvatski", object()),
    Locale("it", "Italian", "Italiano", object()),
    Locale("lt", "Lithuanian", "Lietuviškai", object()),
    Locale("hu", "Hungarian", "Magyar", object()),
    Locale("nl", "Dutch", "Nederlands", object()),
    Locale("no", "Norwegian", "Norsk", object()),
    Locale("pl", "Polish", "Polski", object()),
    Locale("pt-BR", "Portuguese, Brazilian", "Português do Brasil", object()),
    Locale("ro", "Romanian, Romania", "Română", object()),
    Locale("fi", "Finnish", "Suomi", object()),
    Locale("sv-SE", "Swedish", "Svenska", object()),
    Locale("vi", "Vietnamese", "Việt Tiếng", object()),
    Locale("tr", "Turkish", "Türkçe", object()),
    Locale("cs", "Czech", "Čeština", object()),
    Locale("el", "Greek", "Ελληνικά", object()),
    Locale("bg", "Bulgarian", "български", object()),
    Locale("ru", "Russian", "Pусский", object()),
    Locale("uk", "Ukrainian", "Українська", object()),
    Locale("hi", "Hindi", "हिन्दी", object()),
    Locale("th", "Thai", "ไทย", object()),
    Locale("zh-CN", "Chinese, China", "中文", object()),
    Locale("ja", "Japanese", "日本語", object()),
    Locale("zh-TW", "Chinese, Taiwan", "繁體中文", object()),
    Locale("ko", "Korean", "한국어", object()),
]
localesd = {loc.iso_code: loc for loc in locales}
