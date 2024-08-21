import subprocess
from typing import NamedTuple

from peewee import SqliteDatabase
from db import db


class OperationResult(NamedTuple):
    return_code: int
    output: str
    error: str
    results: list[any]


def ps_run(cmd: str) -> subprocess.CompletedProcess:
    """
    Run a command in PowerShell
    :param cmd: Command to run
    :return: CompletedProcess object
    """
    print(cmd)
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


def ps_read_results(raw_output: subprocess.CompletedProcess) -> OperationResult:
    """
    Read the results of a PowerShell command
    :param raw_output: CompletedProcess object
    :return: OperationResult object
    """
    output = raw_output.stdout.decode("utf-8")
    error = raw_output.stderr.decode("utf-8")
    return OperationResult(raw_output.returncode, output, error, [])


def mount_win(abs_path: str) -> OperationResult:
    """
    Mount an ISO file in Windows
    :param abs_path: Absolute path of the ISO file
    :return: OperationResult object
    """
    cmd = (f"$result = Mount-DiskImage \"{abs_path}\" -PassThru ;" +
           "$drive = ($result | Get-Volume) ;" +
           "Write-Output $drive.DriveLetter ;" +
           "Write-Output $drive.FileSystemLabel")
    result = ps_read_results(ps_run(cmd))
    if result.return_code != 0:
        return result
    output_lines = result.output.split('\n')
    drive = output_lines[0]
    label = output_lines[1]
    return OperationResult(result.return_code, result.output, result.error, [drive, label])


def unmount_win(abs_path: str) -> OperationResult:
    """
    Dismount an ISO file in Windows
    :param abs_path: Absolute path of the ISO file
    :return: OperationResult object
    """
    cmd = f"Dismount-DiskImage \"{abs_path}\""
    result = ps_read_results(ps_run(cmd))
    return result


def get_all_drives_win() -> OperationResult:
    """
    Get all drive letters in Windows
    :return: OperationResult object
    """
    cmd = "Get-Volume | Select-Object -ExpandProperty DriveLetter"
    result = ps_read_results(ps_run(cmd))
    if result.return_code != 0:
        return result
    drives = result.output.split('\n')
    return OperationResult(result.return_code, result.output, result.error, drives)


def get_iso_from_drive_letter_win(drive_letter: str) -> OperationResult:
    """
    Get the ISO file mounted on a drive letter in Windows
    :param drive_letter: Drive letter to check
    :return: OperationResult object
    """
    cmd = f"Get-Volume -DriveLetter {drive_letter} | Get-DiskImage | Select-Object -ExpandProperty ImagePath"
    result = ps_read_results(ps_run(cmd))
    if result.return_code != 0:
        return result
    iso_path = result.output
    return OperationResult(result.return_code, result.output, result.error, [iso_path])


def get_db(db_path: str) -> SqliteDatabase:
    """
    Connect to the database
    :param db_path: Path to the database
    :return: None
    """
    sqlite_db = SqliteDatabase(db_path)
    return sqlite_db


def init_db(db_path: str):
    """
    Initialize the database
    :param db_path: Path to the database
    :return: None
    """
    db.init(db_path)
    return None