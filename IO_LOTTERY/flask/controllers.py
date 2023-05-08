from dataclasses import dataclass

from IO_LOTTERY.repositories import UserRepository

@dataclass
class AddUserRequest:
    data: dict


class AddUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def add(self, request: AddUserRequest) -> None:
        self._repository.add(request.data)
        print(request.data)


class GetUserController:
    def get(self, id: int):
        raise NotImplementedError

class UserController:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self):
        raise NotImplementedError()

    def get_user_by_id(self, user_id: int):
        raise NotImplementedError()

    def create_user(self, user: dict):
        return self.user_repository.create_user(user)

    def update_user(self, user_id: int, user: dict):
        return self.user_repository.update_user(user_id, user)

    def delete_user(self, user_id: int):
        raise NotImplementedError()
