from plyer import notification

# title: title of the notification
# message: Message of the Notification
# app_name: Name of the app launching this notification
# app_icon: Icon to be displayed along with the message
# timeout: time to display the message for, defaults to 10
# ticker: time to display on the statys bar as the notification arrives
# toast: simple message instead of full notification
title = 'Hello Amazing people'
message = 'Make something useful'

notification.notify(
    title=title,
    message=message,
    app_icon="/home/joao/books.png",
    timeout=5)
