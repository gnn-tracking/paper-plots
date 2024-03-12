from pathlib import Path

from gnn_tracking.utils.loading import TrackingDataModule


def get_dm(*, n_val=5, setup=True, v=8) -> TrackingDataModule:
    """Get default tracking data module"""
    dm = TrackingDataModule(
        identifier="point_clouds_v8",
        train={
            "dirs": [
                f"/scratch/gpfs/IOJALVO/gnn-tracking/object_condensation/point_clouds_v{v}/part_1/"
            ],
            # If you run into memory issues, reduce this
        },
        val={
            "dirs": [
                f"/scratch/gpfs/IOJALVO/gnn-tracking/object_condensation/point_clouds_v{v}/part_9/"
            ],
            "stop": n_val,
        },
    )
    if setup:
        dm.setup(stage="fit")
    return dm


model_exchange_path = Path(
    "/scratch/gpfs/IOJALVO/gnn-tracking/object_condensation/model_exchange"
)
