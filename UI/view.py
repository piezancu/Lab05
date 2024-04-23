import flet as ft
from model.corso import Corso
from UI.controller import Controller

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.txt_result = None
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddCorso = None
        self.btn_cerca_iscritti = None
        self.txt_matricola = None
        self.txt_nome_studente = None
        self.txt_cognome_studente = None
        self.btn_cerca_studente = None
        self.btn_cerca_corsi = None
        # self.btn_iscrivi_studente = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW 1
        self.ddCorso = ft.Dropdown(label="Corso", width=500, options=[], on_change=self.controller.leggi_corso)
        self._controller.handle_DDcorsi()
        self.btn_cerca_iscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self.controller.handleCercaIscritti)

        row1 = ft.Row([self.ddCorso, self.btn_cerca_iscritti],
                      alignment=ft.MainAxisAlignment.CENTER)

        #ROW 2
        # text field for the matricola
        self.txt_matricola = ft.TextField(
            label="matricola",
            width=200,
            hint_text="Inserisci la matricola"
        )
        self.txt_nome_studente = ft.TextField(read_only=True, label="nome")
        self.txt_cognome_studente = ft.TextField(read_only=True, label="cognome")

        row2 = ft.Row([self.txt_matricola, self.txt_nome_studente, self.txt_cognome_studente],
                      alignment=ft.MainAxisAlignment.CENTER)

        #ROW 3
        self.btn_cerca_studente = ft.ElevatedButton(text="Cerca Studente", on_click=self.controller.handleCercaStudente)
        self.btn_cerca_corsi = ft.ElevatedButton(text="Cerca Corsi", on_click=self.controller.handleCercaCorsi)

        row3 = ft.Row([self.btn_cerca_studente, self.btn_cerca_corsi],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
