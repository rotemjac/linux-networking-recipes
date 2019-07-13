
class NetworkManager:
    def __init__(self,distribution):
        self.__distribution = distribution

        self.package_manager = {
            "debian": "apt",
            "ubuntu": "apt",
            "centos": "yum"
        }

        self.packages_names = {
            "linux_bridge": {
                "debian": "bridge-utils",
                "redhat": "bridge-utils"
            }
        }

        self.manage_command = self.package_manager[self.__distribution]


    def install_package(self, pkg_name):
        self.__execute_bash_command(True, pkg_name)

