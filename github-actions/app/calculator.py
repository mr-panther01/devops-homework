"""Small command-line calculator used by the CI/CD demo."""

from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation


def calculate(
    left: str | int | float | Decimal,
    operation: str,
    right: str | int | float | Decimal,
) -> Decimal:
    """Calculate one arithmetic operation using decimal arithmetic."""
    try:
        first = Decimal(str(left))
        second = Decimal(str(right))
    except (InvalidOperation, ValueError) as error:
        raise ValueError("operands must be valid numbers") from error

    if not first.is_finite() or not second.is_finite():
        raise ValueError("operands must be finite numbers")

    if operation == "+":
        return first + second
    if operation == "-":
        return first - second
    if operation == "*":
        return first * second
    if operation == "/":
        if second == 0:
            raise ValueError("division by zero is not allowed")
        return first / second

    raise ValueError(f"unsupported operation: {operation}")


def format_result(value: Decimal) -> str:
    """Format a decimal without unnecessary trailing fractional zeros."""
    formatted = format(value, "f")
    if "." in formatted:
        formatted = formatted.rstrip("0").rstrip(".")
    return formatted or "0"


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate two numbers.")
    parser.add_argument("left", help="first number")
    parser.add_argument("operation", choices=("+", "-", "*", "/"))
    parser.add_argument("right", help="second number")
    args = parser.parse_args()

    try:
        result = calculate(args.left, args.operation, args.right)
    except ValueError as error:
        parser.error(str(error))

    print(f"Result: {format_result(result)}")


if __name__ == "__main__":
    main()
