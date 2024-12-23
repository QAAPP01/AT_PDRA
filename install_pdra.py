import os
import re
import shutil
import subprocess
import sys

LOCAL_DIR = os.path.join("ATFramework_aPDR", "app")

# 提取 build number
def extract_build_number(filename):
    match = re.search(r"([0-9]+)\.apk$", filename)
    return int(match.group(1)) if match else None

# Local APK
def get_local_apk():
    apk_pattern = re.compile(r".*\.apk$")
    local_apk = None
    local_build_number = None

    os.makedirs(LOCAL_DIR, exist_ok=True)

    for filename in os.listdir(LOCAL_DIR):
        if apk_pattern.match(filename):
            local_apk = os.path.join(LOCAL_DIR, filename)
            local_build_number = extract_build_number(filename)
            break

    return local_apk, local_build_number

# Server 上的最新 APK 檔案
def find_latest_apk(root_dir):
    latest_apk = None
    latest_build_number = None
    apk_pattern = re.compile(r".*\.apk$")

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if apk_pattern.match(filename):
                build_number = extract_build_number(filename)
                if build_number is not None:
                    if latest_build_number is None or build_number > latest_build_number:
                        latest_build_number = build_number
                        latest_apk = os.path.join(dirpath, filename)

    return latest_apk, latest_build_number

