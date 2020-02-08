"""
250hPa 散度

图片暂时没有外网访问渠道。
"""
from nwpc_graphics.systems.grapes_gfs_gmf.graphics.gams import GamsPlotter


class Plotter(GamsPlotter):
    plot_types = [
        "gams.div_250"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        GamsPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "gams_div_250.ncl"

    def _get_image_list(self):
        return [{
            "path": f"./EDI_ASIA_L25_P9_{self.start_time}00{self.forecast_hour}00.png"
        }]