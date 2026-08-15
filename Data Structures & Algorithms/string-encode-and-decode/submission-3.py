class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded = []
        for word in strs:
            # Format: <length>#<word>
            encoded.append(str(len(word)) + "#" + word)

        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0

        while i < len(s):
            # 1. Find where the '#' delimiter is AFTER index i
            j = s.find("#", i)

            # 2. Extract the full integer length (handles 1, 10, 100, etc.)
            length = int(s[i:j])

            # 3. Skip past the length digits and the '#' delimiter
            start_of_word = j + 1
            end_of_word = start_of_word + length

            # 4. Extract the exact word payload
            result.append(s[start_of_word:end_of_word])

            # 5. Jump pointer past the word directly to the next header
            i = end_of_word

        return result