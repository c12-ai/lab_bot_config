from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("rizon", package_name="lab_bot_config").planning_pipelines().to_moveit_configs()
    return generate_move_group_launch(moveit_config)
