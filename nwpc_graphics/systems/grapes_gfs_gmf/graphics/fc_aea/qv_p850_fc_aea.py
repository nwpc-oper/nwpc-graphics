# coding: utf-8
"""
850hPa 比湿

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=0313031102
"""
from nwpc_graphics.systems.grapes_gfs_gmf.graphics.fc_aea import FcAeaPlotter


class Plotter(FcAeaPlotter):
    plot_types = [
        "qv_p850_fc_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        FcAeaPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "GFS_GRAPES_QV_P850_FC_AEA.ncl"
