import contextlib
import io
import traceback

def run_student_code(code, input_data):
    output = ""
    try:
        with contextlib.redirect_stdout(io.StringIO()) as f:
            exec(code, {"__name__": "__main__"}, {"input": lambda: input_data.pop(0)})
        output = f.getvalue().strip()
    except Exception as e:
        output = f"Error: {traceback.format_exc(limit=1)}"
    return output

def evaluate(problem, test_cases, student_code):
    results = []
    for test in test_cases:
        expected = test["output"]
        input_data = test["input"].copy()
        student_output = run_student_code(student_code, input_data)
        correct = student_output == expected
        results.append({
            "input": test["input"],
            "expected": expected,
            "student_output": student_output,
            "correct": correct
        })
    return results

