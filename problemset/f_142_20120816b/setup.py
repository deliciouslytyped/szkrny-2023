#TODO this is a clusterfuck, look into py2exe freeze api as well, see this whole thing is deprecated https://github.com/py2exe/py2exe/blob/00db2d2cf942ad71c4a35f5fcf64c4db2ff82967/py2exe/distutils_buildexe.py
#see also via https://web.archive.org/web/20220119100653/crazedmonkey.com/blog/python/pkg_resources-with-py2exe.html
#TODO well, almost....

from distutils.core import setup
import py2exe, sys, os
from glob import glob
from pathlib import Path

from modulefinder import ModuleFinder

finder = ModuleFinder()
finder.run_script('solution.py')
print(finder.report())

from py2exe.build_exe import py2exe as build_exe

class MediaCollector(build_exe):
    def copy_extensions(self, extensions):
        super(MediaCollector, self).copy_extensions(extensions)

        # Create the media subdir where the
        # Python files are collected.
        media = os.path.join('foo', 'media')
        full = os.path.join(self.collect_dir, media)
        if not os.path.exists(full):
            self.mkpath(full)

        # Copy the media files to the collection dir.
        # Also add the copied file to the list of compiled
        # files so it will be included in zipfile.
        for f in glob.glob('foo/media/*'):
            name = os.path.basename(f)
            self.copy_file(f, os.path.join(full, name))
            self.compiled_files.append(os.path.join(media, name))


sys.argv.append('py2exe')

sys.path.append("C:\\Program Files\\Microsoft Visual Studio 9.0\\VC\\redist\\x86\\Microsoft.VC90.CRT")  # TODO
data_files = [
    #("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*')),  # TODO this doesn't quite work
    ("templates", glob(str(Path(__file__).parent / "templates" / "*.*")))]
setup(
    options={'py2exe': {'bundle_files': 1, 'compressed': True, 'excludes': ['tkinter'], "dll_excludes" : ["libcrypto-1_1.dll", "libssl-1_1.dll"]}},
    data_files=data_files,
    console=[{'script': 'solution.py', 'other_resources': []}],
    zipfile=None,
    cmdclass={'py2exe': MediaCollector})