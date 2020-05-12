# SZ2pdf
Dieses Tool soll dabei helfen, immer die neueste Ausgabe der [Süddeutschen Zeitung](https://www.sueddeutsche.de/) als PDF herunterzuladen. Wenn man sich über die Website einloggen muss, sind es leider nervig viele Klicks, bis man zum eigentlichen Download kommt. Das geht jetzt einfacher!

Zwingend erforderlich ist dafür allerdings ein Account und Abo bei der Süddeutschen, sodass du den Zugriff auf das ePaper hast.

## Installation
Mit `pip` installieren:
```shell script
pip install git+https://github.com/SiKreuz/SZ2pdf
```

Zum Updaten der Software muss die Option `-U` verwendet werden. Für eine system-weite Installation musst du natürlich root-Rechte besitzen.

## Benutzung
```shell script
Usage: SZ2pdf [OPTIONS]

Options:
  -cd, --show-config-dir  Prints the path of the config directory.
  -h, --help              Show this message and exit.
```

### Konfiguration
Die Konfigurationsdatei liegt im für das Betriebssystem üblichen Ordner. Unter Linux-Systemen wäre das beispielsweise `~/.config/SZ2pdf`. Falls du den Standard-Ordner nicht kennst, kannst du ihn mit der Option `-cd` ausgeben lassen.

Die Konfigurationsdatei wird bei der ersten Ausführung des Tools erstellt.
