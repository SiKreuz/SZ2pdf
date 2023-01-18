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
@click.option('--username', '-u', default=conf_utils.get_username(), help='Username for login')
@click.option('--password', '-p', default=conf_utils.get_password(), help='Password for login')
@click.option('--edition', '-e', default=conf_utils.get_edition(), help='Specifies the edition')
@click.option('--download-dir', '-d', default=conf_utils.get_download_path(),
              type=click.Path(exists=True, resolve_path=True), help='Download directory')
def cli(edition, username, password, download_dir):
    if username == '' or password == '':
        e_print('Please enter your credentials.')
        exit(1)

    br = mechanize.Browser()
    br.set_handle_robots(False)

    # login
    print('Logging in...')
    br.open(LOGIN_URL)
    br.select_form(nr=0)
    br.form['login'] = username
    br.form['password'] = password
    br.submit()

    # login validation
    if 'E-Mail-Adresse oder Passwort sind nicht korrekt.' in br.response().read().decode('utf-8'):
        e_print('Login failed. Please check your login credentials.')
        exit(1)
    else:
        print('Login successful.')

    # open selected edition
    try:
        br.open(E_PAPER_URL + edition)
    except mechanize.HTTPError:
        e_print('Invalid edition. Please enter a valid edition.')
        exit(1)

    # crawling for download_url
    download_link = br.find_link(url_regex=re.compile('/webreader/\d{6}'))
    download_url = re.sub('/webreader/', DOWNLOAD_URL_PREFIX, download_link.url)

    # download pdf
    print('Downloading "' + edition + '" of the current newspaper from ' + download_url)
    file_path_regex = datetime.now().strftime(
        click.format_filename(download_dir) + '/%Y_%m_%d_SZ-' + edition + '.pdf')
    file_path = br.retrieve(download_url, file_path_regex)[0]

    br.close()

    print('Saved to ' + file_path + '.')


if __name__ == '__main__':
    cli()
