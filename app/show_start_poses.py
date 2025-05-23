import time
from icem_mpc.config_crearor import get_tabale_top_start_pos, prepare_env_config
from icem_mpc.reach_pose_env import ReachPoseEnv
import numpy as np

DEFAULT_CAMERA_CONFIG = {
    "distance": 1.5,
    "azimuth": 90,
    "elevation": 90,
}


def show_start_poses():
    POSE_NUM, obj_name, key_body_final_pos, config, final_act_pose_sh_hand = prepare_env_config()
    start_poses, x_pose, y_pose = get_tabale_top_start_pos()

    for st_pose in start_poses:
        config.hand_starting_pose = st_pose
        env = ReachPoseEnv(
            config,
            key_pose_dict=key_body_final_pos,
            render_mode="human",
            default_camera_config=DEFAULT_CAMERA_CONFIG,
            width=1600,
            height=1200,
        )
        env.kinematics_debug = True
        for _ in range(100):
            reduced_obs, reward, _, _, debug_dict = env.step(np.zeros(len(env.action_space.sample())))
            time.sleep(0.005)

        env.close()


if __name__ == "__main__":
    show_start_poses()
