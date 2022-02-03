from plyer import notification as notif

def newsnotification(titulo, msg):
    notif.notify(
        title=titulo,
        message=msg,
        app_icon="/home/joao/projects/repositories/persacademy/Python/Arkcrawler/images/ArknightsLogo.png",
        timeout=6
    )
