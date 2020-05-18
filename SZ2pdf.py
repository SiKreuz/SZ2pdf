import re
from datetime import datetime

import click
import mechanize

import conf_utils
from output_utils import e_print

# URLs
LOGIN_URL = 'https://epaper.sueddeutsche.de/login'
E_PAPER_URL = 'https://epaper.sueddeutsche.de/'
DOWNLOAD_URL_PREFIX = 'https://epaper.sueddeutsche.de/download/'

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--edition', '-e', help='Specifies the edition to be downloaded.')
def cli(edition):
    sz_credentials = conf_utils.get_sz_credentials()
    if not edition:
        edition = conf_utils.get_edition()

    br = mechanize.Browser()

    # login
    print('Logging in...')
    br.open(LOGIN_URL)
    br.select_form(nr=0)
    br.form['login'] = sz_credentials[0]
    br.form['password'] = sz_credentials[1]
    br.submit()

    # look for current newspaper
    try:
        br.open(E_PAPER_URL + edition)
    except mechanize.HTTPError:
        e_print('Invalid edition. Please enter a valid edition.')
        exit(1)

    download_link = None
    try:
        download_link = br.find_link(url_regex=re.compile('/webreader/\d{6}'))
        print('Login successful.')
    except mechanize.LinkNotFoundError:
        e_print('Login failed. Please check your login credentials at ' + conf_utils.CONFIG_FILE_PATH)
        exit(1)

    download_url = re.sub('/webreader/', DOWNLOAD_URL_PREFIX, download_link.url)

    # download pdf
    print('Downloading "' + conf_utils.get_edition() + '" of the current newspaper from ' + download_url)
    file_path_regex = datetime.now().strftime(
        conf_utils.get_download_path() + '/%Y_%m_%d_SZ-' + edition + '.pdf')
    file_path = br.retrieve(download_url, file_path_regex)[0]

    br.close()

    print('Saved to ' + file_path + '.')


if __name__ == '__main__':
    cli()
