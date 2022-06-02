import typing

from .locale import localesd

FALLBACK = "en-US"
__all__ = ["translate", "Message", "FALLBACK", "localesd"]


def translate(language: str, key: str, **kwargs) -> str:
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


class Message(typing.NamedTuple):
    translate_key: str
    variables: dict[str, typing.Any] | None = None

    def translate(self, locale: str) -> str:
        if self.variables is None:
            return translate(locale, self.translate_key)
        return translate(locale, self.translate_key, **self.variables)
