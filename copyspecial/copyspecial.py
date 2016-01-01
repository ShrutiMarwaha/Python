# code that uses file-system and external commands
import re
import os
import sys
import shutil
import argparse # for command-line interfaces
import commands
import subprocess

# get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory
# "special" file is one where the name contains the pattern __w__somewhere, where the w is one or more word chars.
def get_special_paths(dirs):
    '''
    get special paths

    :param dirs: directory to be listed.
    :return: list of special files
    '''

    output_list =[]
    # list of filenames in the directory 'dir'
    for dir in dirs:
        filenames = os.listdir(dir)
        for file_name in filenames:
            # proceed further only if the filename contains the special word/pattern
            if re.search("_(\w+)_",file_name):
                # given a path, return an absolute form
                absolute_path = os.path.abspath( os.path.join(dir,file_name))
                output_list.append(absolute_path)

    return output_list

# copy_to(paths, dir) given a list of paths, copies those files into the given directory
def copy_to(todir, sources):
    '''
    copy sources to todir directory

    :param todir: directory where files need to be copied
    :param sources: source files
    '''
    if not os.path.exists(todir):
        print("creating directory: [%s]" % todir)
        os.mkdir(todir)

    for source in sources:
        file_name = os.path.basename(source)
        destination = os.path.join(todir, file_name)
        print("copying file: [%s] to directory: [%s]" % (source, destination))
        shutil.copy(source, destination)

# zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile
def zipfile(tozip, sources):
    # Approach-1: Using subprocess module
    cmd = ['zip', '-j', tozip] + sources
    print("running command: [%s]" % ' '.join(cmd))
    subprocess.check_call(cmd)

    # Approach-2: Using commands module.
    #cmd = "zip -j %s %s" % (tozip, ' '.join(sources))
    #print "command to run:", cmd
    #(status, output) = commands.getstatusoutput(cmd)
    #if status:
    #    sys.stderr.write(output)
    #    sys.exit(1)
    #print output


def main(argv):
    '''

    :param argv:
    :return:
    '''

    # define parser
    parser = argparse.ArgumentParser(prog='copy_spec', description='copy spec')
    parser.add_argument('dirs', nargs='+', help='directories')
    parser.add_argument('--todir', help='copy to directory')
    parser.add_argument('--tozip', help='zip to directory')

    try:
        args = parser.parse_args(argv[1:])

        # compute special files
        sources = get_special_paths(args.dirs)

        if args.todir:
            copy_to(args.todir, sources)

        if args.tozip:
            zipfile(args.tozip, sources)

        if not args.todir and not args.tozip:
            print(sources)

    except Exception as e:
        print("Error: [%s]" % str(e))
        raise e

    return 0

if __name__ == "__main__":
  sys.exit(main(sys.argv))