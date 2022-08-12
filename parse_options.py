class ParseOptions:
    @classmethod
    def display_menu(cls):
        print('*** MENU PRINCIPAL ***')
        print('1. Cargar archivo')
        print('2. Exportar cantidad de mesas por región')
        print('3. Exportar recuento general')
        print('4. Exportar resultados en local')
        print('0. Salir')

    @classmethod
    def get_option(cls):
        ParseOptions.display_menu()
        return int(input('Selecciona una opción: '))