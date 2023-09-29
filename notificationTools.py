from winotify import Notification, audio

notificacao = Notification(app_id="Nota", title="Notificação da automação",
                           msg="Olha esse site que daora", duration="short")

notificacao.set_audio(audio.LoopingAlarm, loop=False)

notificacao.add_actions(label="Aperta no botão ai", launch="https://github.com/sscolpaert/notificationTool")

notificacao.show()