import cx_Freeze
import sys

executables = [cx_Freeze.Executable("src/__main__.py")]
options = {
    'build_exe': {
        'includes': [
            'visualize_example',
            'inputbox'
        ],"include_files":[("src/assets/ball.bmp","assets/ball.bmp")],
        'path': sys.path + ['src']
    }
}

cx_Freeze.setup(
    name="Fajne",
      options=options,
      executables=executables
    )