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
    inputs = ["John","Doe"]
    excepted = ["Hello John Doe","JoDo"]
    output = run(code, inputs).split("\n")
    if output == excepted:
        return True,"ผ่าน"
    else:
        return False, f"ไม่ผ่าน"
