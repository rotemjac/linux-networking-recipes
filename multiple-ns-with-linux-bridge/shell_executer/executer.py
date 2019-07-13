import subprocess


class ShellExecuter:
    def __init__(self):
        pass

    # Static method
    @classmethod
    def execute_bash_command(cls, with_sudo, command):
        sudo_prefix = "sudo" if with_sudo else ""

        # I created a list by using the following syntax / logic:
        # some_var = "sudo"  , some_list = ["apt", "install", "some-pkg"]
        # [some_var] + some_list =  ["sudo" ,"apt", "install", "some-pkg"]

        subprocess.run(
            [sudo_prefix] + command
        )


