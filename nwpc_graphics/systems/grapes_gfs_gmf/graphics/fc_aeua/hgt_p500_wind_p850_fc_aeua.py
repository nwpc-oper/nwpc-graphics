# coding: utf-8
"""
500hPa 高度场＋850hPa 风场

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=03130203
"""
from nwpc_graphics.systems.grapes_gfs_gmf.graphics.fc_aeua import FcAeuaPlotter


class Plotter(FcAeuaPlotter):
    plot_types = [
        "hgt_p500_wind_p850_fc_aeua"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        FcAeuaPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "GFS_GRAPES_HGT_P500+WIND_P850_FC_AEUA.ncl"
