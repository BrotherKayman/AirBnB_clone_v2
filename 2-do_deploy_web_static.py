#!/usr/bin/python3
"""Fabric script for distributing an archive to web servers."""
from fabric.api import task, env, put, run
from datetime import datetime
import os

env.hosts = ['100.27.13.34', '35.153.52.98']

@task
def do_pack():
    """Generates a .tgz archive from the contents of web_static folder."""
    formatted_dt = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir_command = "mkdir -p versions"
    archive_path = "versions/web_static_{}.tgz".format(formatted_dt)
    
    if local("{} && tar -cvzf {} web_static".format(mkdir_command, archive_path)).succeeded:
        return archive_path
    return None

@task
def do_deploy(archive_path):
    """Deploys package to remote server.

    Args:
        archive_path (str): Path to archive to deploy.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    try:
        if not os.path.exists(archive_path):
            return False

        filename_with_ext = os.path.basename(archive_path)
        filename_no_ext, extension = os.path.splitext(filename_with_ext)
        
        remote_path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")

        run("rm -rf {}{}/".format(remote_path, filename_no_ext))
        run("mkdir -p {}{}/".format(remote_path, filename_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(filename_with_ext, remote_path, filename_no_ext))

        run("rm /tmp/{}".format(filename_with_ext))
        run("mv {0}{1}/web_static/* {0}{1}/".format(remote_path, filename_no_ext))
        run("rm -rf {}{}/web_static".format(remote_path, filename_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(remote_path, filename_no_ext))

        return True
    except Exception:
        return False
