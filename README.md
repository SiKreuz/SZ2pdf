# SZ2pdf
Dieses Tool soll dabei helfen, immer die neueste Ausgabe der [Süddeutschen Zeitung](https://www.sueddeutsche.de/) als PDF herunterzuladen.
Wenn man sich über die Website einloggen muss, sind es leider nervig viele Klicks, bis man zum eigentlichen Download kommt.
Das geht jetzt einfacher!

Zwingend erforderlich ist dafür natürlich ein Account und Abo bei der Süddeutschen Zeitung, sodass du den Zugriff auf das ePaper hast.

## Installation
Mit `pip` installieren:
```shell script
pip install git+https://github.com/SiKreuz/SZ2pdf
```

Zum Updaten der Software muss die Option `-U` verwendet werden. Für eine systemweite Installation sind root-Rechte nötig.

## Konfiguration
Der Konfigurationsordner liegt in dem für das Betriebssystem typischen Ordner. Unter Linux wäre das `~/.config/SZ2pdf`.
Dort musst du deine Logindaten angeben und kannst den Download-Ordner festlegen und die Version der Zeitung angeben, die du gerne hättest.

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
