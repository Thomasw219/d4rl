from distutils.core import setup
from platform import platform

from setuptools import find_packages

setup(
    name='d4rl',
    version='1.1',
    install_requires=['gym',
                      'numpy',
                      'mujoco_py',
                      'pybullet',
                      'h5py',
                      'termcolor',  # adept_envs dependency
                      'click',  # adept_envs dependency
                      'dm_control' if 'macOS' in platform() else
                      'dm_control @ git+git://github.com/deepmind/dm_control@644d9e0047f68b35a6f8b79e5e8493e2910563af#egg=dm_control',
                      'mjrl @ git+git://github.com/aravindr93/mjrl@3871d93763d3b49c4741e6daeaebbc605fe140dc#egg=mjrl'],
    packages=find_packages(),
    package_data={'d4rl': ['locomotion/assets/*',
                           'hand_manipulation_suite/assets/*',
                           'hand_manipulation_suite/Adroit/*',
                           'hand_manipulation_suite/Adroit/gallery/*',
                           'hand_manipulation_suite/Adroit/resources/*',
                           'hand_manipulation_suite/Adroit/resources/meshes/*',
                           'hand_manipulation_suite/Adroit/resources/textures/*',
                           ]},
    include_package_data=True,
)
