from database.impianto_DAO import ImpiantoDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Model:
    def __init__(self):
        self._impianti = None
        self.load_impianti()

        self.__sequenza_ottima = []
        self.__costo_ottimo = -1

    def load_impianti(self):
        """ Carica tutti gli impianti e li setta nella variabile self._impianti """
        self._impianti = ImpiantoDAO.get_impianti()

    def get_consumo_medio(self, mese:int):
        risultati = []
        for impianto in self._impianti:
            consumi = impianto.get_consumi()
            consumi_mese = 0
            giorni = []
            for c in consumi:
                mese_consumo = c.data.month
                if mese_consumo == mese:
                    consumi_mese += c.kwh
                    giorni.append(c.data.day)
            media_consumo = consumi_mese/len(giorni)
            risultati.append((impianto.nome, media_consumo))
        return risultati

        """
        Calcola, per ogni impianto, il consumo medio giornaliero per il mese selezionato.
        :param mese: Mese selezionato (un intero da 1 a 12)
        :return: lista di tuple --> (nome dell'impianto, media), es. (Impianto A, 123)
        """
        # TODO

    def get_sequenza_ottima(self, mese:int):
        """
        Calcola la sequenza ottimale di interventi nei primi 7 giorni
        :return: sequenza di nomi impianto ottimale
        :return: costo ottimale (cioè quello minimizzato dalla sequenza scelta)
        """
        self.__sequenza_ottima = []
        self.__costo_ottimo = -1
        consumi_settimana = self.__get_consumi_prima_settimana_mese(mese)

        self.__ricorsione([], 1, None, 0, consumi_settimana)

        # Traduci gli ID in nomi
        id_to_nome = {impianto.id: impianto.nome for impianto in self._impianti}
        sequenza_nomi = [f"Giorno {giorno}: {id_to_nome[i]}" for giorno, i in enumerate(self.__sequenza_ottima, start=1)]
        return sequenza_nomi, self.__costo_ottimo

    def __ricorsione(self, sequenza_parziale, giorno, ultimo_impianto, costo_corrente, consumi_settimana):
        """ Implementa la ricorsione """
        # TODO

        if giorno > 7:
            return


        for impianto in self._impianti:
            id_impianto = impianto.id
            consumi = consumi_settimana[id_impianto]
            consumo_giorno = consumi[giorno-1]
            costo_giorno = consumo_giorno

            if ultimo_impianto is not None and ultimo_impianto != id_impianto:
                costo_giorno += 5

            nuovo_costo = costo_corrente + costo_giorno
            nuova_sequenza = sequenza_parziale + [id_impianto]
            print(sequenza_parziale, nuovo_costo)
            self.__ricorsione(nuova_sequenza, giorno + 1, id_impianto, nuovo_costo, consumi_settimana)















    def __get_consumi_prima_settimana_mese(self, mese: int):
        risultato = {}
        for impianto in self._impianti:
            consumi = impianto.get_consumi()
            consumi_giorni = []
            for c in consumi:
                if c.data.month == mese and c.data.day in range(1, 8):
                    consumi_giorni.append(c.kwh)
            risultato[impianto.id] = consumi_giorni
        print(risultato)
        return risultato


        """
        Restituisce i consumi dei primi 7 giorni del mese selezionato per ciascun impianto.
        :return: un dizionario: {id_impianto: [kwh_giorno1, ..., kwh_giorno7]}
        """
        # TODO

