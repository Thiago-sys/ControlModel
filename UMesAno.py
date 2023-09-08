class MesAno:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MesAno, cls).__new__(cls)
            cls._instance.mes = None
            cls._instance.ano = None
        return cls._instance

    def set_mes_ano(self, mes, ano):
        self.mes = mes
        self.ano = ano

    def get_mes(self):
        return self.mes

    def get_ano(self):
        return self.ano
