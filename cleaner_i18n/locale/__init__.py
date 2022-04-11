import typing

from . import (
    da,
    de,
    en_gb,
    en_us,
    es_es,
    fr,
    hr,
    it,
    lt,
    hu,
    nl,
    no,
    pl,
    pt_br,
    ro,
    fi,
    sv_se,
    vi,
    tr,
    cs,
    el,
    bg,
    ru,
    uk,
    hi,
    th,
    zh_cn,
    ja,
    zh_tw,
    ko,
)


class Locale(typing.NamedTuple):
    iso_code: str
    english_name: str
    native_name: str
    data: typing.Any


locales = [
    Locale("da", "Danish", "Dansk", da),
    Locale("de", "German", "Deutsch", de),
    Locale("en-GB", "English, UK", "English, UK", en_gb),
    Locale("en-US", "English, US", "English, US", en_us),
    Locale("es-ES", "Spanish", "Español", es_es),
    Locale("fr", "French", "Français", fr),
    Locale("hr", "Croatian", "Hrvatski", hr),
    Locale("it", "Italian", "Italiano", it),
    Locale("lt", "Lithuanian", "Lietuviškai", lt),
    Locale("hu", "Hungarian", "Magyar", hu),
    Locale("nl", "Dutch", "Nederlands", nl),
    Locale("no", "Norwegian", "Norsk", no),
    Locale("pl", "Polish", "Polski", pl),
    Locale("pt-BR", "Portuguese, Brazilian", "Português do Brasil", pt_br),
    Locale("ro", "Romanian, Romania", "Română", ro),
    Locale("fi", "Finnish", "Suomi", fi),
    Locale("sv-SE", "Swedish", "Svenska", sv_se),
    Locale("vi", "Vietnamese", "Việt Tiếng", vi),
    Locale("tr", "Turkish", "Türkçe", tr),
    Locale("cs", "Czech", "Čeština", cs),
    Locale("el", "Greek", "Ελληνικά", el),
    Locale("bg", "Bulgarian", "български", bg),
    Locale("ru", "Russian", "Pусский", ru),
    Locale("uk", "Ukrainian", "Українська", uk),
    Locale("hi", "Hindi", "हिन्दी", hi),
    Locale("th", "Thai", "ไทย", th),
    Locale("zh-CN", "Chinese, China", "中文", zh_cn),
    Locale("ja", "Japanese", "日本語", ja),
    Locale("zh-TW", "Chinese, Taiwan", "繁體中文", zh_tw),
    Locale("ko", "Korean", "한국어", ko),
]
localesd = {loc.iso_code: loc for loc in locales}
