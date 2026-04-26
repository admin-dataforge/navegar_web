import pytest

from src.web.utilidades.config import leer_config


class TestLeerConfig:
    def test_successful_yaml_loading(self, tmp_path):
        config_content = "site: propiedades\nlimit: 50\ntimeout: 30"
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        result = leer_config(str(config_file))

        assert result == {"site": "propiedades", "limit": 50, "timeout": 30}

    def test_raises_filenotfound_error_for_missing_file(self):
        with pytest.raises(FileNotFoundError):
            leer_config("/non/existent/path/config.yaml")

    def test_raises_valueerror_for_directory_path(self, tmp_path):
        directory = tmp_path / "subdir"
        directory.mkdir()

        with pytest.raises(ValueError):
            leer_config(str(directory))

    def test_expands_user_tilde_path(self, tmp_path, monkeypatch):
        config_content = "key: value"
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        monkeypatch.setenv("HOME", str(tmp_path))
        result = leer_config("~/config.yaml")

        assert result == {"key": "value"}

    def test_resolves_relative_path(self, tmp_path):
        config_content = "mode: test"
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        import os

        original_cwd = os.getcwd()
        try:
            os.chdir(tmp_path)
            result = leer_config("config.yaml")
            assert result == {"mode": "test"}
        finally:
            os.chdir(original_cwd)
