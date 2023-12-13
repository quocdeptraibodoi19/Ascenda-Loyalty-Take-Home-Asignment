class Merchant:
    def __init__(self, id: int, name: str, distance: float, *args, **kwargs) -> None:
        self._id = id
        self._name = name
        self._distance = distance

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def distance(self) -> float:
        return self._distance

    def __str__(self):
        return f"Merchant(id={self.id}, name='{self.name}', distance={self.distance})"
