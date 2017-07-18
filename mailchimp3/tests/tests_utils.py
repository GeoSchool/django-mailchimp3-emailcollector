class AppSettingsManager(object):
    """ Manager that allow to override application settings """

    def __init__(self, module, app_settings_name='app_settings', **kwargs):
        """ Initialize the manager, the module should have an app_settings property that will get patched """
        self.module = module
        self.app_settings_name = app_settings_name
        self.kwargs = kwargs
        self.originals = {}

    def __enter__(self):
        """ Patch the app setting values passed as parameters """
        for key, value in self.kwargs.items():
            app_settings_module = getattr(self.module, self.app_settings_name)
            self.originals[key] = getattr(app_settings_module, key)
            setattr(app_settings_module, key, value)

    def __exit__(self, type, value, traceback):
        """ Restore the app setting values """
        for key, value in self.originals.items():
            if value is not None:
                app_settings_module = getattr(
                    self.module, self.app_settings_name
                )
                setattr(app_settings_module, key, value)


class ExtraTestToolsMixin(object):
    """ Mixin adding an app_settings context manager to override application settings """
    app_settings = AppSettingsManager
