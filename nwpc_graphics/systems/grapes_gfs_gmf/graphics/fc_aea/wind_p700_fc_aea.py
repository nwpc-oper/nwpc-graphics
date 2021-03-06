# coding: utf-8
"""
700hPa 风场

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=0313030401
"""
from nwpc_graphics.systems.grapes_gfs_gmf.graphics.fc_aea import FcAeaPlotter


class Plotter(FcAeaPlotter):
    plot_types = [
        "wind_p700_fc_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        FcAeaPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "GFS_GRAPES_WIND_P700_FC_AEA.ncl"
