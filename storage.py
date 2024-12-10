import json
from abc import ABC, abstractmethod
from uuid import uuid4
from pathlib import Path


class BaseStorage(ABC):

    @abstractmethod
    def create_car(self, car: dict):
        pass

    @abstractmethod
    def get_cars(self, skip: int = 0, limit: int = 10, search_param: str = ''):
        pass

    @abstractmethod
    def get_cars_info(self, car_id: str):
        pass

    @abstractmethod
    def update_cars(self, car_id: str, brand: str):
        pass

    @abstractmethod
    def delete_cars(self, book_id: str):
        pass


class JSONStorage(BaseStorage):
    def __init__(self):
        self.file_name = 'storage.json'

        my_file = Path(self.file_name)
        if not my_file.is_file():
            with open(self.file_name, mode='w', encoding='utf-8') as file:
                json.dump([], file, indent=4)

    def create_car(self, car: dict):
        with open(self.file_name, mode='r') as file:
            content: list[dict] = json.load(file)

        car['id'] = uuid4().hex
        content.append(car)
        with open(self.file_name, mode='w', encoding='utf-8') as file:
            json.dump(content, file, indent=4)
            return car

    def get_cars(self, skip: int = 0, limit: int = 10, search_param: str = ''):
        with open(self.file_name, mode='r') as file:
            content: list[dict] = json.load(file)

        if search_param:
            data = []
            for car in content:
                if search_param in car['brand']:
                    data.append(car)
            sliced = data[skip:][limit:]
            return sliced

        sliced = content[skip:][limit:]
        return sliced

    def get_cars_info(self, car_id: str):
        with open(self.file_name, mode='r') as file:
            content: list[dict] = json.load(file)
        for car in content:
            if car_id == car['id']:
                return car
        return {}

    def update_cars(self, car_id: str, brand: str):
        with open(self.file_name, mode='r') as file:
            content: list[dict] = json.load(file)
        was_found = False
        for car in content:
            if car_id == car['id']:
                car['brand'] = brand
                was_found = True
                break
        if was_found:
            with open(self.file_name, mode='w', encoding='utf-8') as file:
                json.dump(content, file, indent=4)
        raise ValueError()

    def delete_cars(self, car_id: str):
        with open(self.file_name, mode='r') as file:
            content: list[dict] = json.load(file)
        was_found = False
        for car in content:
            if car_id == car['id']:
                content.remove(car)
                was_found = True
                break
        if was_found:
            with open(self.file_name, mode='w', encoding='utf-8') as file:
                json.dump(content, file, indent=4)
        raise ValueError()

storage = JSONStorage()
