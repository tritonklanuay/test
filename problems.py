problems = {
    "A01": {
        "description": "ให้พิมพ์ 'เลขคู่' ถ้าเป็นเลขคู่ หรือ 'เลขคี่' ถ้าเป็นเลขคี่",
        "testcases": [
            {"inputs": ["1"], "expected": ["เลขคี่"]},
            {"inputs": ["2"], "expected": ["เลขคู่"]},
        ],
        "required_keywords": ["input", "if", "else", "เลขคู่", "เลขคี่"],
    },
    "A02": {
        "description": "ให้พิมพ์ 'บวก' ถ้าตัวเลขมากกว่า 0 หรือ 'ลบ' ถ้าน้อยกว่า 0",
        "testcases": [
            {"inputs": ["5"], "expected": ["บวก"]},
            {"inputs": ["-3"], "expected": ["ลบ"]},
        ],
        "required_keywords": ["input", "if", "else", "บวก", "ลบ"],
    }
}