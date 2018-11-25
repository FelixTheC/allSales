class StaffRouter(object):
    pass
    # """
    # A router to control all database operations on models in the
    # staff application.
    # """
    # def db_for_read(self, model, **hints):
    #     """
    #     Attempts to read staff models go to auth_db.
    #     """
    #     if model._meta.app_label == 'staff':
    #         return 'staff_db'
    #     return None
    #
    # def db_for_write(self, model, **hints):
    #     """
    #     Attempts to write staff models go to staff_db.
    #     """
    #     if model._meta.app_label == 'staff':
    #         return 'staff_db'
    #     return None
    #
    # def allow_relation(self, obj1, obj2, **hints):
    #     """
    #     Allow relations if a model in the staff app is involved.
    #     """
    #     if obj1._meta.app_label == 'staff' or obj2._meta.app_label == 'staff':
    #        return True
    #     return None
    #
    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     """
    #     Make sure the staff app only appears in the 'staff_db'
    #     database.
    #     """
    #     if app_label == 'staff':
    #         return db == 'staff_db'
    #     return None