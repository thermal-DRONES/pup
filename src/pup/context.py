"""
Packaging Context.
"""

import logging
import pathlib
from urllib import parse
import sys


_log = logging.getLogger(__name__)

class Context:

    def __init__(
        self,
        *,
        src,
        launch_module,
        launch_pyflags,
        nice_name,
        icon_path,
        license_path,
        ignore_plugins,
        platform,
        python_version,
    ):

        self.src = src
        self._icon_path = None
        self.icon_path = None
        self._license_path = None
        self.license_path = None
        self.package_name = ""
        self.app_id = ""
        self.apple_user = ""
        self.team_id = ""
        self.app_password = ""
        self.sign_extra = []
        self.src_wheel = None
        self.src_metadata = None
        self.relocatable_root = None

        self.python_runtime_dir = None
        self.python_rel_exe = None
        self.python_rel_scripts = None
        self.python_rel_stdlib = None
        self.python_rel_site_packages = None
        self.python_rel_tcl_library = None

        self.final_artifact = None

        sys.path.insert(1, src)
        try:
            import pup_setup
            if hasattr(pup_setup,"icon_path"):
                self.icon_path = pathlib.Path(pup_setup.icon_path).absolute() 
            if hasattr(pup_setup,"license_path"):
                self.license_path = pathlib.Path(pup_setup.license_path).absolute()
            if hasattr(pup_setup,"nice_name"):
                self.given_nice_name = pup_setup.nice_name
            if hasattr(pup_setup,"package_name"):
                self.package_name = pup_setup.package_name     
            if hasattr(pup_setup,"app_id"):
                self.app_id = pup_setup.app_id
            if hasattr(pup_setup,"team_id"):
                self.team_id = pup_setup.team_id
            if hasattr(pup_setup,"apple_user"):
                self.apple_user = pup_setup.apple_user
            if hasattr(pup_setup,"app_password"):
                self.app_password = pup_setup.app_password
            if hasattr(pup_setup,"sign_extra"):
                self.sign_extra = pup_setup.sign_extra
        except:
            _log.error("CTX import pup setup error", exc_info=True)
        
        self.launch_module = launch_module
        self.launch_pyflags = tuple(pyflag for pyflag in launch_pyflags if pyflag)
        self.given_nice_name = nice_name

        if icon_path:
            self.icon_path = pathlib.Path(icon_path).absolute() 
        if license_path:
            self.license_path = pathlib.Path(license_path).absolute()
        

        self.ignore_plugins = ignore_plugins
        self.pkg_platform = platform
        self.tgt_platform = platform
        self.tgt_python_version = python_version

        


    @property
    def nice_name(self):
        """
        User facing packaged name.
        """
        return self.given_nice_name or self.src_metadata.name


    @property
    def icon_path(self):
        """
        Path to the packaged application Icon.
        """
        return self._icon_path


    @icon_path.setter
    def icon_path(self, value):

        if value and not value.exists():
            raise EnvironmentError(f'Non-existent icon path {str(value)!r}.')
        self._icon_path = value


    @property
    def license_path(self):
        """
        Path to the license text file.
        """
        return self._license_path

    @license_path.setter
    def license_path(self, value):

        if value and not value.exists():
            raise EnvironmentError(f'Non-existent license path {str(value)!r}.')
        self._license_path = value


    @property
    def application_id(self):
        """
        Returns the application identifier built from the package's home_page
        URL, consisting of two-sets of '.'-separated strings: the reverse DNS
        host/domain part, followed by the in-order path components.

        Example:
        - home_page='https://example.com/a/path'
        - bundle_id='com.example.a.path'
        """
        if self.app_id:
            return self.app_id
        
        url_parts = parse.urlsplit(self.src_metadata.home_page)
        out =  '.'.join((
            '.'.join(reversed(url_parts.netloc.split('.'))),
            '.'.join(filter(None, url_parts.path.split('/')))
        ))
        return out+self.src_metadata.name
        
