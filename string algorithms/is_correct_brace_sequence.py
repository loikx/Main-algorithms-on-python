import unittest


def is_correct_brace_sequence(sequence: str) -> bool:
    """
    This function provides algorithm to check brace sequence.
    :param sequence: string or list[str] (sequence) that we need to check.
    :return: boolean value (True if sequence is correct else False)
    """
    # this algorithm work with stack
    stack = []
    for i in sequence:
        for j in '()', '{}', '[]':
            # if our brace is open type than we need to add it to stack
            if i == j[0]:
                stack.append(i)
                break
            if i == j[1]:
                # close type brace
                if not stack:
                    return False
                last_open_brace = stack.pop()
                # check current brace type with last open brace type
                if last_open_brace != j[0]:
                    return False
    # if we have more open type braces then close type braces
    # it's not correct sequence
    return len(stack) == 0


class Test(unittest.TestCase):
    def _checks(self, correct_sequences, wrong_sequences):
        for sequence in correct_sequences:
            self.assertTrue(is_correct_brace_sequence(sequence))

        for sequence in wrong_sequences:
            self.assertFalse(is_correct_brace_sequence(sequence))

    def test_round_braces(self):
        correct_sequences = ['(())', 'kadfasbdfjaskhdfasdfba.fabsdfasdf', '(ad)(asfv_)()()(()()()()()()())']
        wrong_sequences = ['())(', '(9(((((((()))))', '))))((((((', 'kuahsfah)s;(dlfhas;lf']
        self._checks(correct_sequences, wrong_sequences)

    def test_square_braces(self):
        correct_sequences = ['[][][][][][][]', '[[[[]]]]', '[[]][[[]]][]', '[as[da]s[d[s]]asd[as[s]d]dada]']
        wrong_sequences = ['][][][[[[]]]]]]]]', '[[[[[[[]]]]', '[[[[]]]]]]]]]]', 'ld[[[f]]]]]]]hasldfalsd[f]]]']
        self._checks(correct_sequences, wrong_sequences)

    def test_braces(self):
        correct_sequences = ['{{}{}{}{}{}{}{}{}}', '{{{{{{{}}}}}}}', 'aas{}d{{{}}}fas{{}}fa{sdf}a{{{{{{sd}}}}}}f']
        wrong_sequences = ['{{{{{{{{{{{{{{{{}}}}}}', '}}}}}}}}}}}}}}}{{{{{{{', '{{{{}}}}}}}}}}}}}', 'a{{{{s}aD}{']
        self._checks(correct_sequences, wrong_sequences)

    def test_mix_braces(self):
        correct_sequences = ['{([[]])}', '(adf[a{s}f]d)', '{((()[a]a))}', '{a(s)f[d]a[s]f{d}}']
        wrong_sequences = ['[)])', '[(])', 'lj(((((fk}}}}}}a[()()()()]lsdj{}{{{}fa', '{{{{{{(((((]{}}}}}}]]]]]']
        self._checks(correct_sequences, wrong_sequences)


if __name__ == '__main__':
    unittest.main()
