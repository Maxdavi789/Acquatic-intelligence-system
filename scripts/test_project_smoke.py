"""Smoke test della baseline installata e dei punti di ingresso del progetto.

Uso:
    python scripts/test_project_smoke.py

Non elabora l'intero video: controlla che il default CLI punti al riferimento
ufficiale versionato, che MediaPipe legacy sia disponibile e che la dashboard
Streamlit completi un primo render senza eccezioni.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import mediapipe as mp  # noqa: E402
from streamlit.testing.v1 import AppTest  # noqa: E402

from scripts.analyze_video import DEFAULT_SOURCE  # noqa: E402


def check_default_video_is_official() -> None:
    expected = PROJECT_ROOT / "test_videos" / "profilo_test.mp4"
    assert DEFAULT_SOURCE.resolve() == expected.resolve(), (DEFAULT_SOURCE, expected)
    assert DEFAULT_SOURCE.is_file(), f"Video ufficiale assente: {DEFAULT_SOURCE}"


def check_mediapipe_legacy_pose_available() -> None:
    assert hasattr(mp, "solutions"), "mediapipe.solutions non disponibile"
    assert hasattr(mp.solutions, "pose"), "mediapipe.solutions.pose non disponibile"


def check_streamlit_initial_render() -> None:
    app = AppTest.from_file(str(PROJECT_ROOT / "app.py")).run(timeout=30)
    assert not app.exception, app.exception
    assert len(app.columns) == 2, len(app.columns)
    assert [title.value for title in app.title] == ["AI Swimming Motion Analyzer"]


def main() -> int:
    checks: list[tuple[str, Callable[[], None]]] = [
        ("default video ufficiale", check_default_video_is_official),
        ("MediaPipe legacy Pose", check_mediapipe_legacy_pose_available),
        ("render iniziale Streamlit", check_streamlit_initial_render),
    ]
    failures = 0
    for label, check in checks:
        try:
            check()
        except Exception as error:  # noqa: BLE001
            failures += 1
            print(f"[FAIL] {label}: {error}")
        else:
            print(f"[PASS] {label}")

    passed = len(checks) - failures
    print(f"Riepilogo smoke: {passed}/{len(checks)} passati, {failures} falliti")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
