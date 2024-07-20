import subprocess


def ps_run(cmd: str) -> subprocess.CompletedProcess:
    """
    Run a command in PowerShell
    :param cmd: Command to run
    :return: CompletedProcess object
    """
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


def mount_win(abs_path: str) -> tuple[str, str] | None:
    """
    Mount an ISO file in Windows
    :param abs_path: Absolute path of the ISO file
    :return: (Drive letter, File system label)
    """
    cmd = (f"$result = Mount-DiskImage \"{abs_path}\" -PassThru ;" +
           "$drive = ($result | Get-Volume) ;" +
           "Write-Output $drive.DriveLetter ;" +
           "Write-Output $drive.FileSystemLabel")
    raw_output = ps_run(cmd)
    output = raw_output.stdout.decode("utf-8").strip()
    error = raw_output.stderr.decode("utf-8").strip()
    if error != "":
        print(error)
        return None
    output_lines = output.split('\n')
    drive = output_lines[0].strip()
    label = output_lines[1].strip()
    return drive, label


def unmount_win(abs_path: str) -> bool:
    """
    Dismount an ISO file in Windows
    :param abs_path: Absolute path of the ISO file
    :return: True if successful, False otherwise
    """
    cmd = f"Dismount-DiskImage \"{abs_path}\""
    raw_output = ps_run(cmd)
    output = raw_output.stdout.decode("utf-8").strip()
    error = raw_output.stderr.decode("utf-8").strip()
    if error != "":
        print(error)
        return False
    return True
