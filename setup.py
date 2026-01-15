from setuptools import setup

package_name = 'tb3_avoid'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amjad',
    maintainer_email='st20341331@outlook.cardiffmet.ac.uk',
    description='Simple TurtleBot3 Obstacle Avoidance',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'avoid = tb3_avoid.avoid:main',
        ],
    },
)

