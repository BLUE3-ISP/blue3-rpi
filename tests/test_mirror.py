"""Rewrite synthetic APT files without executing the Raspberry Pi bootstrap."""

from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class MirrorTest(unittest.TestCase):
    def rewrite(self, text, runs=1):
        with tempfile.TemporaryDirectory(prefix="blue3-apt-test-") as directory:
            path = Path(directory) / "sources"
            path.write_text(text)
            for _ in range(runs):
                subprocess.run(
                    ["bash", "-c", 'source "$1"; rewrite_debian_mirror "$2"',
                     "mirror-test", str(ROOT / "rpi_start.sh"), str(path)],
                    check=True, capture_output=True, text=True, timeout=5,
                )
            return path.read_text()

    def test_legacy_archive_urls_are_rewritten(self):
        for scheme in ("http", "https"):
            for host in ("deb.debian.org", "ftp.debian.org"):
                with self.subTest(scheme=scheme, host=host):
                    text = f"deb [signed-by=/usr/share/keyrings/debian-archive-keyring.gpg] {scheme}://{host}/debian trixie main\n"
                    self.assertEqual(
                        text.replace(f"{scheme}://{host}/debian", "http://mirror.blue3.com.br/debian"),
                        self.rewrite(text),
                    )

    def test_deb822_keeps_security_urls_and_archive_trailing_slashes(self):
        text = (
            "Types: deb deb-src\n"
            "URIs: https://deb.debian.org/debian/\n"
            "Suites: trixie trixie-updates\n\n"
            "Types: deb\n"
            "URIs: https://deb.debian.org/debian-security\n"
            "Suites: trixie-security\n"
        )
        self.assertEqual(
            text.replace("https://deb.debian.org/debian/\n", "http://mirror.blue3.com.br/debian/\n"),
            self.rewrite(text),
        )

    def test_security_and_other_repository_paths_are_preserved(self):
        for scheme in ("http", "https"):
            for host in ("deb.debian.org", "ftp.debian.org", "security.debian.org"):
                with self.subTest(scheme=scheme, host=host):
                    text = f"deb {scheme}://{host}/debian-security trixie-security main\n"
                    self.assertEqual(text, self.rewrite(text))
        text = "deb https://deb.debian.org/debian-ports unstable main\n"
        self.assertEqual(text, self.rewrite(text))

    def test_custom_mirrors_are_preserved(self):
        text = "deb https://mirror.example.test/debian trixie main\n"
        self.assertEqual(text, self.rewrite(text))

    def test_repeated_rewrites_are_idempotent(self):
        text = "URIs: http://deb.debian.org/debian https://deb.debian.org/debian-security\n"
        expected = "URIs: http://mirror.blue3.com.br/debian https://deb.debian.org/debian-security\n"
        self.assertEqual(expected, self.rewrite(text, runs=2))


if __name__ == "__main__":
    unittest.main()
