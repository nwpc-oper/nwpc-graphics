# coding: utf-8
"""
500hPa高度 + 500hPa风场

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=03130102
"""
from nwpc_graphics.systems.grapes_gfs_gmf.graphics.fc_ahne import FcAhnePlotter


class Plotter(FcAhnePlotter):
    plot_types = [
        "hgt_p500_fc_ahne"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        FcAhnePlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "GFS_GRAPES_HGT_P500_FC_AHNE.ncl"
