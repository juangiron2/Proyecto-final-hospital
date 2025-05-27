from abc import ABC, abstractmethod

class CRUD(ABC):
    @abstractmethod
    def crear(self, obj): pass

    @abstractmethod
    def obtener_por_id(self, id): pass

    @abstractmethod
    def actualizar(self, obj): pass

    @abstractmethod
    def eliminar(self, id): pass
