from package_manager.manager import PackageManager
from shell_executer.executer import ShellExecuter

package_manager = PackageManager("debian")
command = package_manager.get_installation_command("linux_bridge")

print("Command is: " , command)

executer = ShellExecuter()
executer.execute_bash_command(True, command)