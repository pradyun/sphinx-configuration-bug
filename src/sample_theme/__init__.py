"""A demonstrator for a Sphinx bug."""

from pathlib import Path

THEME_PATH = (Path(__file__).parent / "sample_theme").resolve()

__version__ = "1.0.0"


def _builder_inited(app):
    config = app.config
    print("="*100)
    print(f"{sorted(vars(config))=}")
    print(f"{config.sample_theme_configuration_value=}")
    print(f"{config._raw_config['sample_theme_configuration_value']=}")

    config.init_values()

    print("="*100)
    print(f"{sorted(vars(config))=}")
    print(f"{config.sample_theme_configuration_value=}")
    print(f"{config._raw_config['sample_theme_configuration_value']=}")

    print("="*100)


def setup(app):
    """Entry point for sphinx theming."""
    app.require_sphinx("4.0")

    app.add_config_value(
        "sample_theme_configuration_value", default="default", rebuild="env", types=[str]
    )

    app.add_html_theme("sample_theme", str(THEME_PATH))

    app.connect("builder-inited", _builder_inited)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
