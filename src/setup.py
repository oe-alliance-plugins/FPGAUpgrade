from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.FPGAUpgrade'
setup(name='enigma2-plugin-systemplugins-fpgaupgrade',
       version='3.0',
       description='Upgrade your system FPGA',
       package_dir={pkg: 'FPGAUpgrade'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
