import pathlib

from nwpc_graphics.systems.grapes_meso_3km._plotter import SystemPlotter
from nwpc_graphics._logging import get_logger
from nwpc_graphics._util import load_plotters_from_paths
from nwpc_graphics import get_config


logger = get_logger()


def _load_plotters():
    plotters = load_plotters_from_paths(
        [pathlib.Path(pathlib.Path(__file__).parent, "graphics")],
        SystemPlotter,
    )
    return plotters


plotters = _load_plotters()


def draw_plot(plot_type: str, start_date: str, start_time: str, forecast_time: str):
    """Draw images and save them in work directory.

    Parameters
    ----------
    plot_type : str
        Plot type according to systems.
    start_date: str
        Start date, YYYYMMDD
    start_time: str
        Start hour, HH
    forecast_time: str
        Forecast time duration, such as 3h.

    Raises
    -------
    ValueError
        plot_type is not found
    """
    plot_module = _get_plotter_class(plot_type)
    if plot_type is None:
        raise ValueError(f"plot type is not supported:{plot_type}")

    plotter = plot_module.create_plotter(
        graphics_config=get_config(),
        start_date=start_date,
        start_time=start_time,
        forecast_time=forecast_time)

    plotter.run_plot()


def show_plot(plot_type: str, start_date: str, start_time: str, forecast_time: str):
    """Draw images and show them in Jupyter Notebook.

    Parameters
    ----------
    plot_type : str
        Plot type according to systems.
    start_date: str
        Start date, YYYYMMDD
    start_time: str
        Start hour, HH
    forecast_time: str
        Forecast time duration, such as 3h.

    Raises
    -------
    ValueError
        plot_type is not found
    """
    plot_module = _get_plotter_class(plot_type)
    if plot_module is None:
        raise ValueError(f"plot type is not supported:{plot_type}")

    plotter = plot_module.create_plotter(
        graphics_config=get_config(),
        start_date=start_date,
        start_time=start_time,
        forecast_time=forecast_time)

    plotter.run_plot()
    return plotter.show_plot()


def _get_plotter_class(plot_type: str):
    """Get plot module

    Parameters
    ----------
    plot_type : str
        Plot type according to systems.

    Returns
    -------
    module or None
        plotter module, return None if not found.
    """
    if plot_type in plotters:
        return plotters[plot_type]
    else:
        return None