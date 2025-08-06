import ast
import contextlib
import io

def run_code(code, inputs):
    try:
        with contextlib.redirect_stdout(io.StringIO()) as f:
            exec(code, {'input': lambda: inputs.pop(0)})
        return f.getvalue().strip().split("\n")
    except Exception as e:
        return [f"Error: {e}"]

def check_structure(code, keywords):
    try:
        tree = ast.parse(code)
    except:
        return False, "Error parsing code"

    code_str = code.replace(" ", "").replace("\n", "")
    for keyword in keywords:
        if keyword not in code:
            return False, f"ขาด '{keyword}'"
    return True, "ผ่าน"

def check_output(code, testcases):
    for case in testcases:
        output = run_code(code, case["inputs"].copy())
        if output != case["expected"]:
            return False, f"คาดว่า {case['expected']} ได้ {output}"
    return True, "ผ่าน"