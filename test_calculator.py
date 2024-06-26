import subprocess
from datetime import datetime


def run_calculator(operation, num1, num2):
    try:
        result = subprocess.run(
            ['docker', 'run', '--rm', 'public.ecr.aws/l4q9w4c5/loanpro-calculator-cli', operation, str(num1),
             str(num2)],
            capture_output=True, text=True, check=True, encoding="utf-8"
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()


def test_calculator():
    tests = [
        # Addition
        ("add", 8, 5, "Result: 13"),
        ("add", -3, 7, "Result: 4"),
        ("add", 1.00000001, 1.00000001, "Result: 2.0"),
        ("add", 1.0000001, 1.0000001, "Result: 2.0000002"),
        ("add", 0, 0, "Result: 0"),
        ("add", -0, 0, "Result: 0"),
        ("add", 1e-308, 1e-308, "Result: 2e-308"),
        ("add", 1e+308, -1e+308, "Result: 0"),
        ("add", 1.7976931348623157e+308, 1, "Result: 1.7976931348623157e+308"),

        # Subtraction
        ("subtract", 10, 3, "Result: 7"),
        ("subtract", -5, 4, "Result: -9"),
        ("subtract", 1.00000001, 1.00000001, "Result: 0.0"),
        ("subtract", 0, 0, "Result: 0"),
        ("subtract", -0, 0, "Result: 0"),
        ("subtract", 1e-308, 1e-308, "Result: 0"),
        ("subtract", 1e+308, 1e+308, "Result: 0"),
        ("subtract", 1.7976931348623157e+308, 1, "Result: 1.7976931348623157e+308"),

        # Multiplication
        ("multiply", 6, 7, "Result: 42"),
        ("multiply", -3, -2, "Result: 6"),
        ("multiply", 1.0000001, 1.0000001, "Result: 1.0000002"),
        ("multiply", 0, 0, "Result: 0"),
        ("multiply", -0, 0, "Result: 0"),
        ("multiply", 1e-308, 1e-308, "Result: 0"),  # Underflow to 0
        ("multiply", 1e+308, 1e+308, "Result: ∞"),  # Overflow to infinity
        ("multiply", 1.7976931348623157e+308, 1, "Result: 1.7976931348623157e+308"),

        # Division
        ("divide", 20, 4, "Result: 5"),
        ("divide", 10, 2, "Result: 5"),
        ("divide", 10, 0, "Error: Cannot divide by zero"),  # Assuming the error message contains 'error'
        ("divide", 0, 1, "Result: 0"),
        ("divide", 1e-308, 1e+308, "Result: 0"),
        ("divide", 1e+308, 1e-308, "Result: ∞"),  # Resulting in infinity
    ]

    report = []
    for operation, num1, num2, expected in tests:
        result = run_calculator(operation, num1, num2)
        if result == expected:
            report.append(f"Test passed: {operation} {num1} {num2} - Result: {result}")
        else:
            report.append(f"Test failed: {operation} {num1} {num2} - Expected: {expected}, Got: {result}")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"test_report_{timestamp}.txt"
    with open(report_filename, "w", encoding="utf-8") as f:
        for line in report:
            f.write(line + "\n")
    print(f"Test report generated: {report_filename}")


if __name__ == "__main__":
    test_calculator()
