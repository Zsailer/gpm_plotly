# Try using setuptools first, if it's installed
try:
    from setuptools import setup
except:
    from distutils.core import setup

# define all packages for distribution
packages = ['gpm_plotly']

setup(name='gpm_plotly',
      version='0.1',
      description='3d genotype-phenotype map visualization powered by Plotly (offline).',
      author='Zach Sailer',
      author_email='zachsailer@gmail.com',
      url='https://github.com/harmslab/gpm-plotly',
      packages=packages,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
      ],
      zip_safe=False)
