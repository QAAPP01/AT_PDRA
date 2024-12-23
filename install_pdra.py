import os
import re
import shutil
import subprocess
import sys

LOCAL_DIR = os.path.join("ATFramework_aPDR", "app")


# 提取 build number
def extract_build_number(filename):
    match = re.search(r"([0-9]+)\.apk$", filename)
    if match:
        return int(match.group(1))
    return None


# 從本地資料夾中取得當前的 APK 檔案與其 build number
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


# 在網路目錄中找到最新的 APK 檔案
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


# 更新本地 APK，只有當新 APK 更新時才覆蓋本地版本
def update_local_apk_if_needed(latest_apk, latest_build_number, local_build_number):
    if local_build_number is None or latest_build_number > local_build_number:
        if not os.path.exists(LOCAL_DIR):
            os.makedirs(LOCAL_DIR)

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
    connected_devices = [line.split()[0] for line in devices if '\tdevice' in line]
    return connected_devices


def get_package_name_from_apk(apk_path):
    cmd_aapt = f'aapt dump badging "{apk_path}"'
    result = subprocess.run(cmd_aapt, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if result.returncode != 0:
        print(f"Failed to get package name from APK: {result.stderr}")
        return None

    output = result.stdout
    match = re.search(r"package: name='([^']+)'", output)
    if match:
        return match.group(1)
    else:
        print("Package name not found in APK.")
        return None


def install_apk_on_computer(apk_path, device):
    cmd_install = f'adb -s {device} install -r "{apk_path}"'
    result = subprocess.run(cmd_install, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed to install APK on device {device}: {result.stderr}")
        package_name = get_package_name_from_apk(apk_path)
        if not package_name:
            print("Unable to extract package name from APK. Cannot uninstall existing app.")
            return False

        cmd_uninstall = f'adb -s {device} uninstall {package_name}'
        uninstall_result = subprocess.run(cmd_uninstall, shell=True, capture_output=True, text=True)
        if uninstall_result.returncode != 0:
            print(f"Failed to uninstall app {package_name} from device {device}: {uninstall_result.stderr}")
            return False

        reinstall_result = subprocess.run(cmd_install, shell=True, capture_output=True, text=True)
        if reinstall_result.returncode != 0:
            print(f"Failed to reinstall APK on device {device}: {reinstall_result.stderr}")
            return False

        print(f"APK reinstalled on device {device}: {apk_path}")
        return True

    print(f"APK installed on device {device}: {apk_path}")
    return True


def main():
    root_dir = r"\\CLT-QASERVER\Testing\_SR_Build\PowerDirector Android\PowerDirector Android 14.0"
    phone_dir = r"/storage/emulated/0/Build/PDR"

    # 檢查是否傳入 APK 路徑
    if len(sys.argv) > 1:
        apk_path = sys.argv[1]
        print(f"Using provided APK path: {apk_path}")
    else:
        print("No APK path provided. Searching for latest APK.")
        local_apk, local_build_number = get_local_apk()
        latest_apk, latest_build_number = find_latest_apk(root_dir)
        apk_path = update_local_apk_if_needed(latest_apk, latest_build_number, local_build_number) or local_apk

    if not apk_path:
        print("No APK available to install.")
        return

    devices = get_connected_devices()
    if not devices:
        print("No devices connected.")
        return

    device = devices[0]
    install_apk_on_computer(apk_path, device)


if __name__ == "__main__":
    main()
