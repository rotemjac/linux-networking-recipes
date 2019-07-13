
class PackageManager:
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

    def get_installation_command(self, pkg_name):
        return [
            self.manage_command,
            "install",
            self.packages_names[pkg_name][self.__distribution]
        ]

