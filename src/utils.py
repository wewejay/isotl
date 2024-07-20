import subprocess


def ps_run(cmd: str) -> subprocess.CompletedProcess:
    """
    Run a command in PowerShell
    :param cmd: Command to run
    :return: CompletedProcess object
    """
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


def mount_win(abspath: str) -> tuple[str, str] | None:
    """
    Mount an ISO file in Windows
    :param abspath: Absolute path of the ISO file
    :return: (Drive letter, File system label)
    """
    cmd = (f"$result = Mount-DiskImage \"{abspath}\" -PassThru ;" +
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
