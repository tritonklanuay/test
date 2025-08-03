import contextlib
import io

def run(code,inputs):
    output = ""
    try:
        with contextlib.redirect_stdout(io.StringIO()) as f:
            exec(code, {'input': lambda: inputs.pop(0)})
        output = f.getvalue().strip()
    except Exception as e:
        return f"Error: {e}"
    return output

def check_A01(code):
    testcases = [
        {
            "inputs": ["2015"],
            "expected": ["10,ไม่บรรลุนิติภาวะ"]
        },
        {
            "inputs": ["2000"],
            "expected": ["25,บรรลุนิติภาวะ"]
        },
        {
            "inputs": ["2005"],
            "expected": ["20,บรรลุนิติภาวะ"]
        }
    ]

    for i, case in enumerate(testcases, 1):
        output = run(code, case["inputs"].copy()).split("\n")
        if output != case["expected"]:
            return False, f"ไม่ผ่าน"

    return True, "ผ่าน"
