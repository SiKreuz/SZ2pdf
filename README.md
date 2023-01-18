# SZ2pdf
Dieses Tool soll dabei helfen, immer die neueste Ausgabe der [Süddeutschen Zeitung](https://www.sueddeutsche.de/) als PDF herunterzuladen.
Wenn man sich über die Website einloggen muss, sind es leider nervig viele Klicks, bis man zum eigentlichen Download kommt.
Das geht jetzt einfacher!

Zwingend erforderlich ist dafür natürlich ein Account und Abo bei der Süddeutschen Zeitung, sodass du den Zugriff auf das ePaper hast.

## Installation
Mit `pip` installieren:
```commandline
pip install git+https://github.com/SiKreuz/SZ2pdf
```

Zum Updaten der Software muss die Option `-U` verwendet werden. Für eine systemweite Installation sind root-Rechte nötig.

## Konfiguration
Alle wichtigen Parameter können entweder über die Kommandozeile übergeben werden, oder in der Konfigurationsdatei festgelegt werden.

### Kommandozeile
```text
Usage: SZ2pdf [OPTIONS]

Options:
  -u, --username TEXT      Username for login
  -p, --password TEXT      Password for login
  -e, --edition TEXT       Specifies the edition
  -d, --download-dir PATH  Download directory
  -h, --help               Show this message and exit.
```

### Konfigurationsdatei
Die Konfigurationsdatei liegt in dem für das Betriebssystem typischen Ordner. Unter Linux wäre das `~/.config/SZ2pdf/config`. Standardmäßig werden die folgenden Konfigurationen geschrieben:

```ini
[SZ]
username = 
password = 
edition = Stadtausgabe
download_dir = <home-dir>/SZ2pdf_Downloads
```

### Mögliche Editionen der SZ
Folgende Versionen der Zeitung können angegeben werden (bitte Großschreibung beachten):
- Starnberg
- Wolfratshausen
- Dachau
- Fürstenfeldbruck
- Erding
- Freising
- Ebersberg
- München LK Nord
- München LK Süd
- München Ost
- München West
- München Süd
- Stadtausgabe (Standard)
- Fernausgabe

## Forks für andere Zeitungen

Anscheinend nutzen andere Zeitungen das selbe Framework, weshalb hier Forks für andere Zeitungen aufgelistet sind.

-   Frankfurter Rundschau: [FR2PDF](https://github.com/xorbital/FR2pdf) von [@xorbital](https://github.com/xorbital)
