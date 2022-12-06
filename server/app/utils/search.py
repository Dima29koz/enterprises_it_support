def get_matches(value: str, objs: list[str]) -> list[str]:
    return [name for name in objs if name.lower().startswith(value.lower())]
