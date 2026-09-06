# validkit

Eine kleine, eigenständige Python-Bibliothek mit neun unabhängigen, reinen Prüf- und
Normalisierungsfunktionen (E-Mail, Luhn, IBAN, ISBN-13, Telefon-E.164,
Akzent-Entfernung, Maskierung, Slugify, Clamp). Die Bibliothek kommt ohne CLI, ohne UI
und ohne Netzwerk aus und verwendet ausschließlich die Python-Standardbibliothek.

## Tech Stack

- **Sprache**: Python 3.9+
- **Frameworks**: keine — nur Standardbibliothek (`re`, `unicodedata`, `typing`)
- **Tests**: pytest

## Installation

```bash
pip install -e .
```

## Nutzung

```python
import validkit

validkit.is_valid_email("user@example.com")
validkit.luhn_check("79927398713")
```

Alle neun Funktionen sind direkt über das Paket verfügbar.

## Funktionen

Jede Funktion ist ein reiner, zustandsloser Aufruf. Ungültige Typen (z. B. `None` oder
Nicht-Strings) lösen einen `ValueError` aus, dessen Meldung nur den erwarteten Typ bzw.
das erwartete Format nennt — niemals den übergebenen Wert.

### `is_valid_email(text: str) -> bool`

Prüft, ob ein Text eine syntaktisch gültige E-Mail-Adresse ist.

```python
validkit.is_valid_email("user@example.com")  # -> True
```

### `luhn_check(digits: Union[str, int]) -> bool`

Prüft eine Ziffernfolge (z. B. eine Kreditkartennummer) gegen die Luhn-Prüfsumme.

```python
validkit.luhn_check("79927398713")  # -> True
```

### `is_valid_iban(text: str) -> bool`

Prüft eine IBAN (auch mit Leerzeichen gruppiert) über die Modulo-97-Prüfung.

```python
validkit.is_valid_iban("GB82 WEST 1234 5698 7654 32")  # -> True
```

### `is_valid_isbn13(text: str) -> bool`

Prüft eine ISBN-13 (Bindestriche und Leerzeichen werden toleriert).

```python
validkit.is_valid_isbn13("978-3-16-148410-0")  # -> True
```

### `normalize_phone(text: str, country_code: str) -> str`

Normalisiert eine Telefonnummer in das E.164-Format mit führendem `+` und Ländervorwahl.

```python
validkit.normalize_phone("0176 1234567", "DE")  # -> "+491761234567"
```

### `strip_accents(text: str) -> str`

Entfernt diakritische Zeichen.

```python
validkit.strip_accents("Café")  # -> "Cafe"
```

### `mask_secret(text: str, keep: int = 4) -> str`

Maskiert alle Zeichen bis auf die letzten `keep` Zeichen.

```python
validkit.mask_secret("abcd1234", keep=4)  # -> "****1234"
```

### `slugify(text: str) -> str`

Erzeugt einen URL-freundlichen Slug.

```python
validkit.slugify("Héllo, Wörld!")  # -> "hello-world"
```

### `clamp(value, low, high) -> Union[int, float]`

Begrenzt einen Wert auf den Bereich `[low, high]`.

```python
validkit.clamp(15, 0, 10)  # -> 10
```

## Tests

```bash
pytest
```
