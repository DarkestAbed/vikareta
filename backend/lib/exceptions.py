class DatabaseDoesNotExist(Exception):
    """Exception raised when a SQLite3 database file is not found on the system

    Args:
        Exception (class): super class, inherited 
    """
    def __init__(self, file: str):
        """Constructor method of the `DatabaseDoesNotExist` class

        Args:
            file (str): file path or file name of the SQLite3 database not found

        Returns:
            None: as expected, the constructor method returns `None`
        """
        message = f"Database file '{file}' does not exists on the 'proj/assets/' folder"
        super().__init__(message)
        return None
