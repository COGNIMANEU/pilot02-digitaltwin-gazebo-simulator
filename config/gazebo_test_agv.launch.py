from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

import os
import uuid

def generate_launch_description():
    config_dir = '/config'
    world_path = os.path.join(config_dir, 'worlds', 'agv_circling_room.world')
    agv_model_path = os.path.join(config_dir, 'models', 'simple_agv', 'model.sdf')
    table_model_path = os.path.join(config_dir, 'models', 'circular_table', 'model.sdf')

    agv_entity_name = 'simple_agv_' + str(uuid.uuid4())[:8]
    table_entity_name = 'simple_table_' + str(uuid.uuid4())[:8]

    return LaunchDescription([

        # Launch Ignition Gazebo with the selected world
        ExecuteProcess(
            cmd=['ign', 'gazebo', '-r', world_path],
            output='screen'
        ),

        # Spawn AGV
        ExecuteProcess(
            cmd=[
                'ign', 'service', '-s', '/world/default/create',
                '--reqtype', 'ignition.msgs.EntityFactory',
                '--reptype', 'ignition.msgs.Boolean',
                '--timeout', '3000',
                '--req',
                f'name: "{agv_entity_name}" sdf_filename: "{agv_model_path}"'
            ],
            output='screen'
        ),

        # Spawn Table
        ExecuteProcess(
            cmd=[
                'ign', 'service', '-s', '/world/default/create',
                '--reqtype', 'ignition.msgs.EntityFactory',
                '--reptype', 'ignition.msgs.Boolean',
                '--timeout', '3000',
                '--req',
                f'name: "{table_entity_name}" sdf_filename: "{table_model_path}"'
            ],
            output='screen'
        )
    ])
