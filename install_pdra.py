import os
import subprocess
import sys

def find_apk_in_directory(directory):
    """
    確認資料夾中是否有唯一的 .apk 檔案並返回該檔案的完整路徑。
    """
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

def install_apk(apk_path, device):
    """
    安裝指定的 APK 檔案到裝置。
    """
    cmd_install = f'adb -s {device} install -r "{apk_path}"'
    result = subprocess.run(cmd_install, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"APK installed successfully on device {device}: {apk_path}")
        return True
    else:
        print(f"Failed to install APK on device {device}: {result.stderr}")
        return False

def get_connected_devices():
    """
    獲取所有已連接的裝置。
    """
    cmd_devices = 'adb devices'
    result = subprocess.run(cmd_devices, shell=True, capture_output=True, text=True)
    devices = [line.split()[0] for line in result.stdout.strip().splitlines() if '\tdevice' in line]

    if len(devices) == 0:
        print("No devices connected.")
    else:
        print(f"Connected devices: {devices}")
    return devices

def main():
    """
    主程式：檢查 APK 檔案並安裝到已連接的裝置。
    """
    if len(sys.argv) <= 1:
        print("Error: buildPath not provided.")
        sys.exit(1)

    build_path = sys.argv[1]
    print(f"Provided buildPath: {build_path}")

    apk_path = find_apk_in_directory(build_path)
    if not apk_path:
        print("No valid APK file found in the provided buildPath.")
        sys.exit(2)

    devices = get_connected_devices()
    if not devices:
        print("No devices available to install the APK.")
        sys.exit(3)

    device = devices[0]
    if install_apk(apk_path, device):
        print("Installation completed successfully.")
        sys.exit(0)
    else:
        print("Installation failed.")
        sys.exit(4)

if __name__ == "__main__":
    main()
