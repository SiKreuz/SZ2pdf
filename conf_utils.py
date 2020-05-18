import configparser
from pathlib import Path

import appdirs

APP_NAME = 'SZ2pdf'

CONFIG_DIR = appdirs.user_config_dir(APP_NAME)
CONFIG_FILE_NAME = 'config'
CONFIG_FILE_PATH = CONFIG_DIR + '/' + CONFIG_FILE_NAME

STANDARD_DOWNLOAD_PATH = str(Path.home()) + '/SZ2pdf_Downloads'

SZ_SECTION = 'SZ'
SZ_LOGIN_USERNAME = 'username'
SZ_LOGIN_PASSWORD = 'password'
SZ_DOWNLOAD_DIR = 'download_dir'
SZ_EDITION = 'edition'

# create config directory if not already existing
if not Path(CONFIG_FILE_PATH).exists():
    Path(CONFIG_DIR).mkdir(parents=True, exist_ok=True)

# load existing config
config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH)

# add section if not existing
if not config.has_section(SZ_SECTION):
    config.add_section(SZ_SECTION)


def save_config():
    with open(CONFIG_FILE_PATH, 'w+') as config_file:
        config.write(config_file)


def setup_sz_login():
    config.set(SZ_SECTION, SZ_LOGIN_USERNAME, '')
    config.set(SZ_SECTION, SZ_LOGIN_PASSWORD, '')
    save_config()


def setup_download_dir():
    config.set(SZ_SECTION, SZ_DOWNLOAD_DIR, STANDARD_DOWNLOAD_PATH)
    save_config()


def setup_sz_section():
    config.set(SZ_SECTION, SZ_EDITION, 'Stadtausgabe')
    save_config()


def get_username():
    if not config.has_option(SZ_SECTION, SZ_LOGIN_USERNAME):
        setup_sz_login()
    return config.get(SZ_SECTION, SZ_LOGIN_USERNAME)


def get_password():
    if not config.has_option(SZ_SECTION, SZ_LOGIN_PASSWORD):
        setup_sz_login()
    return config.get(SZ_SECTION, SZ_LOGIN_PASSWORD)


def get_download_path():
    if not config.has_option(SZ_SECTION, SZ_DOWNLOAD_DIR):
        setup_download_dir()
    download_path = config.get(SZ_SECTION, SZ_DOWNLOAD_DIR)
    Path(download_path).mkdir(parents=True, exist_ok=True)
    return download_path


def get_edition():
    if not config.has_option(SZ_SECTION, SZ_EDITION):
        setup_sz_section()
    return config.get(SZ_SECTION, SZ_EDITION)
