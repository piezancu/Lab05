import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._diz_corsi = {}
        self._corso_selezionato = None

    def handle_DDcorsi(self):
        corsi_trovati = self._model.get_corsi()
        for corso in corsi_trovati:
            self._view.ddCorso.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
        self._view.update_page()

    def leggi_corso(self,e):
        self._corso_selezionato = self._view.ddCorso.value

    def handleCercaIscritti(self,e):
        if self._corso_selezionato is None:
            self._view.create_alert("Selezionare un corso")
            return
        iscritti = self._model.get_studenti_corso(self._corso_selezionato)
        if iscritti is None:
            self._view.create_alert("Problema nella connessione!")
            return
        self._view.txt_result.controls.clear()
        if len(iscritti) == 0:
            self._view.txt_result.controls.append(ft.Text("Non ci sono iscritti al corso"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:"))
            for studente in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{studente}"))
            self._view.update_page()


    def handleCercaStudente(self, e):
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("Scrivere prima una matricola")
            return
        studente = self._model.cerca_studente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel database")
            return
        else:
            self._view.txt_nome_studente.value = f"{studente.nome}"
            self._view.txt_cognome_studente.value = f"{studente.cognome}"
        self._view.update_page()


    def handleCercaCorsi(self, e):
        matricola = self._view.txt_matricola.value
        studente = self._model.cerca_studente(matricola)
        if matricola == "":
            self._view.create_alert("Scrivere prima una matricola")
            return
        elif studente is None:
            self._view.create_alert("Matricola non presente nel database")
            return
        else:
            lista_corsi_studente = self._model.get_corsi_studente(matricola)
            if len(lista_corsi_studente) == 0:
                self._view.create_alert("La matricola indicata non risulta iscritta ad alcun corso")
            else:
                self._view.txt_result.controls.clear()
                for corso in lista_corsi_studente:
                    self._view.txt_result.controls.append(ft.Text(f"{corso.nome} ({corso.codins})"))
                self._view.update_page()