# 更新 Local APK 檔案
def update_local_apk_if_needed(latest_apk, latest_build_number, local_build_number):
    if local_build_number is None or latest_build_number > local_build_number:
        os.makedirs(LOCAL_DIR, exist_ok=True)

        for file in os.listdir(LOCAL_DIR):
            file_path = os.path.join(LOCAL_DIR, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

        local_apk_path = os.path.join(LOCAL_DIR, os.path.basename(latest_apk))
        shutil.copy(latest_apk, local_apk_path)
        print(f"Updated local APK to: {local_apk_path}")
        return local_apk_path

    print("Local APK is already up to date.")
    return None

# 取得所有已連接的裝置
def get_connected_devices():
    cmd_devices = 'adb devices'
    result = subprocess.run(cmd_devices, shell=True, capture_output=True, text=True)
    devices = result.stdout.strip().splitlines()
    return [line.split()[0] for line in devices if '\tdevice' in line]

# 手動多裝置選取
def select_device(devices):
    print("Available devices:")
    for idx, device in enumerate(devices):
        print(f"{idx + 1}. {device}")

    while True:
        try:
            choice = int(input("Select a device by number: ")) - 1
            if 0 <= choice < len(devices):
                return devices[choice]
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

# 確認 APK 是否需要安裝，並安裝到裝置
def install_apk(apk_path, device):
    cmd_install = f'adb -s {device} install -r "{apk_path}"'
    result = subprocess.run(cmd_install, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Failed to install APK on device {device}: {result.stderr}")
        print("Attempting to uninstall existing app and reinstall.")

        package_name = get_package_name_from_apk(apk_path)
        if not package_name:
            print("Unable to extract package name from APK. Cannot uninstall existing app.")
            return False

        cmd_uninstall = f'adb -s {device} uninstall {package_name}'
        uninstall_result = subprocess.run(cmd_uninstall, shell=True, capture_output=True, text=True)

        if uninstall_result.returncode != 0:
            print(f"Failed to uninstall app {package_name} from device {device}: {uninstall_result.stderr}")
            return False

        print(f"Successfully uninstalled app {package_name} from device {device}.")

        reinstall_result = subprocess.run(cmd_install, shell=True, capture_output=True, text=True)
        if reinstall_result.returncode != 0:
            print(f"Failed to reinstall APK on device {device}: {reinstall_result.stderr}")
            return False

        print(f"APK reinstalled on device {device}: {apk_path}")
        return True

    print(f"APK installed on device {device}: {apk_path}")
    return True

# 提取 APK 檔案的 package 名稱
def get_package_name_from_apk(apk_path):
    cmd_aapt = f'aapt dump badging "{apk_path}"'
    result = subprocess.run(cmd_aapt, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')

    if result.returncode != 0:
        print(f"Failed to get package name from APK: {result.stderr}")
        return None

    output = result.stdout
    match = re.search(r"package: name='([^']+)'", output)
    return match.group(1) if match else None

# 複製 APK 到手機
def copy_apk_to_phone(apk_path, phone_dir, device):
    cmd_push = f'adb -s {device} push "{apk_path}" "{phone_dir}"'
    result = subprocess.run(cmd_push, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Failed to copy APK to device {device}: {result.stderr}")
        return False

    print(f"APK copied to device {device}: {phone_dir}")
    return True

# 管理手機資料夾中的 APK 檔案
def manage_phone_directory(phone_dir, device, max_files=36):
    cmd_ls = f'adb -s {device} shell ls -t "{phone_dir}"'
    result = subprocess.run(cmd_ls, shell=True, capture_output=True, text=True)
    files = result.stdout.strip().splitlines()

    if len(files) > max_files:
        for file in files[max_files:]:
            file_path = f"{phone_dir}/{file}"
            cmd_rm = f'adb -s {device} shell rm "{file_path}"'
            subprocess.run(cmd_rm, shell=True)
            print(f"Removed old APK from device {device}: {file_path}")

# 確保手機資料夾存在
def ensure_phone_dir_exists(phone_dir, device):
    cmd_check = f'adb -s {device} shell "test -d \\"{phone_dir}\\""'
    result = subprocess.run(cmd_check, shell=True)

    if result.returncode != 0:
        print(f"Directory {phone_dir} does not exist on device {device}. Creating it...")
        cmd_mkdir = f'adb -s {device} shell mkdir -p "{phone_dir}"'
        mkdir_result = subprocess.run(cmd_mkdir, shell=True, capture_output=True, text=True)

        if mkdir_result.returncode != 0:
            print(f"Failed to create directory {phone_dir} on device {device}: {mkdir_result.stderr}")
            return False

    print(f"Directory {phone_dir} is ready.")
    return True

def find_apk_in_directory(directory):
    if not os.path.isdir(directory):
        print(f"Provided buildPath is not a directory: {directory}")
        return None

    apk_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".apk")]
    if len(apk_files) == 0:
        print(f"No APK files found in directory: {directory}")
        return None
    elif len(apk_files) > 1:
        print(f"Multiple APK files found in directory: {directory}. Ensure only one APK is present.")
        return None

    return apk_files[0]

def main():
    devices = get_connected_devices()
    if not devices:
        print("No devices connected.")
        sys.exit(3)

    if len(sys.argv) <= 1:
        # 手動執行
        print("Running in manual mode. No buildPath provided.")
        root_dir = r"\\CLT-QASERVER\Testing\_SR_Build\PowerDirector Android\PowerDirector Android 14.0"
        phone_dir = r"/storage/emulated/0/Build/PDR"

        device = devices[0]
        if len(devices) > 1:
            device = select_device(devices)

        local_apk, local_build_number = get_local_apk()
        latest_apk, latest_build_number = find_latest_apk(root_dir)

        if latest_apk:
            updated_apk = update_local_apk_if_needed(latest_apk, latest_build_number, local_build_number)
            if updated_apk:
                local_apk = updated_apk

        if local_apk:
            install_apk(local_apk, device)
            if ensure_phone_dir_exists(phone_dir, device):
                copy_apk_to_phone(local_apk, phone_dir, device)
                manage_phone_directory(phone_dir, device)
    else:
        # Jenkins Trigger
        build_path = sys.argv[1]
        print(f"Provided buildPath: {build_path}")

        apk_path = find_apk_in_directory(build_path)
        if not apk_path:
            print("No valid APK file found in the provided buildPath.")
            sys.exit(2)

        device = devices[0]
        if install_apk(apk_path, device):
            print("Installation successful.")
            sys.exit(0)
        else:
            print("Installation failed.")
            sys.exit(4)

if __name__ == "__main__":
    main()
