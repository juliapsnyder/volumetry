import re


class FileInfoExtractor:
    """Extracts information from filenames.

    This class provides a method to extract the mouse ID and imaging timepoint
    from a given filename using regular expressions.
    """
    @staticmethod
    def extract_info_from_filename(filename: str) -> tuple[str, str]:
      """Extracts mouse ID and imaging timepoint from a given filename.

      Parses the provided filename using regular expressions to find and return
      the mouse ID and the imaging timepoint. Hint: Both elements are separated by 
      spaces in the filename.

      Args:
          filename (str): The name of the file from which to extract the mouse ID
          and imaging timepoint.

      Returns:
          tuple: A tuple containing the mouse ID and imaging timepoint as strings.
          Returns (None, None) if the pattern is not found.
      """
      match = re.search(r'(\d{8}) (\w+) (\w+)', filename)
      if match:
          return match.group(2), match.group(3)  # Mouse ID, Imaging Timepoint
      return None, None
