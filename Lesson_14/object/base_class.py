from abc import ABC, abstractmethod

class Base_CLS:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def validate_data(self):
        pass

    @abstractmethod
    def add_data(self):
        pass

    @abstractmethod
    def insert_data(self):
        pass

    @abstractmethod
    def update_data(self):
        pass

    @abstractmethod
    def delete_data(self):
        pass

    @abstractmethod
    def search_data(self):
        pass