from dataclasses import dataclass


@dataclass
class AddUserRequest:
    json: dict


class AddOtherController:
    def add(self, request: AddUserRequest) -> None:
        print(request.json)