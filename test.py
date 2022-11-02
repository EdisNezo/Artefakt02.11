def autoStart(event):
    if len(StartPage.experimentName) > 0 and StartPage.files is not None:
        if StartPage.getStatus():
            StartPage.updateRepetitions()
            StartPage.hide()
            createTable(StartPage.experimentName)
            getRandomTable(TableInfo(StartPage.files).getTableAllInfo())
            StartPage.hide()
        main.auto = True
        countdown = Countdown(window, 3)
        countdown.start(autoSelectEmotion)
    else:
        messagebox.showerror("Error",
                             "Bitte geben Sie einen Namen für das Experiment ein und wählen Sie Tabellen aus, die sie benutzen wollen!")
