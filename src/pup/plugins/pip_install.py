"""
PUP Plugin implementing the 'pup.pip-install' step.
"""

import logging


_log = logging.getLogger(__name__)



class Step:

    """
    Downloads 
    """

    @staticmethod
    def usable_in(ctx):
        return (
            (ctx.pkg_platform == 'darwin') or
            (ctx.pkg_platform == 'win32')
        ) and (
            (ctx.pkg_platform == ctx.tgt_platform)
        )

    def __call__(self, ctx, _dsp):
        _log.warning(
            'TODO: pip install src',
        )
