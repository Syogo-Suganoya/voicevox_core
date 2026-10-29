"""Rust側がインポートする例外クラスが、Python側で正しく定義されていることを確認する。"""

import pytest
import voicevox_core
from voicevox_core._rust import _EXCEPTION_NAMES


@pytest.mark.parametrize("name", _EXCEPTION_NAMES)
def test_exception_is_defined_in_python(name: str) -> None:
    exception = getattr(voicevox_core, name)
    assert isinstance(exception, type) and issubclass(exception, Exception)
    assert name in voicevox_core.__all__


def test_all_exceptions_are_imported_by_rust() -> None:
    exceptions = {
        name
        for name in voicevox_core.__all__
        if isinstance(attr := getattr(voicevox_core, name), type)
        and issubclass(attr, Exception)
    }
    assert exceptions == set(_EXCEPTION_NAMES)
