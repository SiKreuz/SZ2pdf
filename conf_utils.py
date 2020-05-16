import configparser
from pathlib import Path

import appdirs

from output_utils import e_print

APP_NAME = 'SZ2pdf'

CONFIG_DIR = appdirs.user_config_dir(APP_NAME)
CONFIG_FILE_NAME = 'config'
CONFIG_FILE_PATH = CONFIG_DIR + '/' + CONFIG_FILE_NAME

STANDARD_DOWNLOAD_PATH = str(Path.home()) + '/SZ2pdf_Downloads'

SZ_SECTION = 'SZ'
SZ_LOGIN_USERNAME = 'username'
SZ_LOGIN_PASSWORD = 'password'
SZ_DOWNLOAD_DIR = 'download_dir'

# create config directory if not already existing
if not Path(CONFIG_FILE_PATH).exists():
    Path(CONFIG_DIR).mkdir(parents=True, exist_ok=True)

# load existing config
config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH)


def save_config():
    with open(CONFIG_FILE_PATH, 'w+') as config_file:
        config.write(config_file)


def setup_sz_login():
    config.add_section(SZ_SECTION)
    config.set(SZ_SECTION, SZ_LOGIN_USERNAME, '')
    config.set(SZ_SECTION, SZ_LOGIN_PASSWORD, '')
    config.set(SZ_SECTION, SZ_DOWNLOAD_DIR, STANDARD_DOWNLOAD_PATH)
    save_config()


def get_sz_credentials():
    if config.has_option(SZ_SECTION, SZ_LOGIN_USERNAME) and config.has_option(SZ_SECTION, SZ_LOGIN_PASSWORD):
        return [config.get(SZ_SECTION, SZ_LOGIN_USERNAME), config.get(SZ_SECTION, SZ_LOGIN_PASSWORD)]
    else:
        setup_sz_login()
        e_print('No login credentials. Please enter your username and password for the "Sueddeutsche Zeitung" first '
                'in the config file: '
                + CONFIG_FILE_PATH)
        exit(1)


def get_download_path():
    if config.has_option(SZ_SECTION, SZ_DOWNLOAD_DIR):
        download_path = config.get(SZ_SECTION, SZ_DOWNLOAD_DIR)
        Path(download_path).mkdir(parents=True, exist_ok=True)
        return STANDARD_DOWNLOAD_PATH
    else:
        setup_sz_login()
        return get_download_path()
