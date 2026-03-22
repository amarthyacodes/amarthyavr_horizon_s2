from setuptools import find_packages, setup

package_name = 'distance_demo_bonus'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ami',
    maintainer_email='amarthyavr@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': ['sensor_node = distance_demo_bonus.sensor_node:main',
        'decision_node = distance_demo_bonus.decision_node:main',
        'command_listener = distance_demo_bonus.command_listener:main',
        ],
    },
)
