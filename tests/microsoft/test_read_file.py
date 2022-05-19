class AdminCommandTests:

    def command(self):
        return ["ps", "aux"]

    def test_no_sudo(self):
        result = admin_command(self.command(), sudo=False)
        assert result == self.command()

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
        assert result == expected


def admin_command(command, sudo=True):
    """
    Prefix a command with `sudo` unless it is explicitly not needed. Expects
    `command` to be a list.
    """
    if sudo:
        return ["sudo"] + command
    return command