from pathlib import Path
from shutil import copytree
import argparse

PROJECT_DIR = Path(__file__).resolve().parent
INSTALL_LINE = "COPY jumpbox /opt/CTFd/CTFd/plugins/jumpbox"
INSTALL_REQUIREMENTS_LINE = "RUN pip install -r /opt/CTFd/CTFd/plugins/jumpbox/requirements.txt"


def install(ctfd_path: Path, docker_file_name: str = "Dockerfile"):
    plugin_dir = PROJECT_DIR / "jumpbox"
    ctfd_path = Path(ctfd_path)
    dockerfile_path = ctfd_path.joinpath(docker_file_name)
    dest_dir = ctfd_path.joinpath("jumpbox")


    if not ctfd_path.exists():
        raise ValueError(f"The path {ctfd_path} does not exist.")
    if not ctfd_path.joinpath(docker_file_name).exists():
        if not ctfd_path.joinpath(docker_file_name.lower()).exists():
            raise ValueError(f"The specified compose file {docker_file_name} does not exist in {ctfd_path}.")
        else: 
            docker_file_name = docker_file_name.lower()
            dockerfile_path = ctfd_path.joinpath(docker_file_name)

    # Copy the project plugin into the CTFd directory
    if not dest_dir.exists():
        copytree(plugin_dir, dest_dir)
    
    # Modify the CTFd Dockerfile to include the plugin
    dockerfile_path.open("a").write("\n"+INSTALL_LINE+"\n"+INSTALL_REQUIREMENTS_LINE+"\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Install Jumpbox plugin to CTFd")
    parser.add_argument(
        "ctfd_path",
        type=str,
        help="Path to the CTFd directory",
    )
    parser.add_argument(
        "--docker_file_name",
        type=str,
        default="Dockerfile",
        help="Name of the Dockerfile to modify",
    )
    args = parser.parse_args()

    install(args.ctfd_path, args.docker_file_name)
