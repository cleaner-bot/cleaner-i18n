from .locale import localesd

FALLBACK = "en-US"


def translate(language: str, key: str, **kwargs):
    locale = localesd.get(language, None)
    if locale is None:
        language = FALLBACK
        locale = localesd[language]

    if key.startswith("_"):  # just a bit of security
        return key

    string = getattr(locale.data, key, None)
    if string is None:
        if language == FALLBACK:
            return key
        locale = localesd[FALLBACK]
        string = getattr(locale.data, key, None)
        if string is None:
            return key

    return string.format(**kwargs)
