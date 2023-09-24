from winotify import Notification, audio

notificacao = Notification(app_id="Nota", title="Notificação da automação",
                           msg="Entra no site ai", duration="short")

notificacao.set_audio(audio.LoopingAlarm, loop=False)

notificacao.add_actions(label="Aprenda Python", launch="https://github.com/sscolpaert/notificationTool")

notificacao.show()
