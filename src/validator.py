import ast

class CodeValidator:
    def is_syntax_valid(self, code):
        """
        Überprüft, ob der Code syntaktisch korrekt ist.
        """
        try:
            compile(code, "<string>", "exec")
            return True
        except SyntaxError:
            return False

    def has_testable_structures(self, code):
        """
        Überprüft, ob der Code Funktionen oder Klassen enthält.
        """
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    return True
            return False
        except SyntaxError:
            return False