from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("abb_irb4600_40_255", package_name="abb_crb15000_5_95_moveit_config").to_moveit_configs()
    return generate_demo_launch(moveit_config)
