from collections.abc import Generator
from contextlib import contextmanager
from tempfile import NamedTemporaryFile
from typing import Any

import ffmpeg
import speech_recognition as sr


@contextmanager
def convert_audio_format(
    input_path: str, output_format: str = ".wav"
) -> Generator[str, Any]:
    with NamedTemporaryFile(suffix=output_format) as tmp_file:
        output_path = tmp_file.name
        ffmpeg.input(input_path).output(output_path).run(overwrite_output=True)
        yield output_path


def recognize_audio(file_path: str) -> dict[str | None, str | None]:
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="ru-RU")
        return {"text": text, "error": None}
    except sr.UnknownValueError:
        return {"text": None, "error": "Не удалось распознать голос."}
    except sr.RequestError:
        return {"text": None, "error": "Ошибка сервиса распознавания."}
    except Exception as e:
        return {"text": None, "error": str(e)}
