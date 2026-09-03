import base64

class Solution:

    def __init__(self):
        self.delimiter = b'\xC0\xAF'

    def encode(self, strs: List[str]) -> str:
        encoded_parts = [s.encode('utf-8') for s in strs]
        joined = self.delimiter.join(encoded_parts)
        count_prefix = len(strs).to_bytes(4, 'big')  # 4-byte count prefix
        full_data = count_prefix + joined
        return base64.b64encode(full_data).decode('ascii')

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        raw = base64.b64decode(s.encode('ascii'))
        count = int.from_bytes(raw[:4], 'big')
        data = raw[4:]

        # Edge case: count = 0 → must return []
        if count == 0:
            return []

        parts = data.split(self.delimiter)
        
        # Pad the list with empty strings if needed (e.g., ["", ""])
        while len(parts) < count:
            parts.append(b'')

        return [p.decode('utf-8') for p in parts]