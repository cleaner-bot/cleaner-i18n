from cleaner_i18n.translate import translate


def test_translate_locale_fallback():
    assert translate(None, "helloworld") == "Hello World!"
    assert translate("xx-XX", "helloworld") == "Hello World!"


def test_leakage():
    assert translate("en-US", "__file__") == "__file__"


def test_translate_non_existent():
    assert translate("en-US", "does_not_exist") == "does_not_exist"


def test_translate_key_fallback():
    assert translate("en-UK", "helloworld") == "Hello World!"
    assert translate("en-UK", "does_not_exist") == "does_not_exist"
