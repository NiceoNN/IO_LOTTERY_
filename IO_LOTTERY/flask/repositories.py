class UserRepository:
    def __init__(self, dao):
        self.dao = dao

    def get_all_users(self):
        raise NotImplementedError()

    def get_user_by_id(self, user_id):
        raise NotImplementedError()

    def create_user(self, user):
        raise NotImplementedError()

    def update_user(self, user_id, user):
        raise NotImplementedError()

    def delete_user(self, user_id):
        raise NotImplementedError()


class UserDao:
    def get_all_users(self):
        raise NotImplementedError()

    def get_user_by_id(self, user_id):
        raise NotImplementedError()

    def create_user(self, user):
        return user

    def update_user(self, user_id, user):
        return user

    def delete_user(self, user_id):
        raise NotImplementedError()