from winotify import Notification, audio

notificacao = Notification(app_id="Código Python", title="Notificação da Automação",
                           msg="Acabou a zoeira, vai estudar Python, se inscreve no canal",
                           duration="short")

notificacao.set_audio(audio.LoopingAlarm, loop=False)

notificacao.add_actions(label="Aprenda Python", launch="https://github.com/sscolpaert/notificationTool")

notificacao.show()
