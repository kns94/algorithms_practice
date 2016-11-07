class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note = map(str, ransomNote)
        mag = map(str, magazine)

        note_count = {}
        mag_count = {}

        for notes in note:
            if notes not in note_count:
                note_count[notes] = 1
            else:
                note_count[notes] += 1

        for mags in mag:
            if mags not in mag_count:
                mag_count[mags] = 1
            else:
                mag_count[mags] += 1

        for key in note_count.keys():
            if key not in mag_count:
                return False
            else:
                if note_count[key] > mag_count[key]:
                    return False
            
        return True
