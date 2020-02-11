"""
850hPa 高度场

图片暂时没有外网访问渠道。
"""
from nwpc_graphics.systems.grapes_gfs_gmf.graphics.gams import GamsPlotter


class Plotter(GamsPlotter):
    plot_types = [
        "gams.hgt_850"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        GamsPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "gams_hgt_850.ncl"

    def get_image_list(self):
        return [{
            "path": f"./EGH_ASIA_L85_P9_{self.start_time}00{self.forecast_hour}00.png"
        }]
