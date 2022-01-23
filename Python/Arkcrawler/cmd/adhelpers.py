from plyer import notification as notif


def newsnotification(titulo):
    notif.notify(
        title=titulo,
        message="a Arknights Event was announced.",
        app_icon="/home/joao/projects/repositories/persacademy/Python/Arkcrawler/images/ArknightsLogo.png",
        timeout=6
    )
