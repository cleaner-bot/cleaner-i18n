from setuptools import setup, find_namespace_packages  # type: ignore

setup(
    name="cleaner_i18n",
    version="0.1.4",
    url="https://github.com/cleaner-bot/cleaner-i18n",
    author="Leo Developer",
    author_email="git@leodev.xyz",
    description="i18n of the cleaner",
    packages=find_namespace_packages(include=["cleaner_i18n*"]),
    package_data={"cleaner_i18n": ["py.typed"]},
)
