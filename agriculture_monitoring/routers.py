class DatabaseRouter:
    """
    A router to control database operations
    """
    def db_for_read(self, model, **hints):
        """
        Suggest the database that should be used for read operations
        """
        if model._meta.app_label == 'your_new_app':
            return 'second_db'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Suggest the database that should be used for writes
        """
        if model._meta.app_label == 'your_new_app':
            return 'second_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the same database
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Control which apps go to which database
        """
        if app_label == 'your_new_app':
            return db == 'second_db'
        return db == 'default' 