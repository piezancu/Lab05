import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._diz_corsi = {}

    def handle_DDcorsi(self):
        corsi_trovati = self._model.get_corsi()
        for corso in corsi_trovati:
            self._view.ddCorso.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
        self._view.update_page()

    def handleCercaIscritti(self):
        pass

    def handleCercaStudente(self):
        pass

    def handleCercaCorsi(self):
        pass
