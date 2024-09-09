class ValeurNegativeException(Exception):

    def __init__(self, message : str = "La valeur ne peut pas être négative."):
        super().__init__(message)