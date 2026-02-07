class StringUtils:

    def capitalize(self, string: str) -> str:
        if isinstance(string, str):
            return string.capitalize()
        raise TypeError("string must be of type str")

    def trim(self, string: str) -> str:
        if isinstance(string, str):
            return string.strip()
        raise TypeError("string must be of type str")

    def contains(self, string: str, symbol: str) -> bool:
        if isinstance(string, str) and isinstance(symbol, str):
            return symbol in string
        raise TypeError("string and symbol must be of type str")

    def delete_symbol(self, string: str, symbol: str) -> str:
        if isinstance(string, str) and isinstance(symbol, str):
            return string.replace(symbol, "")
        raise TypeError("string and symbol must be of type str")
