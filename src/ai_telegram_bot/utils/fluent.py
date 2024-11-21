from pathlib import Path
from fluent.runtime import FluentLocalization, FluentResourceLoader

def get_fluent_localization() -> FluentLocalization:
    """
    Load all '.ftl' locale files from 'l10n' directory
    :return: FluentLocalization object
    """
    # Убедимся, что директория существует и содержит файлы
    locale_dir = Path(__file__).parent.parent.joinpath("l10n")
    if not locale_dir.exists():
        raise FileNotFoundError("'l10n' directory not found")
    if not locale_dir.is_dir():
        raise NotADirectoryError("'l10n' is not a directory")
    
    # Собираем все .ftl файлы
    locale_files = list(locale_dir.glob("*.ftl"))
    if not locale_files:
        raise FileNotFoundError("No '.ftl' files found in 'l10n' directory")
    
    # Извлекаем коды локалей из имен файлов (например, "ru-RU", "en-US" и т.д.)
    locales = [file.stem for file in locale_files]  # .stem возвращает имя файла без расширения
    print(f"Detected locales: {locales}")

    # Создаём загрузчик ресурсов Fluent
    l10n_loader = FluentResourceLoader(str(locale_dir.absolute()))

    # Создаём объект FluentLocalization с найденными ресурсами
    return FluentLocalization(
        locales=locales,  # Передаем все локали, извлеченные из имен файлов
        resource_ids=[str(file.absolute()) for file in locale_files],
        resource_loader=l10n_loader,
    )
