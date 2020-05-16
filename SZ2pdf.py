import configparser
import re
from datetime import datetime
from pathlib import Path

import appdirs
import click
import mechanize

# load config
CONFIG_DIR = appdirs.user_config_dir('SZ2pdf')
if not Path(CONFIG_DIR + '/config').exists():
    # create config file
    Path(CONFIG_DIR).mkdir(parents=True, exist_ok=True)
    config = configparser.RawConfigParser()
    config.set('DEFAULT', 'username', '')
    config.set('DEFAULT', 'password', '')
    config.set('DEFAULT', 'download_dir', str(Path.home()) + '/SZ2pdf_Downloads')
    if not Path(CONFIG_DIR + '/config').exists():
        with open(CONFIG_DIR + '/config', 'w+') as config_file:
            config.write(config_file)

# load existing config
config = configparser.ConfigParser()
config.read(CONFIG_DIR + '/config')

# URLs
LOGIN_URL = 'https://epaper.sueddeutsche.de/login'
E_PAPER_URL = 'https://epaper.sueddeutsche.de/Stadtausgabe'
DOWNLOAD_URL_PREFIX = 'https://epaper.sueddeutsche.de/download/'


def create_download_directory():
    Path(config.get('DEFAULT', 'download_dir')).mkdir(parents=True, exist_ok=True)


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--show-config-dir', '-cd', is_flag=True, help='Prints the path of the config directory.')
def cli(show_config_dir):
    # Show path of config dir
    if show_config_dir:
        print('Your config file is located in ' + CONFIG_DIR)
        exit(0)

    # login
    print('Logging in...')
    br = mechanize.Browser()
    br.open(LOGIN_URL)
    br.select_form(nr=0)
    br.form['login'] = config.get('DEFAULT', 'username')
    br.form['password'] = config.get('DEFAULT', 'password')
    br.submit()

    # look for current newspaper
    br.open(E_PAPER_URL)
    download_link = None
    try:
        download_link = br.find_link(url_regex=re.compile('/webreader/\d{6}'))
        print('Login successful.')
    except mechanize.LinkNotFoundError:
        print('Login failed.')
        exit(1)

    download_url = re.sub('/webreader/', DOWNLOAD_URL_PREFIX, download_link.url)

    # download pdf
    print('Downloading current newspaper from ' + download_url)
    create_download_directory()
    file_name = datetime.now().strftime(config.get('DEFAULT', 'download_dir') + '/%Y_%m_%d_SZ.pdf')
    file_path = br.retrieve(download_url, file_name)[0]

    print('Saved to ' + file_path + '.')


if __name__ == '__main__':
    cli()
