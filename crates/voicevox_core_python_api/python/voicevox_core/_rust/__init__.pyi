import builtins
from typing import TYPE_CHECKING, NoReturn, SupportsIndex

if TYPE_CHECKING:
    from voicevox_core import (
        AccentPhrase,
        AudioQuery,
        FrameAudioQuery,
        FramePhoneme,
        Mora,
        Note,
        Score,
        UserDictWord,
    )

__version__: str

FRAME_RATE: float = 93.75
"""
フレームレート。

音声の秒数は ``frame_length / FRAME_RATE`` で表せる。

.. note::

    この定数は将来的に削除される可能性がある。例えば、 ``StyleMeta.frame_rate`` というフィールドに置き換えられる可能性がある。
"""

class AudioFeature:
    def __repr__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __len__(self) -> int:
        """
        総フレーム数。

        この ``AudioFeature`` を生成するときに用いた ``AudioQuery`` の
        :meth:`frame_length <AudioQuery.frame_length>` に等しい。
        """
        ...
    def __getitem__(
        self, slice: builtins.slice[SupportsIndex | None, SupportsIndex | None, None]
    ) -> AudioFeatureSlice:
        """
        ``slice`` に対応した :class:`AudioFeatureSlice` を返す。

        Parameters
        ----------
        slice
            範囲。
        """
        ...

class AudioFeatureSlice:
    """ある :class:`AudioFeature` 上の区間。"""

    def __init__(self, audio_feature: AudioFeature) -> None:
        """与えられた :class:`AudioFeature` の全体を表す ``AudioFeatureSlice`` を生成する。"""
        ...
    @property
    def audio_feature(self) -> AudioFeature:
        """元の :class:`AudioFeature`。"""
        ...
    @property
    def start_offset(self) -> int:
        """この ``AudioFeatureSlice`` の始端が、元の :class:`AudioFeature` のどの箇所にあたるか。"""
        ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __len__(self) -> int:
        """この ``AudioFeatureSlice`` が持つフレーム数。"""
        ...
    def __getitem__(
        self, slice: builtins.slice[SupportsIndex | None, SupportsIndex | None, None]
    ) -> AudioFeatureSlice:
        """
        この ``AudioFeatureSlice`` のサブスライスを返す。

        Parameters
        ----------
        slice
            範囲。
        """
        ...

_EXCEPTION_NAMES: list[str]
"""Rust側が ``voicevox_core`` からインポートする例外クラスの名前。テスト用。"""

class _ReservedFields:
    def __new__(cls, *args: object, **kwargs: object) -> NoReturn: ...

def _audio_query_from_accent_phrases(
    accent_phrases: list[AccentPhrase],
) -> AudioQuery: ...
def _audio_query_from_json(json: str) -> AudioQuery: ...
def _audio_query_to_json(audio_query: AudioQuery) -> str: ...
def audio_query_frame_length(
    audio_query: AudioQuery, enable_interrogative_upspeak: bool
) -> int: ...
def _validate_mora(mora: Mora) -> None: ...
def _validate_accent_phrase(accent_phrase: AccentPhrase) -> None: ...
def _validate_audio_query(audio_query: AudioQuery) -> None: ...
def _validate_user_dict_word(word: UserDictWord) -> None: ...
def _validate_note(note: Note) -> None: ...
def _validate_score(score: Score) -> None: ...
def _validate_frame_phoneme(frame_phoneme: FramePhoneme) -> None: ...
def _validate_frame_audio_query(frame_audio_query: FrameAudioQuery) -> None: ...
def _to_zenkaku(text: str) -> str: ...
def wav_from_s16le(pcm: bytes, sampling_rate: int, is_stereo: bool) -> bytes:
    """
    16bit PCMにヘッダを付加しWAVフォーマットのバイナリを生成する。

    Parameters
    ----------
    pcm : bytes
        16bit PCMで表現された音声データ
    sampling_rate: int
        入力pcmのサンプリングレート
    is_stereo: bool
        入力pcmがステレオかどうか

    Returns
    -------
    bytes
        WAVフォーマットで表現された音声データ
    """
    ...

def ensure_compatible(score: Score, frame_audio_query: FrameAudioQuery) -> None:
    """
    与えられた |ensure-compatible-score|_ と |ensure-compatible-frame-audio-query|_ の組み合わせが、基本周波数と音量の生成に利用できるかどうかを確認する。

    次のうちどれかを満たすなら
    |ensure-compatible-incompatible-queries-error|_ を送出する。

    - ``score`` が |ensure-compatible-score-validate|_ 。
    - ``frame_audio_query`` が |ensure-compatible-score-validate|_ 。
    - ``score`` が表す音素ID列と、 ``frame_audio_query.phonemes``
      が表す音素ID列が等しくない。ただし異なる音素の表現が同一のIDを表すことがある。

    .. |ensure-compatible-score| replace:: 楽譜
    .. _ensure-compatible-score: #voicevox_core.Score
    .. |ensure-compatible-frame-audio-query| replace:: 歌唱音声合成用のクエリ
    .. _ensure-compatible-frame-audio-query: #voicevox_core.FrameAudioQuery
    .. |ensure-compatible-incompatible-queries-error| replace:: ``IncompatibleQueriesError``
    .. _ensure-compatible-incompatible-queries-error: #voicevox_core.IncompatibleQueriesError
    .. |ensure-compatible-score-validate| replace:: 不正
    .. _ensure-compatible-score-validate: #voicevox_core.Score.validate
    .. |ensure-compatible-frame-audio-query-validate| replace:: 不正
    .. _ensure-compatible-frame-audio-query-validate: #voicevox_core.FrameAudioQuery.validate
    """
    ...
